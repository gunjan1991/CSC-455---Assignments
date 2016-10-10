# Assignment: 5
# Name: Gunjan Pravinchandra Pandya
# Part: 2(b)

import sqlite3
from csv import reader

cityTable = '''CREATE TABLE CITY
( CHAUFFERCITY VARCHAR2(20) NOT NULL,
  CHAUFFERSTATE VARCHAR2(20),
  CONSTRAINT CHAUCITY_PK PRIMARY KEY(CHAUFFERCITY)
);'''

driverTable = '''CREATE TABLE DRIVER
( LICENSENUMBER INTEGER,
  RENEWED VARCHAR2(20),
  STATUS VARCHAR2(20),
  STATUSDATE DATE,
  DRIVERTYPE VARCHAR2(20),
  LICENSETYPE VARCHAR2(20),
  ORIGINALISSUEDATE DATE,
  NAME VARCHAR2(30),
  SEX VARCHAR2(10),
  CHAUFFERCITY VARCHAR2(30),
  RECORDNUMBER VARCHAR2(20) NOT NULL,
  CONSTRAINT RECNUM_PK PRIMARY KEY(RECORDNUMBER),
  CONSTRAINT CHAUCITY_FK FOREIGN KEY(CHAUFFERCITY) REFERENCES CITY(CHAUFFERCITY)
);'''

# Open a connection to database
conn = sqlite3.connect("ChaufferDatabase.db")

# Request a cursor from the database
cursor = conn.cursor()

# Get rid of the tables if we already created it
cursor.execute("DROP TABLE IF EXISTS CITY")
cursor.execute("DROP TABLE IF EXISTS DRIVER")
# Create the table in ChaufferDatabase.db
cursor.execute(cityTable)
cursor.execute(driverTable)
# Open file for reading
fd = open('C:\Gunjan DePaul\CSC 455\Segment 5\Public_Chauffeurs_Short_hw5.csv', 'r')
# Read all lines from the file into allLines variable
allLines = fd.readlines()
allLines.pop(0)    # Remove column headings
fd.close()         # Close the file

# For each line in the file
for line in reader(allLines): #This will read CSV file as is according to columns
    #print (line)            #To check if we are getting records of CSV in list form
    comma = set(',')
    if comma & set(line[7]):       #To check if Name column contains ',' 
            valueList = line[7].strip().split(',')
            line[7] = valueList[1] + ' ' + valueList[0]
            #print(list[7])
    newList = [line[9],line[10]]   # Another newList for CITY Table
    line.pop(10)                      # Removing State from valueList for table DRIVER

    cursor.execute("INSERT OR IGNORE INTO CITY VALUES (?,?);", newList)
    cursor.execute("INSERT INTO DRIVER VALUES (?,?,?,?,?,?,?,?,?,?,?);", line)

# To check what we inserted into the table
allSelectedRowsCity = cursor.execute("SELECT * FROM CITY;").fetchall()
allSelectedRowsDriver = cursor.execute("SELECT * FROM DRIVER;").fetchall()

# For every row, print the results of the query above, separated by a tab
for eachRow in allSelectedRowsCity:
    for value in eachRow:
        print (value, "\t",)
    print ("\n",) # \n is the end of line symbol
len(allSelectedRowsCity)

for eachRow in allSelectedRowsDriver:
    for value in eachRow:
        print (value, "\t",)
    print ("\n",) # \n is the end of line symbol
len(allSelectedRowsDriver)
# Finalize inserts and close the connection to the database
conn.commit()
conn.close()
#
#