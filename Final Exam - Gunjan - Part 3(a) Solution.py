# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 3(a)
"""
3 (a). Export the contents of the User table from a SQLite table into a sequence of INSERT statements within a 
file. This is very similar to what you did in Assignment 4. However, you have to add a unique ID column which 
has to be a string (you cannot use any numbers). Hint: one possibility is to replace digits with letters, e.g., 
chr(ord('a')+1) gives you a 'b' and chr(ord('a')+2) returns a 'c'

-> Runtime: 12.12 seconds
"""

import sqlite3
import time

start = time.time()
# Open a connection to database
conn = sqlite3.connect("Finaldatabase.db")
# Request a cursor from the database
cursor = conn.cursor()
cursor.execute('pragma foreign_keys=ON')

results = cursor.execute('SELECT * FROM USER;').fetchall()
output = open('C:\Gunjan DePaul\CSC 455\Finals\Insert.txt', 'w', encoding='utf8')
for rows in results:
        insert = 'INSERT INTO USER VALUES ('
        for attr in rows:
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
        ID = str(rows[0])
        uniqueSID = ''

        for j in range( len( ID ) ):
            uniqueSID = uniqueSID + chr(ord('a')+int(ID[j]))
            value = "'" + uniqueSID +"'"
        insert = insert + value + ', '
        insert = insert[:-2] + '); \n'
        #print(insert)        
        output.write(insert)
output.close()

end = time.time()
print ("Difference is ", (end-start), "seconds")   #12.12 seconds

conn.commit()
conn.close()







