%sql
CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
    (1, 'Arun', 'IT', 60000),
    (2, 'Priya', 'IT', 80000),
    (3, 'Rahul', 'IT', 70000),
    (4, 'Divya', 'HR', 50000),
    (5, 'Kumar', 'HR', 65000),
    (6, 'Meena', 'HR', 45000)
AS employees(emp_id, emp_name, department, salary);

SELECT
    emp_id,
    emp_name,
    department,
    salary
FROM (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS rank_num
    FROM employees
) AS ranked
WHERE rank_num <= 2;
