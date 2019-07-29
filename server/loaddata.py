import csv
from app import db
from app.models import Feature

def process_row(row):

    key, value = row[0], row[1]
    if '/' in value:
        values = [val.strip() for val in value.split('/')]
        for v in values:
            f = Feature(key=key, value=v)
            db.session.add(f)
        db.session.commit()
    else:
        f = Feature(key=key, value=value)
        db.session.add(f)
        db.session.commit()

if __name__ == '__main__':
    with open('features.csv', newline='') as infile:
        reader = csv.reader(infile)
        for row in reader:
            process_row(row)
