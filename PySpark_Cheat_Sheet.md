``` python

import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

# create a SparkSession instance with the name moviedb with Hive support enabled
# https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html
spark = SparkSession.builder.appName("moviedb").enableHiveSupport().getOrCreate()

# create a SparkContext instance which allows the Spark Application to access 
# Spark Cluster with the help of a resource manager which is usually YARN or Mesos
sc = SparkContext.getOrCreate()

# create a SQLContext instance to access the SQL query engine built on top of Spark
sqlContext = SQLContext(spark)





#              READING DATA
# set the file_path variable in the beginning of the file
# or if your Spark application interacts with other applications, parameterize it
file_path = '/Users/kovid-r/datasets/moviedb/movies_metadata.csv'

# method 1 for reading a CSV file
df = spark.read.csv(file_path, header=True)

# method 2 for reading a CSV file
df = spark.read.format(csv_plugin).options(header='true', inferSchema='true').load(file_path)

# Reading a json file
df = spark.read.json(json_file_path)

# Reading a text file
df = spark.read.text(text_file_path)

# Reading a parquet file
df = spark.read.load(parquet_file_path) # or
df = spark.read.parquet(parquet_file_path)

# Reading a delta lake file
df = spark.read.format("delta").load(delta_lake_file_path)


#              WRITING DATA
# Write file to disk in parquet format partitioned by year - overwrite any existing file
df.write.partitionBy('year').format('parquet').mode('overwrite').save(parquet_file_path)

# Write file to disk in parquet format partitioned by year - append to an existing file
df.write.partitionBy('year').format('parquet').mode('append').save(parquet_file_path)

# Write data frame as a Hive table
df.write.bucketBy(10, "year").sortBy("avg_ratings").saveAsTable("films_bucketed")


#              MODIFYING DATAFRAMES
# Create a column with the default value = 'xyz'
df = df.withColumn('new_column', F.lit('xyz'))

# Create a column with default value as null
df = df.withColumn('new_column', F.lit(None).cast(StringType()))

# Create a column using an existing column
df = df.withColumn('new_column', 1.4 * F.col('existing_column'))

# Another example using the MovieLens database
df = df.withColumn('test_col3', F.when(F.col('avg_ratings') < 7, 'OK')\
                                 .when(F.col('avg_ratings') < 8, 'Good')\
                                 .otherwise('Great')).show()

# Create a column using a UDF

def categorize(val):
  if val < 150: 
    return 'bucket_1'
  else:
    return 'bucket_2'
    
my_udf = F.udf(categorize, StringType())

df = df.withColumn('new_column', categorize('existing_column'))
# Changing column name with withColumnRenamed feature
df = df.withColumnRenamed('existing_column_name', 'new_column_name')

# Changing column with selectExpr (you'll have to select all the columns here)
df = df.selectExpr("existing_column_name AS existing_1", "new_column_name AS new_1")

# Changing column with sparksql functions - col and alias
from pyspark.sql.functions import col
df = df.select(col("existing_column_name").alias("existing_1"), col("new_column_name").alias("new_1"))

# Changing column with a SQL select statement
sqlContext.registerDataFrameAsTable(df, "df_table")
df = sqlContext.sql("SELECT existing_column_name AS existing_1, new_column_name AS new_1 FROM df_table")

# Remove a column from a DataFrame
df.drop('this_column')

# Remove multiple columns in a go
drop_columns = ['this_column', 'that_column']
df.select([col for col in df.columns if column not in drop_columns])



# JOINS
# Joining two DataFrames
df1.join(df2, 'title', 'full')

# Another way to join DataFrames
df1.join(df2, 'title', how='left') 

# Cross join when you don't specify a key
df1.join(df2)

# Another way to join
df1.join(df2, df1.title == df2.title, how='left')

# PySpark supports lesser known join types such as semi left and anti left
df1.join(df2, on=['title'], how='left_anti')
df1.join(df2, on=['title'], how='left_semi')

# Left join in another dataset
df = df.join(person_lookup_table, 'person_id', 'left')

# Match on different columns in left & right datasets
df = df.join(other_table, df.id == other_table.person_id, 'left')

# Match on multiple columns
df = df.join(other_table, ['first_name', 'last_name'], 'left')

# Useful for one-liner lookup code joins if you have a bunch
def lookup_and_replace(df1, df2, df1_key, df2_key, df2_value):
    return (
        df1
        .join(df2[[df2_key, df2_value]], df1[df1_key] == df2[df2_key], 'left')
        .withColumn(df1_key, F.coalesce(F.col(df2_value), F.col(df1_key)))
        .drop(df2_key)
        .drop(df2_value)
    )

df = lookup_and_replace(people, pay_codes, id, pay_code_id, pay_code_desc)

```
# FILTERS
``` python 
# Filter movies with avg_ratings > 7.5 and < 8.2
df.filter((F.col('avg_ratings') > 7.5) & (F.col('avg_ratings') < 8.2)).show()

# Another way to do this
df.filter(df.avg_ratings.between(7.5,8.2)).show()
# Finding info of Ace Ventura films
df.where(F.lower(F.col('title')).like("%ace%")).show()

# Another way to do this
df.where("title like '%ace%'").show()

# Using where clause in sequence
df.where(df.year != '1998').where(df.avg_ratings >= 6.0)

# Filter on equals condition
df = df.filter(df.is_adult == 'Y')

# Filter on >, <, >=, <= condition
df = df.filter(df.age > 25)

# Multiple conditions require parentheses around each condition
df = df.filter((df.age > 25) & (df.is_adult == 'Y'))

# Compare against a list of allowed values
df = df.filter(col('first_name').isin([3, 4, 7]))

# Sort results
df = df.orderBy(df.age.asc()))
df = df.orderBy(df.age.desc()))
```

```python
# AGGREGATES
# Year wise summary of a selected portion of the dataset
df.groupBy('year')\
          .agg(F.min('budget').alias('min_budget'),\
               F.max('budget').alias('max_budget'),\
               F.sum('revenue').alias('total_revenue'),\
               F.avg('revenue').alias('avg_revenue'),\
               F.mean('revenue').alias('mean_revenue'),\
              )\
          .sort(F.col('year').desc())\
          .show()

# Pivot to convert Year as Column name and Revenue as the value
df.groupBy().pivot('year').agg(F.max('revenue')).show()



# WINDOW FUNCTIONS & SORTING
# As with most analysis engines, window functions have become quite the standard with rank, dense_rank , etc., being heavily used. Spark utilizes the traditional SQL based window function syntax of rank() over (partition by something order by something_else desc).


from pyspark.sql import Window

# Rank all the films by revenue in the default ascending order
df.select("title", "year", F.rank().over(Window.orderBy("revenue")).alias("revenue_rank")).show()

# Rank year-wise films by revenue in the descending order
df.select("title", "year", F.rank().over(Window.partitionBy("year").orderBy("revenue").desc()).alias("revenue_rank")).show()
df.filter(df.year != '1998').sort(F.asc('year'))
df.filter(df.year != '1998').sort(F.desc('year'))
df.filter(df.year != '1998').sort(F.col('year').desc())
df.filter(df.year != '1998').sort(F.col('year').asc())

df.filter(df.year != '1998').orderBy(F.asc('year'))
df.filter(df.year != '1998').orderBy(F.desc('year'))
df.filter(df.year != '1998').orderBy(F.col('year').desc())
df.filter(df.year != '1998').orderBy(F.col('year').asc())








# COMMON OPERATIONS
# Add a new static column
df = df.withColumn('status', F.lit('PASS'))

# Construct a new dynamic column
df = df.withColumn('full_name', F.when(
    (df.fname.isNotNull() & df.lname.isNotNull()), F.concat(df.fname, df.lname)
).otherwise(F.lit('N/A'))

# Pick which columns to keep, optionally rename some
df = df.select(
    'name',
    'age',
    F.col('dob').alias('date_of_birth'),
)

# Remove columns
df = df.drop('mod_dt', 'mod_username')

# Rename a column
df = df.withColumnRenamed('dob', 'date_of_birth')

# Keep all the columns which also occur in another dataset
df = df.select(*(F.col(c) for c in df2.columns))

# Batch Rename/Clean Columns
for col in df.columns:
    df = df.withColumnRenamed(col, col.lower().replace(' ', '_').replace('-', '_'))

```













