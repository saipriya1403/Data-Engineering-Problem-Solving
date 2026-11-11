%sql
CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
    (1, 'Priya', 30000),
    (2, 'Rahul', 50000),
    (3, 'Anjali', 40000),
    (4, 'Kumar', 60000),
    (5, 'Divya', 20000)
AS employees(emp_id, emp_name, salary);


SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
