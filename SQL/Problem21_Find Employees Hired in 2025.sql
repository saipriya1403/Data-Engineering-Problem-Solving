CREATE OR REPLACE TEMP VIEW employees AS
 SELECT * FROM VALUES
    (1, 'Arun', '2024-06-15'),
    (2, 'Priya', '2025-01-10'),
    (3, 'Kumar', '2025-08-20'),
   (4, 'Divya', '2026-02-05'),
     (5, 'Meena', '2025-11-12')
 AS employees(EmployeeId, EmployeeName, JoiningDate);

SELECT
 EmployeeId,
 EmployeeName,
 JoiningDate
 FROM employees
 WHERE YEAR(TO_DATE(JoiningDate)) = 2025;
