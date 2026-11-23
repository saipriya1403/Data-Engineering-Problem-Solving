%sql
CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
    (1, 'Arun', 5000),
    (2, 'Priya', NULL),
    (3, 'Kumar', 3000),
    (4, 'Divya', NULL)
AS employees(emp_id, emp_name, bonus);


SELECT
    emp_id,
    emp_name,
    COALESCE(bonus, 0) AS bonus
FROM employees;
