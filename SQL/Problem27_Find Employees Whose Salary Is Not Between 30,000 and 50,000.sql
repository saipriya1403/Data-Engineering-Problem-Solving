CREATE OR REPLACE TEMP VIEW employees AS
 SELECT * FROM VALUES
 (101, 'Arun', 25000),
 (102, 'Priya', 45000),
 (103, 'Rahul', 55000),
 (104, 'Sneha', 35000),
 (105, 'Kiran', 60000)
 AS employees(emp_id, emp_name, salary);

 SELECT *
 FROM employees
 WHERE salary NOT BETWEEN 30000 AND 50000;
