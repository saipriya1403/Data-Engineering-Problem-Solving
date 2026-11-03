CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
 (101, 'Arun', 201),
 (102, 'Priya', NULL),
(103, 'Rahul', 202),
 (104, 'Sneha', NULL),
(105, 'Kiran', 201)
AS employees(emp_id, emp_name, manager_id);
SELECT *
 FROM employees
 WHERE manager_id IS NULL;
