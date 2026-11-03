
 CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
    (1, 'Arun', 'Data', 60000),
   (2, 'Priya', 'Data', 75000),
     (3, 'Kumar', 'IT', 90000),
    (4, 'Meena', 'HR', 75000),
   (5, 'Ravi', 'IT', 85000),
     (6, 'Divya', 'Data', 60000)
 AS employees(EmployeeId, EmployeeName, Department, Salary);

SELECT
 EmployeeId,
     EmployeeName,
    Department,
    Salary
 FROM (
     SELECT
     *,
     DENSE_RANK() OVER (
     ORDER BY Salary DESC
    ) AS salary_rank
    FROM employees
 )
 WHERE salary_rank = 2;
