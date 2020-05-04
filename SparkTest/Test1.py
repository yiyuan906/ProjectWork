import pyspark
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

	confz = SparkConf()\
.setAppName("blah")\
.setMaster("local")\
.set("spark.hadoop.fs.s3a.endpoint","http://127.0.0.1:9000")\
.set("spark.hadoop.fs.s3a.access.key","minio")\
.set("spark.hadoop.fs.s3a.secret.key","minio123")\
.set("spark.hadoop.fs.s3a.path.style.access","true")\
.set("spark.hadoop.fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")

	sc = SparkContext(conf=confz)

	b1 = sc.textFile("s3a://spark-test/cars.csv")
	for x in b1.collect():
		print(x)

	b1.saveAsTextFile("/home/yy/Testfolder/testfolder2.text")


