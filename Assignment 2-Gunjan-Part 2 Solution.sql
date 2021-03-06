/*Assignment No.: 2
  Name: Gunjan Pravinchandra Pandya
  Part: 2*/

DROP TABLE AUTHORS;
DROP TABLE PUBLISHERS;
DROP TABLE BOOKS;
DROP TABLE WRITE;

/*Creating Tables*/
CREATE TABLE AUTHORS
( LASTNAME VARCHAR2(32) NOT NULL,
  FIRSTNAME VARCHAR2(32)NOT NULL,
  AUTHID NUMBER(2) NOT NULL,
  BIRTHDATE DATE NOT NULL,
  CONSTRAINT AUTHIDPK PRIMARY KEY(AUTHID)
);

CREATE TABLE PUBLISHERS
( NAME VARCHAR2(32) NOT NULL,
  PUBID NUMBER(2) NOT NULL,
  ADDRESS VARCHAR(40) NOT NULL,
  CONSTRAINT PUBIDPK PRIMARY KEY(PUBID)
);

CREATE TABLE BOOKS
( ISBN CHAR(8) NOT NULL,
  TITLE VARCHAR2(40) NOT NULL,
  PUBLISHER NUMBER(2) NOT NULL,
  CONSTRAINT ISBNPK PRIMARY KEY(ISBN),
  CONSTRAINT PUBIDFK FOREIGN KEY(PUBLISHER) REFERENCES PUBLISHERS(PUBID)
);

CREATE TABLE WRITE
( AUTHID NUMBER(2) NOT NULL,
  ISBN CHAR(8) NOT NULL,
  RANK INTEGER NOT NULL,
  CONSTRAINT AUTHID_ISBN_PK PRIMARY KEY(AUTHID,ISBN),
  CONSTRAINT AUTHIDFK FOREIGN KEY(AUTHID) REFERENCES AUTHORS(AUTHID),
  CONSTRAINT ISBNFK FOREIGN KEY(ISBN) REFERENCES BOOKS(ISBN)
);

/*Inserting Data Into Tables*/
INSERT INTO AUTHORS VALUES ('King','Stephan',2,TO_DATE('September 9 1947','MM DD YYYY'));
INSERT INTO AUTHORS VALUES ('Asimov','Isaac',4,TO_DATE('January 2 1920','MM DD YYYY'));
INSERT INTO AUTHORS VALUES ('Verne','Jules',7,TO_DATE('February 8 1828','MM DD YYYY'));
INSERT INTO AUTHORS VALUES ('Rowling','Joanne',37,TO_DATE('July 31 1965','MM DD YYYY'));

INSERT INTO PUBLISHERS VALUES ('Bloomsbury Publishing',17,'London Borough of Camden');
INSERT INTO PUBLISHERS VALUES ('Arthur A. Levine Books',18,'New York City');

INSERT INTO BOOKS VALUES ('1111-111','Databases from outer space',17);
INSERT INTO BOOKS VALUES ('2222-222','Dark SQL',17);
INSERT INTO BOOKS VALUES ('3333-333','The night of the living databases',18);

INSERT INTO WRITE VALUES (2,'1111-111',1);
INSERT INTO WRITE VALUES (4,'1111-111',2);
INSERT INTO WRITE VALUES (4,'2222-222',2);
INSERT INTO WRITE VALUES (7,'2222-222',1);
INSERT INTO WRITE VALUES (37,'3333-333',1);
INSERT INTO WRITE VALUES (2,'3333-333',2);

COMMIT;