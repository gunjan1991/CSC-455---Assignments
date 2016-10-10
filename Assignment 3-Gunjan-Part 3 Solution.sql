/*Assignment No.: 3
  Name: Gunjan Pravinchandra Pandya
  Part: 3*/

/*a.	Levels of inventory moved by each store. For each store identifier, retrieve store identifier and number of products sold in that store 
and arrange the results by number of products sold from low to high.*/
SELECT S.STOREID Store_Identifier,SUM(NOOFITEMS) AS Number_of_products_sold 
FROM STORE S,SALESTRANSACTION,SOLDVIA 
WHERE S.STOREID=SALESTRANSACTION.STOREID AND SALESTRANSACTION.TID=SOLDVIA.TID 
GROUP BY S.STOREID 
ORDER BY SUM(NOOFITEMS);

/*b. Analyzing sales in a particular region. For each line item of a sales transaction that took place in the "Chicagoland" region, retrieve 
the transaction identifier, date of the transaction, customer name, customer zip, store identifier and store zip.*/
SELECT ST.TID AS TRANSACTION_IDENTIFIER,ST.TDATE AS TRANSACTION_DATE,CUSTOMERNAME,CUSTOMERZIP,ST.STOREID AS STORE_IDENTIFIER,S.STOREZIP
FROM SALESTRANSACTION ST,CUSTOMER C,STORE S,REGION R 
WHERE ST.CUSTOMERID=C.CUSTOMERID AND ST.STOREID=S.STOREID AND S.REGIONID=R.REGIONID AND R.REGIONNAME='Chicagoland';

/*c.	Finding the high end product shoppers - Find the customer Name of any customer that has bought a product worth $150 or more.*/
SELECT DISTINCT CUSTOMERNAME 
FROM SOLDVIA SV,SALESTRANSACTION ST,PRODUCT P,CUSTOMER C 
WHERE SV.PRODUCTID=P.PRODUCTID AND SV.TID=ST.TID AND ST.CUSTOMERID=C.CUSTOMERID AND PRODUCTPRICE>=150;

/*d.	Finding the performance of product categories - For each product category, retrieve the category name and the total amount of dollars for all products 
sold in that category and arrange the results highest total to lowest sum.*/
SELECT CATEGORYNAME,SUM(NOOFITEMS*PRODUCTPRICE) AS TOTAL_AMOUNT 
FROM SOLDVIA SV,PRODUCT P,CATEGORY C 
WHERE SV.PRODUCTID=P.PRODUCTID AND P.CATEGORYID=C.CATEGORYID
GROUP BY CATEGORYNAME 
ORDER BY TOTAL_AMOUNT DESC;