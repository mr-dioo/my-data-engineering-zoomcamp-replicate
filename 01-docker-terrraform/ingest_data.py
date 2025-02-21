#!/usr/bin/env python
# coding: utf-8
import os
import argparse
import pandas as pd
from sqlalchemy import create_engine

def main(params):
    user=params.user
    password=params.password
    host=params.host
    port=params.port
    db=params.db
    table_name=params.table_name
    url=params.url

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    os.system("wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv -O taxi_zone_lookup.csv")

    os.system(f'wget {url} -O yellow_taxi_data.csv.gz')

    df_zones = pd.read_csv("taxi_zone_lookup.csv")

    df_zones.to_sql(name="zones", con=engine, if_exists="replace")

    df_iter = pd.read_csv(
        "./yellow_taxi_data.csv.gz", iterator=True, chunksize=100000, low_memory=False
    )

    for i, df in enumerate(df_iter):

        if i == 0:
            df.head(n=0).to_sql(con=engine, name=f"{table_name}", if_exists="replace")
        df.tpep_pickup_datetime = pd.to_datetime(df["tpep_pickup_datetime"])
        df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
        df.to_sql(con=engine, name=f"{table_name}", if_exists="append")

if __name__ == '__main__':
  
  parser = argparse.ArgumentParser()
  parser.add_argument("--user",required=True, help="database username" )
  parser.add_argument("--password",required=True, help="database password" )
  parser.add_argument("--host",required=True, help="host name of database server" )
  parser.add_argument("--port",required=True, help="port of the host" )
  parser.add_argument("--db",required=True, help="database name" )
  parser.add_argument("--table_name" , required=True, help="table_name")
  parser.add_argument("--url" , required=True, help="url to download the file")
  
  args = parser.parse_args()
  
  main(args)
