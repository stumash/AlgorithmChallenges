-- get second highest salary
SELECT
    top_two_salaries.Salary AS SecondHighestSalary
FROM
    (
        SELECT
            DISTINCT Salary
        FROM
            Employee
        ORDER BY
            Salary DESC
        LIMIT 2
    ) AS top_two_salaries
    RIGHT JOIN
    (
        SELECT
            DISTINCT Salary
        FROM
            Employee
        ORDER BY
            Salary DESC
        LIMIT 2
    ) AS top_two_salaries_2
    ON
        top_two_salaries.Salary < top_two_salaries_2.Salary
LIMIT 1
;
