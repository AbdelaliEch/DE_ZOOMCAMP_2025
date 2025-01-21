# DE-ZOOMCAMP-homework2

**Question 1:**    
**Answer:** 128.3 MB


**Question 2:**  
**Answer:** green_tripdata_2020-04.csv


**Question 3:**  
**Answer:** 24,648,499  
Query used: 
```sql
SELECT COUNT(1) FROM de_zoomcamp.yellow_tripdata WHERE filename LIKE "yellow_tripdata_2020-__.csv";
```



**Question 4:**  
**Answer:** 1,734,051  
Query used: 
```sql
SELECT COUNT(1) FROM de_zoomcamp.green_tripdata WHERE filename LIKE "green_tripdata_2020-__.csv";
```



**Question 5:**  
**Answer:** 1,925,152  
Query used: 
```sql
SELECT COUNT(1) FROM `de_zoomcamp.yellow_tripdata_2021_03`;
```


**Question 6:**  
**Answer:** Add a timezone property set to America/New_York in the Schedule trigger configuration

