#!bin/bash


hdfs dfs -rm -r /tennis_rating

hadoop fs -rm -r /input08


hdfs dfs -mkdir /input08

hdfs dfs -copyFromLocal hadoop-playground/Ch08/input/*.csv /input08


hdfs dfs -ls /input08

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar \
-files /hadoop-playground/Ch08/elo-mapper.py,/hadoop-playground/Ch08/elo-reducer.py \
-mapper elo-mapper.py -reducer elo-reducer.py \
-input /input08 -output /tennis_rating

hdfs dfs -ls /tennis_rating
