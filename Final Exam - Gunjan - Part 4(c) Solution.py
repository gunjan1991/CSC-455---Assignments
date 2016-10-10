# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 4(c)
"""
4 (c). For the User table file add a column (true/false) that specifies whether “screen_name” or “description” 
attribute contains within it the “name” attribute of the same user. That is, your output file should contain all 
of the columns from the User table, plus the new column. You do not have to modify the original User table.

-> Runtime: 7.48 seconds
"""

import sqlite3
import time

# Open a connection to database
conn = sqlite3.connect("Finaldatabase.db")
# Request a cursor from the database
cursor = conn.cursor()
cursor.execute('pragma foreign_keys=ON')

start = time.time()
results = cursor.execute('SELECT * FROM USER;').fetchall()
output = open("C:\Gunjan DePaul\CSC 455\Finals\InsertPipeUser.txt", "w",encoding='utf8')

for rows in results:
        insert = ''        
        i=0
        #for attr in rows:
            # Convert None to NULL
        for i in range (4):
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
        if rows[3] != None:
            if rows[1] in rows[2] or rows[1] in rows[3]:
                value = 'True'
            else:
                value = 'False'
        else:
            value = 'False'
        insert = insert + "'" + value + "'" + '| '
        insert = insert[:-2] + '\n'
        #print(insert)        
        output.write(insert)

output.close()
end = time.time()
print ("Difference is ", (end-start), "seconds") #7.48 seconds

conn.close()