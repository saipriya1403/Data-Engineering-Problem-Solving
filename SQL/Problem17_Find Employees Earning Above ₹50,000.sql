 CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
   (1, 'Arun', 'IT', 45000),
    (2, 'Priya', 'Data', 60000),
    (3, 'Kumar', 'IT', 55000),
    (4, 'Divya', 'HR', 40000),
     (5, 'Meena', 'Data', 70000)
AS employees(EmployeeId, EmployeeName, Department, Salary);

 SELECT
 EmployeeId,
EmployeeName,
 Department,
 Salary
 FROM employees
 WHERE Salary > 50000;
