#MYSql
# Write your MySQL query statement below
select ifnull(
(select distinct Salary 
from Employee
order by Salary desc
limit 1 offset 1), NULL
)
as SecondHighestSalary

#mssql
/* Write your T-SQL query statement below */
select ISNULL((select distinct Salary from Employee
order by Salary desc
OFFSET 1 ROWS
FETCH NEXT 1 ROWS ONLY), NULL)
AS "SecondHighestSalary";
