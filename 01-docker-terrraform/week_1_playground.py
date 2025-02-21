#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")

df_iter = pd.read_csv(
    "./yellow_tripdata_2021-01.csv", iterator=True, chunksize=100000, low_memory=False
)

for i, df in enumerate(df_iter):

  if i == 0:
    df.head(n=0).to_sql(con=engine, name="yellow_taxi_data", if_exists="replace")
  df.tpep_pickup_datetime = pd.to_datetime(df["tpep_pickup_datetime"])
  df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
  df.to_sql(con=engine, name="yellow_taxi_data", if_exists="append")




