181. Employees Earning More Than Their Managers
  select a.name Employee
  from employee a 
  join employee b
  on a.ManagerId = b.Id
  where a.salary > b.salary
  
