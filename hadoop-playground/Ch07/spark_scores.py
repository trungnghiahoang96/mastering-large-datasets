#! /usr/bin/env python3
import re
from pyspark import SparkContext
from pyspark.sql import SparkSession


def score(word):
    total = 0
    for i, char in enumerate(word):
        if char.lower() in "dlcu":
            total += 1
        elif char.lower() in "mwfbygpvk":
            total += 2
        elif char.lower() in "jxqz":
            total += 4
        if i >= 4:
            total += 2
    return total


if __name__ == "__main__":
    sc = SparkContext(appName="WordScores")
    spark = SparkSession(sc)
    PAT = re.compile(r"[-./:\s\xa0]+")
    text_files = sc.textFile(
        "/home/nghiaht/pyspark/mastering-large-datasets/Ch07/*.txt"
    )
    # xs = text_files.flatMap(lambda x:PAT.split(x))\
    #                .filter(lambda x:len(x)>6)\
    #                .countByValue()\

    # for k,v in xs.items():
    #   print('{:<30}{}'.format(str(k.encode("ascii","ignore"))[1:],v))

    # print(type(xs)) --> default dict

    xs = (
        text_files.flatMap(lambda x: PAT.split(x))
        .filter(lambda x: len(x) > 10)
        .map(lambda x: (x, score(x)))
    )
    print(xs.collect())

    df = spark.createDataFrame(xs, ["word", "score"])
    df.show()
