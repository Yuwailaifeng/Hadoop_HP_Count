hadoop jar /usr/local/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar \
-file /home/hadoop/HPCount/mapper.py       -mapper /home/hadoop/HPCount/mapper.py \
-file /home/hadoop/HPCount/reducer.py       -reducer /home/hadoop/HPCount/reducer.py \
-input /HPCount/DPAll_Color.txt  -output /HPCount/Output
