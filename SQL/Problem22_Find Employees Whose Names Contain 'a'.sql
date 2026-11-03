 CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
     (1, 'Arun', 'IT'),
    (2, 'Priya', 'Data'),
   (3, 'Kumar', 'IT'),
    (4, 'Divya', 'HR'),
    (5, 'Meena', 'Data'),
  (6, 'Rohit', 'HR')
 AS employees(EmployeeId, EmployeeName, Department);

 SELECT
EmployeeId,
 EmployeeName,
 Department
 FROM employees
 WHERE LOWER(EmployeeName) LIKE '%a%';
