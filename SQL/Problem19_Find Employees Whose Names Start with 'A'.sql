 CREATE OR REPLACE TEMP VIEW employees AS
 SELECT * FROM VALUES
    (1, 'Arun', 'IT'),
(2, 'Priya', 'Data'),
     (3, 'Anu', 'HR'),
    (4, 'Kumar', 'IT'),
    (5, 'Ajay', 'Data'),
    (6, 'Divya', 'HR')
 AS employees(EmployeeId, EmployeeName, Department);

 SELECT
 EmployeeId,
 EmployeeName,
 Department
 FROM employees
 MAGIC WHERE EmployeeName LIKE 'A%';
