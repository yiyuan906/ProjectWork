#! /usr/bin/env python

from __future__ import print_function
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

import Addressbook_pb2 									
import sys
from google.protobuf import json_format
import json
import glob
import errno

if __name__ == "__main__":
	confz = SparkConf()\
.set("spark.hadoop.fs.s3a.endpoint","http://127.0.0.1:9000")\
.set("spark.hadoop.fs.s3a.access.key","minio")\
.set("spark.hadoop.fs.s3a.secret.key","minio123")\
.set("spark.hadoop.fs.s3a.path.style.access","true")\
.set("spark.hadoop.fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")

	spark = SparkSession.builder.master("local[3]").appName("Test4").config(conf=confz).getOrCreate()
	
	ndf = spark.read.option("multiline","false").format("json").load("s3a://spark-test/jsontest")   

	ndf.write.mode("overwrite").format("json").save("/home/yy/fod/jsonfile")
		
	address_book = Addressbook_pb2.AddressBook()				
												
	json_dict = {}
	files = glob.glob("/home/yy/fod/jsonfile/*.json")					
	for name in files:								
		try:
			with open(name) as f:						
				json_dict.update(json.load(f))			
		except IOError as exc:
			if exc.errno != errno.EISDIR:
				raise

	address_book = json_format.ParseDict(json_dict, Addressbook_pb2.AddressBook())	
	with open(sys.argv[1], "wb") as f:
 		f.write(address_book.SerializeToString())
							


	

	
