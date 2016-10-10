# Final Exam
# Name: Gunjan Pravinchandra Pandya
# Part: 1(a)
"""
1 (a). Create a 3rd table incorporating the Geo table (in addition to tweet and user tables that you already 
have) and extend your schema accordingly. You will need to generate an ID for the Geo table primary key (you may 
use any value or combination of values as long as it is unique) for that table and link it to the Tweet table 
(foreign key should be in the Tweet table because there can be multiple tweets sent from the same location). 
In addition to the primary key column, the geo table should have “type”, “longitude” and “latitude” columns.
"""


import sqlite3

geoTable = '''CREATE TABLE GEO
( GEO_ID VARCHAR2(50),
  TYPE VARCHAR2(10),
  LONGITUDE VARCHAR2(100),
  LATITUDE VARCHAR2(100),
  CONSTRAINT GEO_ID_PK PRIMARY KEY (GEO_ID)
  );'''

userTable = '''CREATE TABLE USER
( ID INTEGER,
  NAME VARCHAR2(50),
  SCREEN_NAME VARCHAR2(50),
  DESCRIPTION VARCHAR2(100),
  FRIENDS_COUNT INTEGER,
  CONSTRAINT ID_PK PRIMARY KEY (ID)
);'''

tweetTable = '''CREATE TABLE TWEET
( CREATED_AT VARCHAR2(35),
  ID_STR INTEGER,
  TEXT VARCHAR2(140),
  SOURCE VARCHAR2(100),
  IN_REPLY_TO_USER_ID VARCHAR2(50),
  IN_REPLY_TO_SCREEN_NAME VARCHAR2(50),
  IN_REPLY_TO_STATUS_ID VARCHAR2(50),
  RETWEET_COUNT INTEGER,
  CONTRIBUTORS VARCHAR2(100),
  USER_ID INTEGER,
  GEO_ID VARCHAR2(50),
  CONSTRAINT ID_STR_PK PRIMARY KEY (ID_STR),
  CONSTRAINT USERID_FK FOREIGN KEY (USER_ID) REFERENCES USER(ID)
  CONSTRAINT GEO_ID FOREIGN KEY (GEO_ID) REFERENCES GEO(GEO_ID)
);'''


# Open a connection to database
conn = sqlite3.connect("Finaldatabase.db")

# Request a cursor from the database
cursor = conn.cursor()
cursor.execute('pragma foreign_keys=ON')

# Get rid of the tables if we already created it
cursor.execute("DROP TABLE IF EXISTS TWEET")
cursor.execute("DROP TABLE IF EXISTS USER")
cursor.execute("DROP TABLE IF EXISTS GEO")
# Create the table in ChaufferDatabase.db
cursor.execute(geoTable)
cursor.execute(userTable)
cursor.execute(tweetTable)

conn.commit()
conn.close()