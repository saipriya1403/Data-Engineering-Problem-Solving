 CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
     (1, 'Arun', 'IT'),
   (2, 'Priya', 'Data'),
    (3, 'Kumar', 'IT'),
   (4, 'Divya', 'HR'),
     (5, 'Meena', 'Data'),
    (6, 'Ravi', 'IT')
AS employees(EmployeeId, EmployeeName, Department);

 SELECT
 Department,
 COUNT(*) AS TotalEmployees
 FROM employees
 GROUP BY Department;
