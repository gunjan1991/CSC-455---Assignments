# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 1(d)
"""
1 (d). Use your locally saved tweet file (created in part-b) to repeat the database population step from part-c. 
That is, load 500,000 tweets into the 3-table database using your saved file with tweets (do not use the URL to 
read twitter data). How does the runtime compare with part-c?

-> Runtime: 15.66 minutes
-> No of records: 
Geo: 11849
User: 447304
Tweet: 499776
-> Compared to loading the data from URL (part-c) this approach of loading data from text file took less time.
"""

import json
import sqlite3
import time
import html

start = time.time()

# Open a connection to database
conn = sqlite3.connect("Finaldatabase.db")
# Request a cursor from the database
cursor = conn.cursor()
cursor.execute('pragma foreign_keys=ON')
COUNT = 0

fd = open('C:\Gunjan DePaul\CSC 455\Finals\Tweet.txt', 'r', encoding='utf8')

#tweet = fd.readlines()
for i in range(500000):
        #COUNT = COUNT + 1;
        #print(COUNT)
        tweet = fd.readline()
        
        try:    
              jsonobject = json.loads(str(tweet))
                            
              if jsonobject['geo'] != None:
                   geovalues = (str(jsonobject['geo']['coordinates'][1]) + str(jsonobject['geo']['coordinates'][0]), jsonobject['geo']['type'], jsonobject['geo']['coordinates'][1], jsonobject['geo']['coordinates'][0])
                   cursor.execute("INSERT OR IGNORE INTO GEO VALUES(?,?,?,?);",geovalues)
              
              uservalues = (jsonobject['user']['id'], jsonobject['user']['name'], jsonobject['user']['screen_name'], jsonobject['user']['description'], jsonobject['user']['friends_count'])
              
              cursor.execute("INSERT OR IGNORE INTO USER VALUES(?,?,?,?,?);",uservalues)
              
              if 'retweeted_status' in jsonobject.keys():
                retweetcount = jsonobject['retweeted_status']['retweet_count']
              else:
                retweetcount = jsonobject['retweet_count']
              
              text = html.unescape(jsonobject['text'])
              
              if jsonobject['geo'] != None:
                tweetvalues = (jsonobject['created_at'], jsonobject['id_str'], text, jsonobject['source'],jsonobject['in_reply_to_user_id'], jsonobject['in_reply_to_screen_name'], jsonobject['in_reply_to_status_id'], retweetcount, jsonobject['contributors'], jsonobject['user']['id'], str(jsonobject['geo']['coordinates'][1]) + str(jsonobject['geo']['coordinates'][0])) 
              else:
                tweetvalues = (jsonobject['created_at'], jsonobject['id_str'], text, jsonobject['source'],jsonobject['in_reply_to_user_id'], jsonobject['in_reply_to_screen_name'], jsonobject['in_reply_to_status_id'], retweetcount, jsonobject['contributors'], jsonobject['user']['id'], None) 
        
              cursor.execute("INSERT OR IGNORE INTO TWEET VALUES(?,?,?,?,?,?,?,?,?,?,?);",tweetvalues)
                                      
        except ValueError:
              None

end = time.time()
print ("Difference is ", (end-start), "seconds")      #940 seconds -> 15.66 minutes

conn.commit()

print ("Loaded ", cursor.execute('SELECT COUNT(*) FROM GEO').fetchall()[0], " rows into GEO table")
print ("Loaded ", cursor.execute('SELECT COUNT(*) FROM USER').fetchall()[0], " rows into USER table")
print ("Loaded ", cursor.execute('SELECT COUNT(*) FROM TWEET').fetchall()[0], " rows into TWEET table")
    
conn.close()


#Geo: 11849
#User: 447304
#Tweet: 499776