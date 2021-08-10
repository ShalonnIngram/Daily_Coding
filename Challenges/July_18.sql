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
 from courses
 having count(student) >= 5

  
4. 620. Not Boring Movies
  select *
  from cinema
  where id % 2 = 1 and description != 'boring'
  order by rating desc
