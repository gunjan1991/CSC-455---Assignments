# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 4(a)
"""
4 (a). For the Geo table, create a single default entry for the ‘Unknown’ location and round longitude and 
latitude to a maximum of 4 digits after the decimal.

-> Runtime: 1.36 seconds
"""

import sqlite3
import time

# Open a connection to database
conn = sqlite3.connect("Finaldatabase.db")
# Request a cursor from the database
cursor = conn.cursor()
cursor.execute('pragma foreign_keys=ON')

start = time.time()
allSelectedRowsGeo = cursor.execute("SELECT * FROM GEO;").fetchall()
    
text_file = open("C:\Gunjan DePaul\CSC 455\Finals\InsertPipeGeo.txt", "w",encoding='utf8')
count = 0

for i in range( len(allSelectedRowsGeo) ):

    lon = float(allSelectedRowsGeo[i][2])

    lat = float(allSelectedRowsGeo[i][3])
    
    #print("%s|" %(allSelectedRowsUser[i][0]) + "%s|" %(allSelectedRowsUser[i][1]) + "%s|" %(str(round(lon, 4))) + "%s \n" %(str(round(lat, 4))))

    text_file.write("'%s'|" %(allSelectedRowsGeo[i][0]) + "'%s'|" %(allSelectedRowsGeo[i][1]) + "'%s'|" %(str(round(lon, 4))) + "'%s' \n" %(str(round(lat, 4))))
    
text_file.write("'Unknown'|Null|'Unknown'|'Unknown'")

end = time.time()
print ("Difference is ", (end-start), "seconds") #1.36 seconds

conn.commit()
conn.close()