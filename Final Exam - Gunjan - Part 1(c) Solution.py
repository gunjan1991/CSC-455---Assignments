# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 1(c)
"""
1 (c).Repeat what you did in part-b, but instead of saving tweets to the file, populate the 3-table schema that 
you created in SQLite. Be sure to execute commit and verify that the data has been successfully loaded (report 
row counts for each of the 3 tables).
If you use the posted example code be sure to turn off batching for this part. (i.e., batchRows set to 1). How 
long did this step take?

-> Runtime: 21.80 minutes
-> No of records: 
Geo: 11849
User: 447304
Tweet: 499776
"""

import urllib.request as urllib
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
webFD=urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt")

for i in range(500000):
        
        tweet = webFD.readline().decode("utf8")
        #COUNT = COUNT + 1
        #print(COUNT)
        try:    
              jsonobject = json.loads(tweet)
                       
              if jsonobject['geo'] != None:
                   geovalues = (str(jsonobject['geo']['coordinates'][1]) + str(jsonobject['geo']['coordinates'][0]), jsonobject['geo']['type'], jsonobject['geo']['coordinates'][1], jsonobject['geo']['coordinates'][0])
                   #print(geovalues)
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
print ("Difference is ", (end-start), "seconds")              #21.80 minutes    

conn.commit()

print ("Loaded ", cursor.execute('SELECT COUNT(*) FROM GEO').fetchall()[0], " rows into GEO table")
print ("Loaded ", cursor.execute('SELECT COUNT(*) FROM USER').fetchall()[0], " rows into USER table")
print ("Loaded ", cursor.execute('SELECT COUNT(*) FROM TWEET').fetchall()[0], " rows into TWEET table")

webFD.close()            
conn.close()