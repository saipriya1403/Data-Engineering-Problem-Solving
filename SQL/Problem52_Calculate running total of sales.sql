%sql
CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
    (101, DATE'2026-01-01', 1000),
    (102, DATE'2026-01-02', 1500),
    (103, DATE'2026-01-03', 2000),
    (104, DATE'2026-01-04', 500),
    (105, DATE'2026-01-05', 1000)
AS orders(order_id, order_date, amount);


SELECT
    order_id,
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING
        AND CURRENT ROW
    ) AS running_total
FROM orders;
