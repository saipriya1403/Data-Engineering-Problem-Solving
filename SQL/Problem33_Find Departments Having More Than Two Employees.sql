%sql
CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
(101, 'Arun', 'IT'),
(102, 'Priya', 'HR'),
(103, 'Rahul', 'IT'),
(104, 'Sneha', 'IT'),
(105, 'Kiran', 'HR'),
(106, 'Meena', 'Finance')
AS employees(emp_id, emp_name, department);

%sql
SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;
