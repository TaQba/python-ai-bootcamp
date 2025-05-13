import sqlalchemy_create
import csv
from datetime import date
from sqlalchemy import text
code_ids = {}


def insert_stations():
    with open('M6/clean_stations.csv', newline='') as f:
        reader = csv.reader(f)
        stations = list(reader)

    ignore_column = True
    for station in stations:
        if ignore_column:
            ignore_column = False
            continue
        ins = sqlalchemy_create.stations.insert().values(
            code=station[0],
            name=station[4],
            latitude=station[1],
            longitude=station[2],
            elevation=station[3],
            country=station[5],
            state=station[6]
        )

        result = conn.execute(ins)
        code_ids[station[0]] = result.inserted_primary_key[0]


def insert_measurements():
    with open('M6/clean_measure.csv', newline='') as f:
        reader = csv.reader(f)
        measures = list(reader)
    ignore_column = True
    for measure in measures:
        if ignore_column:
            ignore_column = False
            continue
        date_str = measure[1].split("-")
        ins = sqlalchemy_create.measures.insert().values(
            station_id=code_ids[measure[0]],
            date=date(int(date_str[0]), int(date_str[1]), int(date_str[2])) if len(date_str) == 3 else None,
            precip=measure[2],
            tobs=measure[3]
        )

        conn.execute(ins)


def select_stations(limit=5):
    s = sqlalchemy_create.stations.select().limit(limit)
    result = conn.execute(s)

    for row in result:
        print(row)


if __name__ == "__main__":
    conn = sqlalchemy_create.engine.connect()
    insert_stations()
    insert_measurements()
    select_stations(5)
    conn.close()
