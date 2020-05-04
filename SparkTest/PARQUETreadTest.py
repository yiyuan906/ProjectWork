from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

if __name__ == "__main__":
	confz = SparkConf()\
.set("spark.hadoop.fs.s3a.endpoint","http://127.0.0.1:9000")\
.set("spark.hadoop.fs.s3a.access.key","minio")\
.set("spark.hadoop.fs.s3a.secret.key","minio123")\
.set("spark.hadoop.fs.s3a.path.style.access","true")\
.set("spark.hadoop.fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")

	spark = SparkSession.builder.master("local[3]").appName("PARQUETread").config(conf=confz).getOrCreate()
	
	ndf = spark.read.format("parquet").load("s3a://spark-test/userdata1.parquet") 
	for x in ndf.collect():
		print(x)

	ndf.write.partitionBy("gender").mode("overwrite").format("parquet").save("/home/yy/Testfolder/parquetfile") 

		

	

	
