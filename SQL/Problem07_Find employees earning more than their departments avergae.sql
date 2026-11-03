
 CREATE OR REPLACE TEMP VIEW employees AS
 SELECT * FROM VALUES
 (1, 'Arun', 'Data', 60000),
 (2, 'Priya', 'Data', 80000),
 (3, 'Kumar', 'IT', 90000),
(4, 'Meena', 'IT', 70000),
 (5, 'Ravi', 'HR', 50000),
 (6, 'Divya', 'HR', 65000)
 AS employees(EmployeeId, EmployeeName, Department, Salary);

 select EmployeeId,EmployeeName,Department, Salary
From (
    select * ,avg(Salary) over(partition by 
    Department) as department_avgsalary
    from employees
 )
 where Salary > department_avgsalary
