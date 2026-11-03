CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
 (101, 'Arun', 45000),
 (102, 'Priya', 60000),
(103, 'Rahul', 35000),
 (104, 'Sneha', 55000),
(105, 'Kiran', 40000)
 AS employees(emp_id, emp_name, salary);

 SELECT *
 FROM employees
 ORDER BY salary DESC;
