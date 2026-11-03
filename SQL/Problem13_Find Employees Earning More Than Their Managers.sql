 CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
    (1, 'Arun', 'Data', 90000, NULL),
   (2, 'Priya', 'Data', 95000, 1),
    (3, 'Kumar', 'Data', 70000, 1),
    (4, 'Meena', 'IT', 100000, NULL),
    (5, 'Ravi', 'IT', 110000, 4),
    (6, 'Divya', 'IT', 80000, 4),
    (7, 'Suresh', 'HR', 75000, NULL),
     (8, 'Kavya', 'HR', 85000, 7)
  AS employees(EmployeeId, EmployeeName, Department, Salary, ManagerId);
 SELECT
 e.EmployeeId,
e.EmployeeName,
 e.Department,
 e.Salary AS EmployeeSalary,
 m.EmployeeName AS ManagerName,
 m.Salary AS ManagerSalary
FROM employees e
 INNER JOIN employees m
 ON e.ManagerId = m.EmployeeId
 WHERE e.Salary > m.Salary;
