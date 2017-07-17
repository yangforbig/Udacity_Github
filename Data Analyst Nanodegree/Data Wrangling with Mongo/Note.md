Lesson 1. Data Extraction Fundamentals

1. What is data wrangling ?

The process of gathering, extracting, cleaning, and storing our data. 

2. We need to access our data to:

- Test Assumptions about:

(1) Test Values 

(2) Data Types

(3) Shape 

- Identify errors or outliers

- Finding Missing Values

3. Tabular Formats


4. CSV file 

CSV is lightweight

- Each line of text is single row

- Fields are separated by a delimiter

- Just the data itself

- Don't need special software

- all spreadsheets read/write csv

5. Whenever working with CSV file, using csv.DictReader


6. Data Modeling in JSON:

- Items may have different fields

- may have nested object

- may have nested array


Json tutorial:


If you're unfamiliar with JSON, or would just like a refresher, W3Schools has a great tutorial on the subject.

JSON Tutorial

You can also check out

http://www.json.org/

You can find information about Python's json module on this page of the Python documentation. 
Note that JSON arrays are interpreted as lists and JSON objects as dictionaries, 
so you can use the standard Python approaches to inspect JSON data.

Lesson 2 (extracting data from XML and scraping data from HTML)

1. (Goal of XML)[https://www.w3.org/TR/xml/#sec-origin-goals]

- Data Transfer

- Easy to write code to read/write

- Documentation Validation

- human readable 

- support a wide variety of apps

2. Best practice for scraping 

(1) Look at how a browser makes requests  (use requests.Session())

(2) Emulate in code

(3) if stuff blows up, look at your http traffic

(4) Return to 1 until get work

```
# parse xml

import xml.etree.ElementTree as ET
tree = ET.parse('file.xml')
root = tree.getroot()
for child in root:
	print child.tag
	
root.findall(xpath)


```

```
# scraping html file
from bs4 import BeautifulSoup
soup = BeautifulSoup(datafile, 'lmxl')
soup.find()
soup.find_all()

```


Lesson 4 

1. Measure of Data quality

- validity: conform to a schema

- accuracy: conform to golden standard

- completeness: all records

- consistency:  match other data

- uniformity:  same unit (measurements)

2. Blueprint for cleaning:

- audit your data

- create data cleaning plan

- execute plan 

- manually correct (human involved)

3. auditing validity is all about determining what constraints are on individual field and ensure

the field values adhere to the constraints.

4. auditing accuracy:

for example "Country data":

- Some values are arrays

- columns shift

- regex to the rescue 

- possibly valid countries

5. auditing completeness

- you don't know what you don't know

- missing records

- similar situation to accuracy

- need reference data

6. auditing consistency: two difference entries contradict each other


7. more of correcting data:

8. SQL or MongoDB

[SQL vs. NoSQL: The Differences](https://www.sitepoint.com/sql-vs-nosql-differences/)

[Should a Newbie Learn SQL or NoSQL?](https://www.quora.com/Should-a-newbie-learn-SQL-or-NoSQL)


Lesson 5

1. Data Modeling in MongoDB (Jason like syntax)


2. find the record of interests:

```

# find the number of total documents 

db.autos.find().count()

# find one document 

db.autos.find_one()


# find autos that have manufacture of "Toyota"

db.autos.find({"manufacturer" : "Toyota"}) 

# multiple field queries

autos = db.autos.find({"manufacturer" : "Toyota", "class" : "mid-size car"})

# using projection: describes the shape we would like the document to take in the result set.

# only name in result 
query = {"manufacturer" : "Toyota", "class" : "mid size car"}
projection = {"_id" = 0, "name" = 1}
db.auto.find(query, projection)

```

3. Getting data into MongoDB: 

insert data to MongoDB: 

(1) from CSV file into MongoBD:

```
input_data = csv.DictReader(open(input_file))
data = []
entry = {}
for row in input_data:
	for field, val in row.iteritems():
		entry[field] = val
	data.append(entry)

db.filename.insert(data)
	

(2) from json into MongoDB

mongoimport --help 

mongoimport -d database -c collections -file jsonfile 
mongoimport -d examples -c myautos --file autos.json

(3) when file has multiple json documents: 

```
data = []
with codecs.open('d:\output.txt','rU','utf-8') as f:
    for line in f:
       data.append(json.loads(line))

for line in data:
	db.collectionname.insert(line)
```

4. Operators 

- same operators in programming language

- same syntax as field name

- distinguish with $

(1) Range Operators 
``
# cities' population less equal than 5000000 and greater than 250000
query = {"population" : {"%gt" : 250000, "%lte" : 500000}}
cities = db.cities.find(query)

# cities capitalized between "X" and "Y"

query = {"population" : {"%gte" : "X", "%lte" : "Y"}}
ciites = db.cities.find(query)

# cities established between 1837,1,1 and 1837,12,31
```
query = {"foundingDate" : {"%gte" : datetime(1837, 1, 1),
							"%lte" : datetime(1837, 12 ,31)}}


(2) exist operator 

```
# cities have "govenmentType" field 

db.cities.find({"governmentType" : {"exists" : 1}}).count())
db.cities.find({"governmentType" : {"exists" : 1}}).pretty()# pretty print

```


5. Regex Operation


db.cities.find({"moto" : {"regex" : "[Ff]riendship|[Pp]ride"}})


6. Querying scalars using array

The powerful ability to query against fields that are not simply scalar values.
MongoDB searches inside the array value fields for individual values that match
by building the index on the fields, query will be very efficient


7. in operator or all

```
# modelYears at least contain one year in the list
db.autos.find{'modelYears' : {"$in" : [1965, 1866, 1967]}}

# model year contain all of the values in the list

db.autos.find{'modelYears' : {"$all" : [1965, 1866, 1967]}}


```

8. dot notation --> get inside the document 



db.tweets.find({"entities.hashtags" : {"$ne" : []}, {"entities.hashtags.text" : 1}})

9. save to update 

city = db.cities.find_one({"name" : "Germany"}) ---> return the first document 
city['id'] = 001 
db.cities.save(city) 

10 .set, unset to update 

update the first doc that found 

#
cities = db.cities.update({"name" : "Munche"},
							"%set" : "isCountryCode" : "DEU") # update isCountryCode
							
#				
cities = db.cities.update({"name" : "Munche"},
							"%unset" : "isCountryCode" : "") # disappear isCountryCode
							

Heads up:
			
cities = db.cities.update({"name" : "Munche"},
							{"isCountryCode" : "DEU"}) 
							
The entire document will be replaced a single field (isCountryCode)


11. Multi update

cities = db.cities.update({"name" : "Munche"},
							{"%set" : "isCountryCode" : "DEU"}, multi =True) # update isCountryCode

12. Removing document # similar to find

db.cities.remove() # remove one document
# remove the documents do not have name

db.cities.remove({"name" : {"$exist" : 0}})

db.cities.drop() # remove all the documents

Lesson 6 aggregational framework (built-in analytical tool)


1.  Aggregation pipeline 

collection --> stage 1 --> stage2 ---> .... ---> result 

$group and $sort

"_id" is mandatory arg

```
def most_tweets():
	result = db.tweets.aggregate([
								{"$group" : {"_id" : "$user.screen_name",
											 "count" : {"$sum" : 1}}},
											 {"$sort" : {"count" : -1 }}])
	return result

```

$ match  (filter operation)

# Who has the greatest followers to friends ratio?

db.tweets.aggregate([
		{ "$match" : { "user.friends_count" : { "$gt" : 0},
					   "user.followers_count" : { "$gt" : 0} } },
		{ "$project" : { "ratio" : {"$divide" : ["$user.followers_count",
												 "$user.friends_count"]},
						 "screen_name" : "$user.screen_name"}},
		{"$sort" : {"ratio" : -1}},
		{"$limit" : 1}])

 6. unwind （we want use the elements in the array area to analysze）
 
 create a copy of containing document for any array field
 
 # who included the most user mentions?
 ```
 db.tweets.find({"entities.user_mentions" : {"$size" : 3}}) # user_mentions field has the length of 3
 
 def user_mentions():
 	result = db.tweets.aggregate([
 					{"$unwind" : "$entities.user_mentions", 
 					{"$group" : {"_id" : "$user.screen_name",
 								"count" : {"$num" : 1}}},
 					{"$sort" : {"count" : -1 }},
 					{"$limit" : 1}])
 	return result
 	
 
 
 7. Group Accumulation Operators
 
 $sum
 $first
 $last
 $max
 $min
 $avg
 $push       (array)
 $addToSet		(array)
 
 def unique_hashtags_by_user():
 	result = db.tweets.aggregate([
 						{"$unwind" : "$entities.hashtags"},
 						{"$group" : {"_id" : "$user.screen_name",
 									 "unique_hashtags" : { "$addToSet" : "entities.hashtags.text"}}},
 						{"$sort" : {"_id" : -1}}])
 	return result
 	

8. Multiple Stages Using A Given Operator

# Who has mentioned the most unique users?

def mentioned_unique_users():
	result = db.tweets.aggregate([
		{"$unwind" : “$entities.user_mentions”},
		{"$group" : {"_id" : "user.screen_name",
					 "mset" : {"$addToSet" : $entities.user_mentions.screen_name}}},
		{"$unwind" : "mset"},
		{"$group" : { "_id" : "$_id", "count" : {"sum" : 1}},
		{"$sort" : { "count" : -1 },
		{$limit : 5} 
 
 
 9. Index ( DataBase performance)  (Hashtag, Date, username)
 
 collection scan (table scan )
 
 10. Geospatial  Indexes
 
 location : [x, y]
 
 ensureIndex
 
 $near 
 
 
 
 
 
 
 
 

