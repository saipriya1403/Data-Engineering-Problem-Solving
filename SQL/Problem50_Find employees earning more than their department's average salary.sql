%sql
CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
    (1, 'Arun', 'IT', 60000),
    (2, 'Priya', 'IT', 40000),
    (3, 'Kumar', 'HR', 50000),
    (4, 'Divya', 'HR', 30000),
    (5, 'Rahul', 'IT', 70000)
AS employees(emp_id, emp_name, department, salary);


SELECT
    emp_id,
    emp_name,
    department,
    salary
FROM (
    SELECT
        *,
        AVG(salary) OVER (
            PARTITION BY department
        ) AS dept_avg_salary
    FROM employees
) AS result
WHERE salary > dept_avg_salary;
