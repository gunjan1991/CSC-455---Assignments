# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 2(c) - Extra Credit
"""
2(c). Extra-credit: Perform the python equivalent for 2-iii

->Runtime: 45.04 seconds
-> For SQL Query it was 1.96 seconds while this approach took 45.04 seconds.
"""
import json
import time

start = time.time()
COUNT = 0
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
            
            if len(jsonobject['text']) == 140:
                if 'retweeted_status' in jsonobject.keys():
                    retweetcount = jsonobject['retweeted_status']['retweet_count']
                else:
                    retweetcount = jsonobject['retweet_count']
                
                if jsonobject['geo'] != None:     
                    tweetvalues = (jsonobject['created_at'], jsonobject['id_str'], jsonobject['text'], jsonobject['source'],jsonobject['in_reply_to_user_id'], jsonobject['in_reply_to_screen_name'], jsonobject['in_reply_to_status_id'], retweetcount, jsonobject['contributors'], jsonobject['user']['id'], str(jsonobject['geo']['coordinates'][1]) + str(jsonobject['geo']['coordinates'][0])) 
                else:
            
                    tweetvalues = (jsonobject['created_at'], jsonobject['id_str'], jsonobject['text'], jsonobject['source'],jsonobject['in_reply_to_user_id'], jsonobject['in_reply_to_screen_name'], jsonobject['in_reply_to_status_id'], retweetcount, jsonobject['contributors'], jsonobject['user']['id'], None)
                queryOutput.append(tweetvalues)
        
        except ValueError:
            None

end = time.time()
print ("Difference is ", (end-start), "seconds") #45 seconds