# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 2(b)
"""
2(b). Write python code that is going to read the locally saved tweet data file from 1-b and perform the 
equivalent computation for parts 2-i and 2-ii only. How does the runtime compare to the SQL queries?

-> Runtime for performing the equivalent computation for parts 2-i and 2-ii is more than the SQL queries.
2-i SQL query took 1.09 seconds while program took 50 seconds
2-ii SQL queruy took 1.71 seconds while program took 180 seconds
"""
import json
import time

#2(b) Python equivalent computation for 2(a). i. Find tweets where tweet id_str contains “44” or “77” anywhere in the column
start = time.time()
error = 0
queryOutput = []
fd = open('C:\Gunjan DePaul\CSC 455\Finals\Tweet.txt', 'r', encoding='utf8')

for i in range(500000):
        
        tweet = fd.readline()
       
        try:    
            jsonobject = json.loads(str(tweet))
            id_str = jsonobject['id_str']
            if '44' in id_str or '77' in id_str:
                if 'retweeted_status' in jsonobject.keys():
                    retweetcount = jsonobject['retweeted_status']['retweet_count']
                else:
                    retweetcount = jsonobject['retweet_count']
                
                if jsonobject['geo'] != None:     
                    tweetvalues = (jsonobject['created_at'], jsonobject['id_str'], jsonobject['text'], jsonobject['source'],jsonobject['in_reply_to_user_id'], jsonobject['in_reply_to_screen_name'], jsonobject['in_reply_to_status_id'], retweetcount, jsonobject['contributors'], jsonobject['user']['id'], str(jsonobject['geo']['coordinates'][1]) + str(jsonobject['geo']['coordinates'][0])) 
                else:
            
                    tweetvalues = (jsonobject['created_at'], jsonobject['id_str'], jsonobject['text'], jsonobject['source'],jsonobject['in_reply_to_user_id'], jsonobject['in_reply_to_screen_name'], jsonobject['in_reply_to_status_id'], retweetcount, jsonobject['contributors'], jsonobject['user']['id'], None)
                queryOutput.append(tweetvalues)  
                #print(queryOutput)
                #len(queryOutput)
        except ValueError:
      
            None

        except Exception:
            error = error +1
            
end = time.time()
print ("Difference is ", (end-start), "seconds") # 50 seconds


#2(b) Python equivalent computation for 2(a). ii.Find how many unique values are there in the “in_reply_to_user_id” column
start = time.time()
COUNT = 0
error = 0
queryOutput = []
fd = open('C:\Gunjan DePaul\CSC 455\Finals\Tweet.txt', 'r', encoding='utf8')
#tweet = fd.readlines()
for i in range(500000):
        #COUNT = COUNT + 1;
        #print(COUNT)
        tweet = fd.readline()
        #print(tweet)
#for line in tweet: 
  #      print(line)       
        try:    
            jsonobject = json.loads(str(tweet))
            in_reply_to_user_id = jsonobject['in_reply_to_user_id']
            if in_reply_to_user_id != None:
                if in_reply_to_user_id in queryOutput:
                    None
                else:
                    queryOutput.append(in_reply_to_user_id)
            
        except ValueError:
            None

len(queryOutput)
end = time.time()
print ("Difference is ", (end-start), "seconds")  # 180 seconds
print("No of unique values in 'in_reply_to_user_id' column are: ", len(queryOutput))

