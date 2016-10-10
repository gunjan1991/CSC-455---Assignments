# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 2(a)
"""
2(a). Write and execute SQL queries to do the following. Don’t forget to report the running times in each part – 
you do not need to report the output:
"""
import sqlite3
import time

# Open a connection to database
conn = sqlite3.connect("Finaldatabase.db")
# Request a cursor from the database
cursor = conn.cursor()

"""
i. Find tweets where tweet id_str contains “44” or “77” anywhere in the column
-> Runtime: 1.09 seconds
"""
start = time.time()
query1 = cursor.execute("select * from tweet where id_str like '%44%' or id_str like '%77%';").fetchall()
len(query1)
end = time.time()
print ("Difference is ", (end-start), "seconds")  #1.78 seconds

"""
ii. Find how many unique values are there in the “in_reply_to_user_id” column
-> Runtime: 1.71 seconds
"""
start = time.time()
query1 = cursor.execute("select count(distinct in_reply_to_user_id) from tweet;").fetchall()
end = time.time()
print ("Difference is ", (end-start), "seconds")   #1.24 seconds

"""
iii.	Find the tweet(s) with the longest text message
-> Runtime: 1.93 seconds
"""
start = time.time()
query1 = cursor.execute("select * from tweet where length(text) = (select max(length(text)) from tweet);").fetchall()
end = time.time()
print ("Difference is ", (end-start), "seconds") #1.93 seconds

"""
iv. Find the average longitude and latitude value for each user name.
-> 6.38 seconds
"""
start = time.time()
query1 = cursor.execute("select name,avg(longitude), avg(latitude) from user u, tweet t, geo g where u.id = t.user_id and g.geo_id = t.geo_id group by name;").fetchall()
#len(query1)
end = time.time()
print ("Difference is ", (end-start), "seconds") #5.69 seconds

"""
v. Re-execute the query in part iv) 10 times and 100 times and measure the total runtime (just re-run the same 
exact query using a for-loop). Does the runtime scale linearly? (i.e., does it take 10X and 100X as much time?)

-> For 10 times it took 54.53 seconds which almost scaled linearly as it is almost equal to (10*5.69), 2-3 seconds less
-> For 100 times it took 568 seconds which almost scaled linearly as (100 * 5.69)
"""
start = time.time()
for i in range (10):
    #print(i)
    query1 = cursor.execute("select name,avg(longitude), avg(latitude) from user u, tweet t, geo g where u.id = t.user_id and g.geo_id = t.geo_id group by name;").fetchall()
end = time.time()
print ("Difference is ", (end-start), "seconds")   #54.53 seconds

start = time.time()
for i in range (100):
    #print(i)
    query1 = cursor.execute("select name,avg(longitude), avg(latitude) from user u, tweet t, geo g where u.id = t.user_id and g.geo_id = t.geo_id group by name;").fetchall()
end = time.time()
print ("Difference is ", (end-start), "seconds")   #568 seconds
