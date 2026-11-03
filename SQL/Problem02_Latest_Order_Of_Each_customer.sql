% Latest Order for Each Customer

CREATE OR REPLACE TEMP VIEW orders AS SELECT * FROM VALUES
   (1001, 1, '2026-09-01', 5000),
   (1002, 2, '2026-09-02', 3000),    
  (1003, 1, '2026-09-05', 4000),
    (1004, 3, '2026-09-03', 7000),
   (1005, 2, '2026-09-06', 2000),    (1006, 1, '2026-09-08', 600 )
AS orders(OrderId, CustomerId, OrderDate, Amount);

 SELECT
    OrderId,
    CustomerId
    OrderDate,     Amount
 FROM (
     SELECT *,
    ROW_NUMBER() OVER (
    PARTITION BY CustomerId                              
    ORDER BY OrderDate DESC                                            
    )AS row_num 
   From Orders
 ) where row_num =1                                                     
