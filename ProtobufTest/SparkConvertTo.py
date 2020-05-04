#! /usr/bin/env python

from __future__ import print_function
import Addressbook_pb2 							
import sys
from google.protobuf import json_format
import json
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

confz = SparkConf()\
.set("spark.hadoop.fs.s3a.endpoint","http://127.0.0.1:9000")\
.set("spark.hadoop.fs.s3a.access.key","minio")\
.set("spark.hadoop.fs.s3a.secret.key","minio123")\
.set("spark.hadoop.fs.s3a.path.style.access","true")\
.set("spark.hadoop.fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")

spark = SparkSession.builder.master("local[3]").appName("Test4").config(conf=confz).getOrCreate()

address_book = Addressbook_pb2.AddressBook()

if len(sys.argv) != 2:
  print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
  sys.exit(-1)

address_book = Addressbook_pb2.AddressBook()

with open(sys.argv[1], "rb") as f:			
  address_book.ParseFromString(f.read())

message=address_book						
json_string = json_format.MessageToDict(message)				
rddData = spark.sparkContext.parallelize(json_string)				
jsonframe=spark.read.json(rddData)							
jsonframe.write.mode("overwrite").format("json").save("s3a://spark-test/jsonconvert")	


