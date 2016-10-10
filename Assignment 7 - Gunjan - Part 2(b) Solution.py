# -*- coding: utf-8 -*-

# Assignment: 7
# Name: Gunjan Pravinchandra Pandya
# Part: 2(b)

#First, import the json module
import urllib.request as urllib
import json
import sqlite3

# Open a connection to database
conn = sqlite3.connect("Tweetdatabase.db")
# Request a cursor from the database
cursor = conn.cursor()

webFD=urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Assignment5.txt")

oldValue = 0
#allTweets = webFD.readline()
#allTweets = webFD.readline().decode("utf8")
for i in range(7000):
    #for line in allTweets:
        
        tweet = webFD.readline().decode("utf8")
        
        try:    
            jsonobject = json.loads(tweet)
            currentValue = jsonobject['user']['friends_count']
            if currentValue > oldValue:
                maxId = jsonobject['user']['id']
                maxName = jsonobject['user']['name']
                oldValue = jsonobject['user']['friends_count']
            
        except ValueError:
            None
            
print('User ID with highest friends_count: ' + str(maxId))
print('User Name with highest friends_count: ' + str(maxName))
print('Number of friends: ' + str(oldValue))
       
conn.commit()
conn.close()