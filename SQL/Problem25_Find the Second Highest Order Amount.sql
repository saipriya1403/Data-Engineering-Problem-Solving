%sql
CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
(101, 'Arun', 5000),
(102, 'Priya', 8000),
(103, 'Rahul', 3000),
(104, 'Sneha', 8000),
(105, 'Kiran', 6000)
AS orders(order_id, customer_name, amount);

%sql
SELECT MAX(amount) AS second_highest_amount
FROM orders
WHERE amount < (
    SELECT MAX(amount)
    FROM orders
);
