# -*- coding: utf-8 -*-

# Assignment: 7
# Name: Gunjan Pravinchandra Pandya
# Part: 1(b)

#First, import the json module

import urllib.request as urllib
import json
import sqlite3

# Open a connection to database
conn = sqlite3.connect("Tweetdatabase.db")
# Request a cursor from the database
cursor = conn.cursor()
cursor.execute('pragma foreign_keys=ON')
webFD=urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Assignment5.txt")
count = 0;
badTweets = 0;
output = open("C:\Gunjan DePaul\CSC 455\Segment 8\BadTweets.txt", "w")
#allTweets = webFD.readline()
#allTweets = webFD.readline().decode("utf8")
for i in range(7000):
    
        tweet = webFD.readline().decode("utf8")
     
        try:    
            jsonobject = json.loads(tweet)
        
            if 'retweeted_status' in jsonobject.keys():
                retweetcount = jsonobject['retweeted_status']['retweet_count']
            else:
                retweetcount = jsonobject['retweet_count']
        
            uservalues = (jsonobject['user']['id'], jsonobject['user']['name'], jsonobject['user']['screen_name'], jsonobject['user']['description'], jsonobject['user']['friends_count'])
            tweetvalues = (jsonobject['created_at'], jsonobject['id_str'], jsonobject['text'], jsonobject['source'],jsonobject['in_reply_to_user_id'], jsonobject['in_reply_to_screen_name'], jsonobject['in_reply_to_status_id'], retweetcount, jsonobject['contributors'], jsonobject['user']['id']) 
            cursor.execute("INSERT OR IGNORE INTO USER VALUES(?,?,?,?,?);",uservalues)
            cursor.execute("INSERT INTO TWEET VALUES(?,?,?,?,?,?,?,?,?,?);",tweetvalues)
            #print(tweetvalues)
            
        except ValueError:
      # Handle the problematic tweet, which in your case would require writing it to another file
            output.write("%s;\n" % str(tweet.encode('utf8')) )
            
        except Exception:       #for unique id constraint errors
            count = count + 1;
            
print(count)        #number of unique id constraint errors
output.close()            
conn.commit()
conn.close()