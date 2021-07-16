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

  
3. 181. Employees Earning More Than Their Managers
  select a.name Employee
  from employee a 
  join employee b
  on a.ManagerId = b.Id
  where a.salary > b.salary
  
  
4. 182. Duplicate Emails
  select email 
  from person
  having count(email) > 1
