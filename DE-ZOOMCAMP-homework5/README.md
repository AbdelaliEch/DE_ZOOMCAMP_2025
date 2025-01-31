## Module 5 Homework

### Question 1: 

**Install Spark and PySpark** 

- Install Spark
- Run PySpark
- Create a local spark session
- Execute spark.version.

Method used: I already installed Spark by following the videos. To run Pyspark, first I add this in the terminal
```bash
export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH"
```
Then I open python interpreter and run these commands
```bash
python

import spark

from pyspark.sql import SparkSession

spark = SparkSession.builder \
   .master("local[*]") \
  .appName('test') \
  .getOrCreate()

spark.version
```

Output: '3.4.4'

### Question 2: 

**FHV October 2019**

Read the October 2019 FHV into a Spark Dataframe with a schema as we did in the lessons.

Repartition the Dataframe to 6 partitions and save it to parquet.

What is the average size of the Parquet (ending with .parquet extension) Files that were created (in MB)? Select the answer which most closely matches.

- 1MB
- 6MB
- 25MB
- 87MB

For this question, I first downloaded the data using wget then I created the jupyter file "**homework5.ipynb**".  
For me, the size of each of the 6 parquet files was: 6.4MB, so:  
Answer: 6MB

### Question 3: 

**Count records** 

How many taxi trips were there on the 15th of October?

Consider only trips that started on the 15th of October.

- 108,164
- 12,856
- 452,470
- 62,610

> [!IMPORTANT]
> Be aware of columns order when defining schema

### Question 4: 

**Longest trip for each day** 

What is the length of the longest trip in the dataset in hours?

- 631,152.50 Hours
- 243.44 Hours
- 7.68 Hours
- 3.32 Hours



### Question 5: 

**User Interface**

Spark’s User Interface which shows the application's dashboard runs on which local port?

- 80
- 443
- 4040
- 8080



### Question 6: 

**Least frequent pickup location zone**

Load the zone lookup data into a temp view in Spark</br>
[Zone Data](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv)

Using the zone lookup data and the FHV October 2019 data, what is the name of the LEAST frequent pickup location Zone?</br>

- East Chelsea
- Jamaica Bay
- Union Sq
- Crown Heights North


## Submitting the solutions

- Form for submitting: https://courses.datatalks.club/de-zoomcamp-2024/homework/hw5
- Deadline: See the website
