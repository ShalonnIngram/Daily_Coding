# LEETCODE CHALLENGES

## SQL
1. Combine Two Tables:
  select FirstName, LastName, City, State
  from Person 
  left join Address 
  on Person.PersonId = Address.PersonId;

2. 176. Second Highest Salary
  select max(salary) SecondHighestSalary
  from employee
  where salary < (select max(salary) first from Employee) 
