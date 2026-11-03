 CREATE OR REPLACE TEMP VIEW orders AS
 SELECT * FROM VALUES
    (101, 1, '2026-10-01', 2000),
    (102, 1, '2026-10-05', 3500),
    (103, 2, '2026-10-02', 1500),
     (104, 2, '2026-10-07', 4000),
     (105, 3, '2026-10-03', 2500)
 AS orders(OrderId, CustomerId, OrderDate, Amount);

 select 
 OrderId,CustomerId,Orderdate,amount 
 from (
     select *, row_number()
     over(partition by CustomerID order by OrderDate desc ,OrderId desc) as rn from orders
 )
 where rn =1;
