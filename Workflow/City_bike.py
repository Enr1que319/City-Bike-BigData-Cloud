import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.conf import SparkConf
from pyspark.sql.session import SparkSession
from datetime import date

sc = SparkContext()
spark = SQLContext(sc)

files_name = ['2013-07 - Citi Bike trip data',
              '2013-08 - Citi Bike trip data',
              '2013-09 - Citi Bike trip data',
              '2013-10 - Citi Bike trip data',
              '2013-11 - Citi Bike trip data',
              '2013-12 - Citi Bike trip data',
              '2014-01 - Citi Bike trip data',
              '2014-02 - Citi Bike trip data'
             ]

bucket_name = "gs://enr1qu319-data-engineer-1"

for file in files_name:

    file_name = file

    citibike_data = spark.read.format("csv").option("header", "true").load(bucket_name+"/citi-bike/"+file_name+".csv")
    citibike_data.registerTempTable("citibike_data")
    # citibike_data.printSchema()

    qry = """
            select 
                starttime,
                `start station id`,
                `start station name`,
                tripduration,
                bikeid,
                usertype,
                gender
            from
                citibike_data
        """

    name_splt = file.split('-')
    second_parm = name_splt[1]
    month_splt = second_parm.split()
    file_name_output = name_splt[0] + '-' + month_splt[0] + '_selected_data'

    result = spark.sql(qry)
    output_data = bucket_name+"/citi-bike_data_output/"+file_name_output
    result.coalesce(1).write.format("csv").save(output_data)
    print('File ' + file_name_output + ' created')