WITH RankedEarners AS (
    SELECT 
        employee_id,
        department_id,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY department_id 
            ORDER BY salary DESC
        ) as row_num
    FROM employee
)
SELECT 
    department_id,
    employee_id,
    salary
FROM RankedEarners
WHERE row_num <= 3;