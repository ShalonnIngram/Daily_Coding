1. 595. Big Countries
  select name, population, area
  from world 
  where area > 3000000 or population > 25000000
  
2. 197. Rising Temperature
  select distinct a.id as Id
  from weather a
  join weather b
  where a.temperature > b.temperature
  and Datediff(a.recordDate, b.recordDate) = 1
    
3. 596. Classes More Than 5 Students
  select class
  from
      (select class, count(distinct student) num
      from courses
      group by class) temp
  where num >= 5
