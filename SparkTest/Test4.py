from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

if __name__ == "__main__":
	conf = SparkConf().setAppName("Tez").setMaster("local[3]")
	sc = SparkContext(conf=conf)

	cars=sc.textFile("Downloads/cars.csv").map(lambda x: x.split(";"))

	spark = SparkSession.builder.master("local[3]").appName("Test4").getOrCreate()
	
	df=spark.createDataFrame(cars,['Car','MPG','Cylinder','Displacement','HorsePower','Weight','Acceleration','Model','Origin'])
	
	df.createOrReplaceTempView("table1")
	
	df2 = spark.table("table1")

	for x in df.select('HorsePower','Car').collect():
		print(x)

	for y in spark.sql("select Car as c1, HorsePower as c2 from table1").collect():
		print(y)

	df.write.csv("/home/yy/Testfolder/testfile")
	
