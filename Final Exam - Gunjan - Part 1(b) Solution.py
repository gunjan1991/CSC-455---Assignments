# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 1(b)
"""
1 (b).	Use python to download from the web and save to a local text file (not into database yet) at least 500,000 
lines worth of tweets. Test your code with fewer rows first – you can reduce the number of tweets if your computer 
is running too slow to handle 500K tweets in a reasonable time. How long did it take to save?
NOTE: Do NOT call read() or readlines() without any parameters. That command will attempt to read the entire file 
and you only need 500K rows.

-> Runtime: 1201.77 seconds -> 20.02 minutes
-> Filesize: 1.54 GB
"""

import urllib.request as urllib

import time

start = time.time()

webFD=urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt")

output = open("C:\Gunjan DePaul\CSC 455\Finals\Tweet.txt", "wb")

for i in range(500000):
    
        tweet = webFD.readline()        
        
        output.write(tweet)        

end = time.time()
print ("Difference is ", (end-start), "seconds")   #1201.771 seconds -> 20.02 minutes
output.close()            
