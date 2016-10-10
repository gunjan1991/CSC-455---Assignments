# -*- coding: utf-8 -*-

# Assignment: 6
# Name: Gunjan Pravinchandra Pandya
# Part: 2(b)

#First, import the json module
import json
import sqlite3
# Open a connection to database
conn = sqlite3.connect("Tweetdatabase.db")
# Request a cursor from the database
cursor = conn.cursor() 
#you read the file through to the fd variable
fd = open('C:\Gunjan DePaul\CSC 455\Segment 6\Assignment6.txt', 'r', encoding='utf8') #similar to past reads for hw4, but we are encoding the bytes in this file

#then we need to parse its contents into a list of strings
allLines = fd.readline().split('EndOfTweet') #splits the lines on a delimiter and creates strings for each line
 
type(allLines[0]) #check type of first list item, making sure it is a string so that json can load it

fd.close()

# For each line in the file
# now we go through each line in the file to load it into an object using json API
for line in allLines:
    jsonobject = json.loads(line)
			#the json API parses the line as a json object so that we can call its items similar to calling dictionary keys and values
    
    if 'retweeted_status'in jsonobject.keys():
        jsonobject['retweet_count'] = jsonobject['retweeted_status']['retweet_count']
    else:
        jsonobject['retweet_count'] = jsonobject['retweet_count']
         
    cursor.execute("INSERT INTO TWEET VALUES (:created_at, :id_str, :text, :source, :in_reply_to_user_id, :in_reply_to_screen_name, :in_reply_to_status_id, :retweet_count, :contributors);", jsonobject)
    conn.commit()   #commiting every single time a record is inserted, as dictionary will have new tweet in every iteration

conn.close()