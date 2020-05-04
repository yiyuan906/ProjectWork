import pyspark
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

	confz = SparkConf().setAppName("blah").setMaster("local")
	sc = SparkContext(conf=confz)
	
	rdd = sc.parallelize(["a","b","c"])
	rdd.saveAsTextFile("home/yy/testtxt3")


