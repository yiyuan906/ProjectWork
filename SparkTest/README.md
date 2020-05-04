# sparkTesting

Minio server setup by using "MINIO_ACCESS_KEY=minio MINIO_SECRET_KEY=minio123 ./minio server /home/yy/miniostorage"

Setup of Spark done with reference to this post https://github.com/minio/cookbook/blob/master/docs/apache-spark-with-minio.md

Things which differ from the referenced post:
-Spark 2.4.5 with hadoop is used 
-Hadoop not installed
-No paths set
-All jar files downloaded except "Hadoop 2.8.2"
-"Hadoop 2.7.3" and "aws java sdk 1.7.4" jar files are also added
  
Reading of files involving Spark and Minio needs to be done using ./spark-submit /path/to/program.py
