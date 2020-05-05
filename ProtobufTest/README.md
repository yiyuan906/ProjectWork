# protobufTesting

The Addressbook.proto is the file which contains the structure of the message, when it is ran through the protobuf compiler, it can be imported in the python program to perform read/write operation referencing it.

To make use of "add_person.py" which demostrates usage of the protobuf message, use python and execute it. "python /path/to/add_person.py datafile.data" This will create or add onto the datafile.data which can later be used for reading purposes.
"list_people.py" is the file which can read the datafile which was created. 

My own testing up to this point includes conversion of the .data files to json only. The file name shows what the program does, for example "pyJsonConvDirec" would convert the json version of the message data back to the message data original .data format. 

The two Spark examples in this folder makes use of the README setting on the SparkTestfolder. As such to run it, use "./spark-submit /path/to/SparkConvertTo.py /path/to/datafile.data". Assuming that the setup is done correctly, the processed file would be under the spark-test bucket with a "jsonconvert" file which holds the information of the message data in json. 
To run the other file, it is the same, just that "path/to/datafile.data" would be where and what the datafile would be renamed to according to the spark-submit. 
("ndf.write.mode("overwrite").format("json").save("/home/yy/fod/jsonfile")" in the code saves the json file directly)

"add_person.py" and "list_people.py" are taken from the downloaded protobuf package was used to help with the testing.  
