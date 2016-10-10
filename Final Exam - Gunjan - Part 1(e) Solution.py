# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 1(e)

"""
1(e). Re-run the previous step with batching size of 500 (i.e. by inserting 500 rows at a time with executemany).
You can adapt the posted example code. How does the runtime compare when batching is used?

-> Runtime: 1.38 minutes
-> When we used batching, the runtime was quite small and data loading process was very quick.
-> No of records: 
Geo: 11849
User: 447304
Tweet: 499776
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

batchRows = 500
batchedInsertsGeo = []
batchedInsertsUser = []
batchedInsertsTweet = []
#tweet = fd.readlines()
for i in range(500000):
        #COUNT = COUNT + 1;
        #print(COUNT)
        tweet = fd.readline()
        
        try:    
              jsonobject = json.loads(str(tweet))
                            
              if jsonobject['geo'] != None:
                   geovalues = (str(jsonobject['geo']['coordinates'][1]) + str(jsonobject['geo']['coordinates'][0]), jsonobject['geo']['type'], jsonobject['geo']['coordinates'][1], jsonobject['geo']['coordinates'][0])
                   batchedInsertsGeo.append(geovalues)
                   #cursor.execute("INSERT OR IGNORE INTO GEO VALUES(?,?,?,?);",geovalues)
              
              uservalues = (jsonobject['user']['id'], jsonobject['user']['name'], jsonobject['user']['screen_name'], jsonobject['user']['description'], jsonobject['user']['friends_count'])
              batchedInsertsUser.append(uservalues)
              #cursor.execute("INSERT OR IGNORE INTO USER VALUES(?,?,?,?,?);",uservalues)
              
              if 'retweeted_status' in jsonobject.keys():
                retweetcount = jsonobject['retweeted_status']['retweet_count']
              else:
                retweetcount = jsonobject['retweet_count']
              
              text = html.unescape(jsonobject['text'])

              if jsonobject['geo'] != None:
                tweetvalues = (jsonobject['created_at'], jsonobject['id_str'], text, jsonobject['source'],jsonobject['in_reply_to_user_id'], jsonobject['in_reply_to_screen_name'], jsonobject['in_reply_to_status_id'], retweetcount, jsonobject['contributors'], jsonobject['user']['id'], str(jsonobject['geo']['coordinates'][1]) + str(jsonobject['geo']['coordinates'][0])) 
              else:
                tweetvalues = (jsonobject['created_at'], jsonobject['id_str'], text, jsonobject['source'],jsonobject['in_reply_to_user_id'], jsonobject['in_reply_to_screen_name'], jsonobject['in_reply_to_status_id'], retweetcount, jsonobject['contributors'], jsonobject['user']['id'], None) 
              batchedInsertsTweet.append(tweetvalues)
              #cursor.execute("INSERT OR IGNORE INTO TWEET VALUES(?,?,?,?,?,?,?,?,?,?,?);",tweetvalues)
              
              if len(batchedInsertsTweet) >= batchRows: #or len(tweetLines) == 0:
                  cursor.executemany('INSERT OR IGNORE INTO GEO VALUES(?,?,?,?)', batchedInsertsGeo)
                  cursor.executemany('INSERT OR IGNORE INTO USER VALUES(?,?,?,?,?);', batchedInsertsUser)
                  cursor.executemany("INSERT OR IGNORE INTO TWEET VALUES(?,?,?,?,?,?,?,?,?,?,?);", batchedInsertsTweet)
                  batchedInsertsGeo = []
                  batchedInsertsUser = []
                  batchedInsertsTweet = []

                        
        except ValueError:
              None

cursor.executemany('INSERT OR IGNORE INTO GEO VALUES(?,?,?,?)', batchedInsertsGeo)
cursor.executemany('INSERT OR IGNORE INTO USER VALUES(?,?,?,?,?);', batchedInsertsUser)
cursor.executemany("INSERT OR IGNORE INTO TWEET VALUES(?,?,?,?,?,?,?,?,?,?,?);", batchedInsertsTweet)


end = time.time()
print ("Difference is ", (end-start), "seconds")      #130 seconds -> 2.16 minutes    
conn.commit()
conn.close()


#Geo: 11849
#User: 447304
#Tweet: 499776