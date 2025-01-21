# Question 1. Understanding docker first run  
**commands used**:     
```bash
docker run -it --entrypoint=bash python:3.12.8    
pip --version
```

# Question 3. Trip Segmentation Count
**queries used**:  
```sql  
SELECT COUNT(*) AS trip_count   
FROM green_taxi_trips    
WHERE lpep_pickup_datetime>='2019-10-01 00:00:00'   
AND lpep_dropoff_datetime<'2019-11-01 00:00:00'  
AND trip_distance<=1  

SELECT COUNT(*) AS trip_count   
FROM green_taxi_trips   
WHERE lpep_pickup_datetime>='2019-10-01 00:00:00'   
AND lpep_dropoff_datetime<'2019-11-01 00:00:00'  
AND trip_distance>1 AND trip_distance<=3

SELECT COUNT(*) AS trip_count 
FROM green_taxi_trips 
WHERE lpep_pickup_datetime>='2019-10-01 00:00:00' 
AND lpep_dropoff_datetime<'2019-11-01 00:00:00'
AND trip_distance>3 AND trip_distance<=7

SELECT COUNT(*) AS trip_count 
FROM green_taxi_trips 
WHERE lpep_pickup_datetime>='2019-10-01 00:00:00' 
AND lpep_dropoff_datetime<'2019-11-01 00:00:00'
AND trip_distance>7 AND trip_distance<=10

SELECT COUNT(*) AS trip_count 
FROM green_taxi_trips 
WHERE lpep_pickup_datetime>='2019-10-01 00:00:00' 
AND lpep_dropoff_datetime<'2019-11-01 00:00:00'
AND trip_distance>10
```

# Question 4. Longest trip for each day
**query used**:
```sql
SELECT DATE(lpep_pickup_datetime), 
       MAX(trip_distance) 
FROM green_taxi_trips 
GROUP BY 1 
ORDER BY 2 DESC
```

# Question 5. Three biggest pickup zones
**query used**:
```sql
SELECT "PULocationID", zones."Zone", SUM(total_amount) AS total_across_all_trips  
FROM green_taxi_trips JOIN zones ON
"PULocationID" = "LocationID"
WHERE DATE(lpep_pickup_datetime)='2019-10-18'
GROUP BY 1, 2
HAVING SUM(total_amount)>13000
ORDER BY 3 DESC
```

# Question 6. Largest tip
**query used**:
```sql
SELECT "PULocationID",
	   zp."Zone" AS pickup_zone,
	   "DOLocationID", 
	   zd."Zone" AS dropoff_zone,
	   tip_amount
FROM green_taxi_trips taxi
JOIN zones zp
ON taxi."PULocationID" = zp."LocationID"
JOIN zones zd
ON taxi."DOLocationID" = zd."LocationID"
WHERE lpep_pickup_datetime >= '2019-10-01 00:00:00'
AND lpep_pickup_datetime < '2019-11-01 00:00:00'
AND zp."Zone" = 'East Harlem North'
ORDER BY tip_amount DESC
```


