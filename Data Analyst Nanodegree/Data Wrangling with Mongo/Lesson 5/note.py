#!/usr/bin/env python
"""
The tweets in our twitter collection have a field called "source". This field describes the application
that was used to create the tweet. Following the examples for using the $group operator, your task is
to modify the 'make-pipeline' function to identify most used applications for creating tweets.
As a check on your query, 'web' is listed as the most frequently used application.
'Ubertwitter' is the second most used. The number of counts should be stored in a field named 'count'
(see the assertion at the end of the script).

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation pipeline
that can be passed to the MongoDB aggregate function. As in our examples in this lesson, the aggregation
pipeline should be a list of one or more dictionary objects.
Please review the lesson examples if you are unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine, you have to install MongoDB,
download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.

Please note that the dataset you are using here is a smaller version of the twitter dataset
used in examples in this lesson.
If you attempt some of the same queries that we looked at in the lesson examples,
your results will be different.
"""
import json
from pprint import pprint
import os
import codecs
os.chdir('/Users/admin/Desktop/Udacity_Github/Data Analyst Nanodegree/Data Wrangling with Mongo/Lesson 5')
def insert_data(data, db):
    for line in data:
        db.twitter.insert(line)


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    data = []
    with codecs.open('twitter.json', 'rU', 'utf-8') as f:
        count = 0
        for line in f:
            data.twitter.insert(line)
            count += 1
            if count >= 10:
                break
        insert_data(data, db)
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{ '$group' : {"_id" : "$source",
                             "count" : {"$sum" : 1}}},
                { '$sort' : {"count" : -1}}]
    return pipeline

def tweet_sources(db, pipeline):
    return [doc for doc in db.tweets.aggregate(pipeline)]

def highest_ratio(db):
	result = db.tweets.aggregate([
		{ "$match" : { "user.friends_count" : { "$gt" : 0},
					   "user.followers_count" : { "$gt" : 0} } },
		{ "$project" : { "ratio" : {"$divide" : ["$user.followers_count",
												 "$user.friends_count"]},
						 "screen_name" : "$user.screen_name"}},
		{"$sort" : {"ratio" : -1}},
		{"$limit" : 1}])


if __name__ == '__main__':
    db = get_db('twitter')
    pprint(db.twitter.find_one())
    result = highest_ratio(db)
    pprint(result)
    #assert result[0] == {u'count': 868, u'_id': u'web'}
