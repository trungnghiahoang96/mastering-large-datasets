#!bin/bash

hdfs dfs -rm -r /output07

hadoop fs -rm -r /input07

hdfs dfs -mkdir /input07

hdfs dfs -copyFromLocal hadoop-playground/Ch07/input/*.txt /input07

hdfs dfs -ls /input07

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar \
-files /hadoop-playground/Ch07/wc_mapper.py,/hadoop-playground/Ch07/wc_reducer.py \
-mapper wc_mapper.py   -reducer wc_reducer.py \
-input /input07 -output /output07


hdfs dfs -ls /output07

