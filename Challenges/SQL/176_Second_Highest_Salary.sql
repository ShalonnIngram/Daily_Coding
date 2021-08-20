176. Second Highest Salary
  select max(salary) SecondHighestSalary
  from employee
  where salary < (select max(salary) first from Employee) 
