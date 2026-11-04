%sql
CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
(101, 'Arun', 'IT', 45000),
(102, 'Priya', 'HR', 55000),
(103, 'Rahul', 'IT', 35000),
(104, 'Sneha', 'HR', 40000),
(105, 'Kiran', 'Finance', 60000)
AS employees(emp_id, emp_name, department, salary);

%sql
SELECT
    department,
    MIN(salary) AS minimum_salary
FROM employees
GROUP BY department;
