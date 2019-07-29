import pycountry

CITY_STATES = ['Monaco', 'Singapore', 'Vatican City', 'Ceuta', 'Melilla',
    'Hong Kong', 'Macau', 'Gibraltar', 'Abu Dhabi', 'Ajman', 'Dubai',
    'Fujairah', 'Ras Al Khaimah', 'Sharjah', 'Umm Al Quwain',
    'Basel-Stadt', 'Berlin', 'Hamburg', 'Bremen']

CONTINENTS = ['Asia', 'Africa', 'America', 'North America', 'South America',
    'Europe', 'Antarctica', 'Australia']

EXCEPTIONS = ['England', 'Scotland', 'Wales', 'Curaçao', 'Curacao',
    'Sint Maarten']

def is_not_city(s):

    if s in CITY_STATES:
        return False

    if s in CONTINENTS:
        return True

    for cntry in pycountry.countries:
        if s == cntry.name:
            return True

    if s in EXCEPTIONS:
        return True

    return False
