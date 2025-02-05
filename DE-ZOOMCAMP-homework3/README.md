# DE-ZOOMCAMP-homework3

## Data upload:
I used the kestra flow "homework3_data_upload.yaml" to upload the Yellow Taxi Trip Records for January 2024 - June 2024 (backfilling)

## BIG QUERY SETUP:  
Create an external table using the Green Taxi Trip Records Data for 2022.
```sql
CREATE OR REPLACE EXTERNAL TABLE `de_zoomcamp.yellow_tripdata_2024_external`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://kestra-project-448315-bucket/yellow_tripdata_2024-*.parquet']
);
```
Create a table in BQ using the Green Taxi Trip Records for 2022 (do not partition or cluster this table).
```sql
CREATE OR REPLACE TABLE `de_zoomcamp.yellow_tripdata_2024` AS
SELECT * FROM `de_zoomcamp.yellow_tripdata_2024_external`;
```

## Question 1:
Question 1: What is count of records for the 2024 Yellow Taxi Data?
- 65,623
- 840,402
- 20,332,093
- 85,431,289

We can just read table details or use a query
```sql
SELECT COUNT(1) FROM `de_zoomcamp.yellow_tripdata_2024`;
```
**Answer:** 20,332,093

## Question 2:
Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.</br> 
What is the **estimated amount** of data that will be read when this query is executed on the External Table and the Table?

- 18.82 MB for the External Table and 47.60 MB for the Materialized Table
- 0 MB for the External Table and 155.12 MB for the Materialized Table
- 2.14 GB for the External Table and 0MB for the Materialized Table
- 0 MB for the External Table and 0MB for the Materialized Table
```sql
SELECT COUNT(DISTINCT PULocationID) FROM `de_zoomcamp.yellow_tripdata_2024_external`;
SELECT COUNT(DISTINCT PULocationID) FROM `de_zoomcamp.yellow_tripdata_2024`;
```
**Answer:** 0 MB for the External Table and 155.12 MB for the Materialized Table

## Question 3:
Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table. Why are the estimated number of Bytes different?
- BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires 
reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.
- BigQuery duplicates data across multiple storage partitions, so selecting two columns instead of one requires scanning the table twice, 
doubling the estimated bytes processed.
- BigQuery automatically caches the first queried column, so adding a second column increases processing time but does not affect the estimated bytes scanned.
- When selecting multiple columns, BigQuery performs an implicit join operation between them, increasing the estimated bytes processed

**Answer:** BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

## Question 4:
How many records have a fare_amount of 0?
- 128,210
- 546,578
- 20,188,016
- 8,333  
```sql
SELECT COUNT(1) FROM `de_zoomcamp.yellow_tripdata_2024` WHERE fare_amount=0;
```
**Answer:** 8,333

## Question 5:
What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy)
- Partition by tpep_dropoff_datetime and Cluster on VendorID
- Cluster on by tpep_dropoff_datetime and Cluster on VendorID
- Cluster on tpep_dropoff_datetime Partition by VendorID
- Partition by tpep_dropoff_datetime and Partition by VendorID
```sql
CREATE OR REPLACE TABLE `de_zoomcamp.yellow_tripdata_2024_partitioned_clustered`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT * FROM `de_zoomcamp.yellow_tripdata_2024`;
```
**Answer:** Partition by tpep_dropoff_datetime and Cluster on VendorID

## Question 6:
Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime
2024-03-01 and 2024-03-15 (inclusive)</br>

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values? </br>

Choose the answer which most closely matches.</br> 

- 12.47 MB for non-partitioned table and 326.42 MB for the partitioned table
- 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table
- 5.87 MB for non-partitioned table and 0 MB for the partitioned table
- 310.31 MB for non-partitioned table and 285.64 MB for the partitioned table
```sql
SELECT DISTINCT(VendorID) FROM `de_zoomcamp.yellow_tripdata_2024`
WHERE tpep_dropoff_datetime>='2024-03-01 00:00:00' AND tpep_dropoff_datetime<='2024-03-15 00:00:00';

SELECT DISTINCT(VendorID) FROM `de_zoomcamp.yellow_tripdata_2024_partitioned_clustered`
WHERE tpep_dropoff_datetime>='2024-03-01 00:00:00' AND tpep_dropoff_datetime<='2024-03-15 00:00:00';
```
**Answer:** 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

## Question 7: 
Where is the data stored in the External Table you created?

- Big Query
- Container Registry
- GCP Bucket
- Big Table

**Answer:** GCP Bucket

## Question 8:
It is best practice in Big Query to always cluster your data:
- True
- False  

**Answer:** False
