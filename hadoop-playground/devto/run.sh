#!bin/bash 

hadoop fs -rm -r /outputdevto

hadoop fs -rm -r /inputdevto

hdfs dfs -copyFromLocal hadoop-playground/devto/input /inputdevto

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar \
-files /hadoop-playground/devto/mapper.py,/hadoop-playground/devto/reducer.py \
-mapper mapper.py   -reducer reducer.py \
-input /inputdevto -output /outputdevto

hdfs dfs -ls /outputdevto
