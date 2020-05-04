import sys
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
	conf = SparkConf().setAppName("Testz").setMaster("local[2]")
	sc = SparkContext(conf=conf)
	
	cars=sc.textFile("Downloads/cars.csv")
	carname=cars.map(lambda x: x.split(";")) 
	
	for x in carname.collect():
		print("{}".format(x))
	
	
