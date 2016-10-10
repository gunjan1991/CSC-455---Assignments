# -*- coding: utf-8 -*-

# Assignment: 7
# Name: Gunjan Pravinchandra Pandya
# Part: 3

import urllib.request as urllib
import json
import sqlite3
import operator
# Open a connection to database
conn = sqlite3.connect("Tweetdatabase.db")
# Request a cursor from the database
cursor = conn.cursor()
webFD=urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Assignment5.txt")
dCount={}
#allTweets = webFD.readline()
#allTweets = webFD.readline().decode("utf8")
for i in range(7000):
    
        tweet = webFD.readline().decode("utf8")
     
        try:
            jsonobject = json.loads(tweet)
            text = jsonobject['text']
            words = text.split()
            
            #print(words)
            for word in words:
                if word not in dCount:
                    dCount[word] = 0
                dCount[word] = dCount[word]+1
            countKeys = dCount.keys()
            countVals = dCount.values()            
            countPairs = zip(countVals, countKeys)
        
        except ValueError:
           None        
      
sorted_countPairs=sorted(countPairs, key=operator.itemgetter(0) , reverse=True)
print(sorted_countPairs)
print('Top three most frequent terms in the text of the tweets are: ' + str(sorted_countPairs[0][1]) + ', ' +str(sorted_countPairs[1][1]) + ', ' +str(sorted_countPairs[2][1]))
conn.close()