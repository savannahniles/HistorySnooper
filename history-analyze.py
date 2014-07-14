import re
import sys
from calais import Calais #https://code.google.com/p/python-calais/

CALAIS_API_KEY = "an5duh4ktc5twbfysaakjhxs"
calais = Calais(CALAIS_API_KEY, submitter="historySnooper test")

f = open('history-sample.csv')
lines = f.readlines()
f.close()

class Topic:

	def __init__(self, name, value): #makes 1 call to users
		self.name = name
		self.value = value

class Entity:

	def __init__(self, name, value): #makes 1 call to users
		self.name = name
		self.value = value

topicsList = []
entitiesList = []
#id,lastVisitTime,title,typedCount,url,visitCount

lines.pop(0)
for line in lines:
	line = line.rstrip('\n')
	data = line.split(',')

	#here we want to create topics objects and entities objects with values related to visit count

	visitCount = data[-1]
	url = data[-2].replace('\"','')
	print url
	try:
		result = calais.analyze_url(url)
		print result
		# print result.topics
		print ""
		# print result.entities
		# print topics
		# for topic in topics:
			# t = Topic(name, visitCount)
    		# topics.append(t)
    	# print entities
    	# for entity in entities:
    	# 	e = Entity(name, visitCount*val)
    	# 	entities.append(e)
	except ValueError:
		print "This URL is fucked up. You need to deal with this in the future: %s" % (url)
	# except:
		# print "Unexpected error: ", sys.exc_info()[0]


