select s.id id,
       s.name name
from students s
where s.department_id not in (select d.id from departments d)
