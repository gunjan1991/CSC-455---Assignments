# Assignment: 5
# Name: Gunjan Pravinchandra Pandya
# Part: 2(a)

import sqlite3
from sqlite3 import OperationalError

conn = sqlite3.connect('csc455_HW5.db')
c = conn.cursor()

# Open and read the file as a single buffer
fd = open('C:\Gunjan DePaul\CSC 455\Segment 5\ZooDatabase.sql', 'r') #File to create tables and insert data
# Read as a single document (not individual lines)
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';' which separates them)
sqlCommands = sqlFile.split(';')

# Execute every command from the input file (separated by ";")
for command in sqlCommands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    try:
        c.execute(command)
        print ("executed command: "+command)
    except OperationalError:
        print ("Command skipped: "+ command)

conn.commit()

# Open and read the file as a single buffer
fd = open('C:\Gunjan DePaul\CSC 455\Segment 5\Assignment 5-Gunjan-Part 1 Solution.sql', 'r') #Queries of Part-1 of HW-5

sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';' which separates them)
sqlCommands = sqlFile.split(';')

# Execute every command from the input file (separated by ";")
for command in sqlCommands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    try:
        c.execute(command)
        print ("executed command: "+command)
    except OperationalError:
        print ("Command skipped: "+ command)
        
    outputData = c.fetchall()      #To fetch output of the queries
    
    for eachRow in outputData:
        print(eachRow)             #To print each row
        print ("\n",) #\n is the end of line symbol
#allSelectedRowsCity = cursor.execute("SELECT * FROM CITY;").fetchall()
#allSelectedRowsDriver = cursor.execute("SELECT * FROM DRIVER;").fetchall()

# For every row, print the results of the query above, separated by a tab
c.close()
conn.commit()
conn.close()