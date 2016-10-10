# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 3(b)
"""
3 (b). Create a similar collection of INSERT for the User table by reading/parsing data from the local tweet 
file that you have saved earlier. How do these compare in runtime? Which method was faster?

-> Runtime: 77.23 seconds

-> If we compare 3(a) and 3(b), 3(a) was faster as it took 12.12 seconds while 3(b) took 77.23 seconds
"""

import json
import sqlite3
import time

# Open a connection to database
conn = sqlite3.connect("Finaldatabase.db")
# Request a cursor from the database
cursor = conn.cursor()
cursor.execute('pragma foreign_keys=ON')

start = time.time()
fd = open('C:\Gunjan DePaul\CSC 455\Finals\Tweet.txt', 'r', encoding='utf8')

output = open('C:\Gunjan DePaul\CSC 455\Finals\InsertText.txt', 'w', encoding='utf8')
COUNT = 0
for i in range(500000):
        #COUNT = COUNT + 1;
        #print(COUNT)
        tweet = fd.readline()
        
        try:    
            jsonobject = json.loads(str(tweet))
        
            #if 'retweeted_status' in jsonobject.keys():
             #   retweetcount = jsonobject['retweeted_status']['retweet_count']
            #else:
             #   retweetcount = jsonobject['retweet_count']

            uservalues = (jsonobject['user']['id'], jsonobject['user']['name'], jsonobject['user']['screen_name'], jsonobject['user']['description'], jsonobject['user']['friends_count'])
            
            insert = 'INSERT INTO USER VALUES ('
            for attr in uservalues:
            # Convert None to NULL
                if attr == None: 
                    insert = insert + 'NULL' + ', '
                else:
                    if isinstance(attr, (int, float)):
                        value = str(attr)
                    else: 
                    # Escape all single quotes in the string
                        value = "'" + str(attr.replace("'", "''")) + "'"
                    
                    insert = insert + value + ', '
                #print(insert)
            ID = str(uservalues[0])
            uniqueSID = ''
            #newNum = int(newID)
            for j in range( len( ID ) ):
                uniqueSID = uniqueSID + chr(ord('a')+int(ID[j]))
                value = "'" + uniqueSID +"'"
            insert = insert + value + ', '
            insert = insert[:-2] + '); \n'
            #print(insert)        
            output.write(insert)
    
        except ValueError:
            None
 
output.close()
end = time.time()
print ("Difference is ", (end-start), "seconds")  #77.23 seconds
conn.commit()
conn.close()







