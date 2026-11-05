%sql
CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
(101, 'Arun', 'IT', 40000),
(102, 'Priya', 'HR', 50000),
(103, 'Rahul', 'IT', 60000),
(104, 'Sneha', 'HR', 45000),
(105, 'Kiran', 'Finance', 55000)
AS employees(emp_id, emp_name, department, salary);

%sql
SELECT
    department,
    SUM(salary) AS total_salary
FROM employees
GROUP BY department;
