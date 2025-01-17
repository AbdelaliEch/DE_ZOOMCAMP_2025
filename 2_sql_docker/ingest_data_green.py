import argparse
from sqlalchemy import create_engine
import pandas as pd
import os


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name

    url = params.url
    if url.endswith('.csv.gz'):
        csv_name = 'output_green.csv.gz'
    else:
        csv_name = 'output_green.csv'

    os.system(f'wget {url} -O {csv_name}')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    
    df.to_sql(name=table_name, con=engine, if_exists='append')

    while True:
        try:
            df = next(df_iter)
            
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
            
            df.to_sql(name=table_name, con=engine, if_exists='append')
            
            print('chunk injested...')
        except StopIteration:
            print('injestion completed')
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest csv data to postgres")
    
    parser.add_argument("--user", required=True, help="username for postgres")
    parser.add_argument("--password", required=True, help="password for postgres")
    parser.add_argument("--host", required=True, help="host for postgres")
    parser.add_argument("--port", required=True, help="port for postgres")
    parser.add_argument("--db", required=True, help="database for postgres")
    parser.add_argument("--table_name", required=True, help="name of the table where we will injest")
    parser.add_argument("--url", required=True, help="url of the csv file")
    
    args = parser.parse_args()
    
    main(args)




