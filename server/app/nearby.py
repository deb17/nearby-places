import textwrap
from operator import itemgetter

from . import db
from .models import Feature
from .country import is_not_city

from geopy.distance import distance
from geopy.geocoders import Nominatim
import overpass
import inflect

geolocator = Nominatim(user_agent="nearby-places")
api = overpass.API()
p = inflect.engine()

MSG = 'Error: Improper key or value. Arbitrary values are not supported.'

def nearby(string, addr=None, lat=None, lon=None):

    if addr:
        addr = addr.replace('\r', '')
        addr = addr.replace('\n', ' ')
        location = geolocator.geocode(addr)
        if not location:
            return 'Error: Address not found. Enter approximate address.'
        lat = location.latitude
        lon = location.longitude

    if ' in ' not in string:
        return 'Error: Check usage.'

    item, city, *rest = [s.strip() for s in string.split(' in ')]

    if rest or not city:
        return 'Input formatting error.'

    city = city.title()
    if is_not_city(city):
        return 'Error: Invalid city name in query.'

    item = item.lower()
    pairs = query_db(item)

    if isinstance(pairs, str):
        return pairs

    osm_query = get_osm_query(pairs, city)

    try:
        data = api.get(osm_query, responseformat='json')
    except Exception:
        return 'Error in getting data.'
    else:
        if not data['elements']:
            return 'No data found. Could be an input formatting issue. ' + \
                'Also check with the list of allowed entities in the link' + \
                ' above.'
        return find_nearest(data['elements'], lat, lon)

def query_db(item):

    lst0 = [i.strip() for i in item.split(' ')]
    lst = [
              p.singular_noun(ele) if p.singular_noun(ele) else ele
              for ele in lst0
          ]

    if len(lst) not in (1,2):
        return 'Error: check usage.'

    if len(lst) == 2:
        x = Feature.query.filter_by(key=lst[0]).first()
        if not x:
            y = Feature.query.filter(
                Feature.value.in_([lst0[0], lst[0]])
            ).first()
            if not y:
                return MSG
            else:
                z = Feature.query.filter_by(key=lst[1]).first()
                if not z:
                    return MSG
                else:
                    return [(z.key, y.value)]
        else:
            y = Feature.query.filter(
                Feature.value.in_([lst0[1], lst[1]])
            ).first()
            if not y:
                return MSG
            else:
                return [(x.key, y.value)]

    row = Feature.query.filter_by(key=lst[0]).first()

    if not row:
        rows = Feature.query.filter(
            Feature.value.in_([lst0[0], lst[0]])
            ).all()

        if rows:
            pairs = [(r.key, r.value) for r in rows]
            return pairs
        else:
            return MSG
    else:
        key = row.key
        value = None
        return [(key, value)]

def get_osm_query(pairs, city):

    part1 = textwrap.dedent(f'''
        area[name={repr(city)}]->.searchArea;
        (
        ''').lstrip()

    part2 = ''.join(
                [f"node[{pair[0]}{'='+repr(pair[1]) if pair[1] else ''}]" +
                "(area.searchArea);\n" for pair in pairs]
            ) + ');'

    return part1 + part2

def find_nearest(lst, lat, lon):

    nodes = []

    for node in lst:
        name = node.get('tags').get('name')
        if not name: name = '<no name>'
        nlat = node['lat']
        nlon = node['lon']
        dist = round(distance((lat, lon), (nlat, nlon)).meters)

        nodes.append({'name': name, 'lat': nlat, 'lon': nlon, 'dist': dist})

    nodes.sort(key=itemgetter('dist'))

    user = {'name': '', 'lat': lat, 'lon': lon, 'dist': 0}
    output = nodes[:5]
    output.insert(0, user)

    return output

