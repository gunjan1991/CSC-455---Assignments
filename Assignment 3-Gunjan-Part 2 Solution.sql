/*Assignment No.: 3
  Name: Gunjan Pravinchandra Pandya
  Part: 2*/

/*a.	For each Author in Assignment 2 – Part 2, retrieve the Author ID, Author First Name, Author Last Name and book ISBN of each book that 
author has written sorted in alphabetical order by the author’s last name.*/
SELECT AUTHORS.AUTHID,FIRSTNAME,LASTNAME,ISBN 
FROM AUTHORS,WRITE 
WHERE AUTHORS.AUTHID=WRITE.AUTHID 
ORDER BY LASTNAME;

/*b.	For each Publisher in Assignment 2 – Part 2, retrieve the Publisher Name, Publisher Address, Book Title and Book ISBN for each book that 
publisher has published in alphabetical order by book title and only for books with titles that begin with the letter “D”.*/
SELECT NAME,ADDRESS,TITLE,ISBN 
FROM PUBLISHERS,BOOKS 
WHERE PUBLISHERS.PUBID=BOOKS.PUBLISHER AND TITLE LIKE 'D%' 
ORDER BY TITLE;

/*c.	For each Office in Assignment 2 – Part 3, retrieve the Office, Floor, Building and the Building’s City for every instance in which the 
Building’s City starts with the letter “C”.*/
SELECT OFFICE,FLOOR,OFFICE.BUILDING,CITY 
FROM OFFICE,BUILDING 
WHERE OFFICE.BUILDING=BUILDING.BUILDING AND CITY LIKE 'C%';

/*d.	We need information on all meetings that took place after January 15, 2014. For each Office in Assignment 2 – Part 3, retrieve the 
Office, Floor, Building City, Client and Executive of all meetings that took place after 1/15/2014 in alphabetical order by executive name.*/
SELECT CLIENTMIX.OFFICE,FLOOR,CITY,CLIENT.CLIENT,EXECUTIVE 
FROM CLIENTMIX,OFFICE,BUILDING,CLIENT 
WHERE CLIENTMIX.OFFICE=OFFICE.OFFICE AND OFFICE.BUILDING=BUILDING.BUILDING AND CLIENT.CLIENT=CLIENTMIX.CLIENT AND MEETDATE>'15/JAN/2016' 
ORDER BY EXECUTIVE;