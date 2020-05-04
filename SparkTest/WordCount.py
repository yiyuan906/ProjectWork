from pyspark import SparkContext

if __name__ == "__main__":

	sc = SparkContext("local[3]", 'word count')
	
	lines = sc.textFile("Spark/spark-2.4.5-bin-hadoop2.7/README.md")
		
	words=lines.flatMap(lambda line: line.split(" "))
	
	wordCounts = words.countByValue()
	for word, count in wordCounts.items():
		print("{}:{}".format(word, count))
