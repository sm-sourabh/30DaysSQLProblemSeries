WITH rankedSalary AS(
    SELECT employee_id,
    salary,
    DENSE_RANK() OVER (
        PARTITION BY department ORDER BY SALARY DESC
    ) as rank
    FROM employees
)
SELECT *
FROM rankedSalary
WHERE rank = 2  --replace '2' with n as provided