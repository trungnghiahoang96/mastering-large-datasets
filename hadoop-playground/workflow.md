Using docker from repo: https://github.com/jware-solutions/docker-big-data-cluster 

 

 

Final hadoop workflow: 

Adding mount file path for master-node to docker-compose yaml 

/home/nghiaht/hadoop/hadoop-playground:/hadoop-playground 

docker-compose up 

docker exec -it master-node bash 

example of testing map reduce job at command line: 

hdfs dfs -cat /inputdevto/*.txt  |/hadoop-playground/devto/mapper.py| sort -k1,1 | /hadoop-playground/devto/reducer.py 

Find out path of executable hadoop streaming at: 

/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar 

Create run.sh 

Delete output for multiple rerun 

Remember chmod a+x this new file run.sh 

 

*************************************************************************** 

#!bin/bash 

hadoop fs -rm -r /outputdevto 

hadoop fs -rm -r /inputdevto 

hdfs dfs -copyFromLocal hadoop-playground/devto/input /inputdevto 

 

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar \ 

-files /hadoop-playground/devto/mapper.py,/hadoop-playground/devto/reducer.py \ 

-mapper mapper.py   -reducer reducer.py \ 

-input /inputdevto -output /outputdevto  

hdfs dfs -ls /outputdevto 

 

Check out result 

hdfs dfs -ls outputdevto 

hdfs dfs -cat outputdevto/part-00000 

 

***************************************************************************  

Run.sh for mapreduce map for Ch07 

 

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

 

 ---> hdfs dfs -cat outputdevto/part-00000 

**************************************************************************** 

Ch08:  

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

 

 

 

 

 
