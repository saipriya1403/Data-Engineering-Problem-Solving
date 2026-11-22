%sql
CREATE OR REPLACE TEMP VIEW departments AS
SELECT * FROM VALUES
    (1, 'IT'),
    (2, 'HR'),
    (3, 'Finance'),
    (4, 'Sales')
AS departments(dept_id, dept_name);

CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
    (101, 'Priya', 1),
    (102, 'Rahul', 2),
    (103, 'Anjali', 1)
AS employees(emp_id, emp_name, dept_id);


SELECT
    d.dept_id,
    d.dept_name
FROM departments d
LEFT JOIN employees e
    ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;
