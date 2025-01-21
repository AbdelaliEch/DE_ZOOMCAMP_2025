FROM python:3.9

RUN apt-get install wget 
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY ingest_data_green.py ingest_data_green.py

ENTRYPOINT [ "python3", "ingest_data_green.py" ]