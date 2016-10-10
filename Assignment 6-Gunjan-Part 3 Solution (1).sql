/* Assignment No: 6
   Name: Gunjan Pravinchandra Pandya
   Part: 3*/

--a.	Count the number of iPhone users (based on “source” attribute)
SELECT COUNT(*)AS NUMBER_OF_iPhone_USERS 
FROM TWEET T 
WHERE T.SOURCE LIKE '%iPhone%';

--b.	Create a view that contains only tweets from users who are not replying ("in_reply_to_user_id" is NULL)
CREATE VIEW TWEET_VIEW (CREATED_AT, ID_STR, TEXT, SOURCE, IN_REPLY_TO_USER_ID, IN_REPLY_TO_SCREEN_NAME, RETWEET_COUNT, CONTRIBUTORS) AS 
SELECT *
FROM TWEET T 
WHERE T.IN_REPLY_TO_USER_ID IS NULL;

--c.	Select tweets that have a "retweet_count" higher than the average "retweet_count" from the tweets in the view in part b
SELECT * FROM TWEET_VIEW TV WHERE TV.RETWEET_COUNT > (SELECT AVG(TV.RETWEET_COUNT) FROM TWEET_VIEW TV);

--d.	Create a view that contains only “id_str”, “text” and “source” from each tweet that has a “retweet_count” of at least 5
CREATE VIEW TWEET_VIEW2 (ID_STR, TEXT, SOURCE) AS
SELECT ID_STR, TEXT, SOURCE
FROM TWEET T 
WHERE T.RETWEET_COUNT >= 5;

--e.	Use the view from part-d to find how many tweets have a “retweet_count” of at least 5
SELECT COUNT(*) FROM TWEET_VIEW2;

/*f.	Write python code to compute the answer from 3-e without using SQL, i.e., write code that is going to read data from the input file and answer the same 
question (find how many tweets have a “retweet_count” of at least 5).*/
--Solution: Assignment 6-Gunjan-Part 3(f) Solution

/*CREATE TABLE TWEET
( CREATED_AT VARCHAR2(35),
  ID_STR VARCHAR2(20),
  TEXT VARCHAR2(100),
  SOURCE VARCHAR2(500),
  IN_REPLY_TO_USER_ID VARCHAR2(30),
  IN_REPLY_TO_SCREEN_NAME VARCHAR2(20),
  RETWEET_COUNT INTEGER,
  CONTRIBUTORS VARCHAR2(10),
  CONSTRAINT ID_STR_PK PRIMARY KEY (ID_STR)
);*/

