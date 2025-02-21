FROM python:3.12

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pgcli

RUN wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
RUN command
WORKDIR /app
COPY ingest_data.py ingest_data.py 

# ENTRYPOINT [ "bash" ]
ENTRYPOINT [ "python", "ingest_data.py" , "--user", "root" , "--password" , "root" , "--host" , "pgdatabase" , "--port" , "5432" , "--db" , "ny_taxi" , "--table_name" , "yellow_taxi_data" , "--url" , "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz" ] 