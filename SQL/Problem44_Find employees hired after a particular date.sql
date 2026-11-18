%sql
CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
    (1, 'Priya', DATE'2024-05-10'),
    (2, 'Rahul', DATE'2025-03-15'),
    (3, 'Anjali', DATE'2025-06-20'),
    (4, 'Kumar', DATE'2024-12-10'),
    (5, 'Divya', DATE'2026-01-05')
AS employees(emp_id, emp_name, joining_date);

SELECT *
FROM employees
WHERE joining_date > DATE'2025-01-01';
