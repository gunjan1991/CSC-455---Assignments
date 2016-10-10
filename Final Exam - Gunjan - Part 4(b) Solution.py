# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 4(b)
"""
4 (b). For the Tweet table, replace NULLs by a reference to ‘Unknown’ entry (i.e., the foreign key column that 
references Geo table should refer to the “Unknown” entry you created in part-a. Report how many known/unknown 
locations there were in total (e.g., 10,000 known, 490,000 unknown,  2% locations are available)

-> Runtime: 71.61 seconds
-> 11,983 known locations, 4,87,793 unknown locations, 2.45% locations are available
"""
import sqlite3
import time

# Open a connection to database
conn = sqlite3.connect("Finaldatabase.db")
# Request a cursor from the database
cursor = conn.cursor()
cursor.execute('pragma foreign_keys=ON')
noLoc = 0
loc = 0
start = time.time()
results = cursor.execute('SELECT * FROM TWEET;').fetchall()
output = open("C:\Gunjan DePaul\CSC 455\Finals\InsertPipeTweet.txt", "w",encoding='utf8')
loc = 0
noLoc = 0
for rows in results:
        insert = ''        
        i=0
        #for attr in rows:
            # Convert None to NULL
        for i in range (10):
                #print(rows[i])
                if rows[i] == None: 
                    insert = insert + 'NULL' + '| '
                else:
                    if isinstance(rows[i], (int, float)):
                        value = str(rows[i])
                    else: 
                    # Escape all single quotes in the string
                        value = "'" + str(rows[i].replace("'", "''")) + "'"
                    #print(value)
                    insert = insert + value + '| '
                    #print(insert)
                i = i+1
                #print(insert)
        
        if rows[10] == None:
            value = 'Unknown'
            noLoc = noLoc + 1
        else:
            value = rows[10]
            loc = loc + 1
        insert = insert + "'" + value + "'" + '| '
        insert = insert[:-2] + '\n'
        #print(insert)        
        output.write(insert)

output.close()

print("Tweets with Unknown location are: ",noLoc)
print("Tweets with Known location are: ",loc)

end = time.time()
print ("Difference is ", (end-start), "seconds") #71.61 seconds

conn.close()