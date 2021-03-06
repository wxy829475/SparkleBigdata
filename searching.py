#!/usr/bin/env python
from csv import reader
import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql import Row
import re

conf = SparkConf().setMaster("local").setAppName("Test")

text = sc.textFile("/user/tw1682/Bigdata/Project/result0",200)
textrdd = text.map(lambda x: Row(Key=x.split('\t')[0],Filename_Count=x.split('\t')[1]))
textframe = spark.createDataFrame(textrdd)

def search_startwith(textframe):
	return textframe.filter(textframe['Key'].startswith(query))


def search_accuracy(query):
	return textframe.filter(textframe['Key'] == query)


def search_contain(query):
	return textframe.filter(textframe['Key'].like('%'+query+'%'))


#multi query command
def search(querys):
	for query in querys:
		if re.match(r".+\*$",query):
			query = query[:-1]
			textframe=textframe.filter(textframe['Key'].startswith(query))
		elif re.match(r'^\*.+\*$',query):
			query = query[1:-1]
			textframe = textframe.filter(textframe['Key'].like('%'+query+'%'))
		else: #call_accuracy
			textframe = textframe.filter(textframe['Key'] == query)
	return textframe
