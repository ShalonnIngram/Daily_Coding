 197. Rising Temperature
  select distinct a.id as Id
  from weather a
  join weather b
  where a.temperature > b.temperature
  and Datediff(a.recordDate, b.recordDate) = 1
