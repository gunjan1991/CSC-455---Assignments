/* Assignment: 5
   Name: Gunjan Pravinchandra Pandya
   Part: 1*/

/* 1. List the animals (animal names) and the ID of the zoo keeper assigned to them.*/
SELECT ANAME AS ANIMAL_NAME, ZOOKEEPID 
FROM ANIMAL A, HANDLES H 
WHERE A.AID = H.ANIMALID;

/*2. Now repeat the previous query and make sure that the animals without a handler also appear in the answer.*/
SELECT ANAME AS ANIMAL_NAME, ZOOKEEPID 
FROM ANIMAL A LEFT JOIN HANDLES H 
ON A.AID = H.ANIMALID;

/*3. Report, for every zoo keeper name, the total number of hours they spend feeding all animals in their care.*/
SELECT ZNAME AS ZOOKEEPER_NAME, SUM(TIMETOFEED) 
FROM ANIMAL A, HANDLES H, ZOOKEEPER Z 
WHERE Z.ZID = H.ZOOKEEPID AND H.ANIMALID = A.AID 
GROUP BY ZNAME;

/*4. Report every handling assignment (as a list of assignment date, zoo keeper name and animal name).  Sort the result of the query by the assignment date in 
an ascending order.*/
SELECT ASSIGNED, ZNAME, ANAME 
FROM ANIMAL A, HANDLES H, ZOOKEEPER Z 
WHERE Z.ZID = H.ZOOKEEPID AND H.ANIMALID = A.AID 
ORDER BY ASSIGNED;

/*5. Find the names of animals that have at least 1 zoo keeper assigned to them.*/
SELECT DISTINCT ANAME 
FROM ANIMAL A, HANDLES H 
WHERE A.AID = H.ANIMALID;

/*6. Find the names of animals that have 0 or 1 (i.e., less than 2) zoo keepers assigned to them.*/
SELECT ANAME AS ANIMAL_NAME 
FROM ANIMAL A LEFT JOIN HANDLES H 
ON A.AID = H.ANIMALID 
GROUP BY ANAME 
HAVING COUNT(ANAME) < 2;

--•	Optional query:
/*List all combination of animals where the difference between feeding time requirement is within 0.25 hours (e.g., Grizzly bear, 3, Bengal tiger, 2.75). 
Hint: this will require a self-join. Avoid listing identical pairs such as (Grizzly bear, 3, Grizzly bear, 3)
Using A1.TIMETOFEED - A2.TIMETOFEED BETWEEN -0.25 AND 0.25 condition so thatA1.AID < A2.AID does not restricts records*/
SELECT A1.ANAME, A1.TIMETOFEED, A2.ANAME, A2.TIMETOFEED 
FROM ANIMAL A1,ANIMAL A2 
WHERE A1.TIMETOFEED - A2.TIMETOFEED BETWEEN -0.25 AND 0.25 AND A1.ANAME != A2.ANAME AND A1.AID < A2.AID;