%sql
CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
    (1, 'Priya', 60000),
    (2, 'Rahul', 35000),
    (3, 'Anjali', 50000),
    (4, 'Kumar', 25000)
AS employees(emp_id, emp_name, salary);

%sql
SELECT
    emp_id,
    emp_name,
    salary,
    CASE
        WHEN salary >= 50000 THEN 'High'
        ELSE 'Low'
    END AS salary_category
FROM employees;
