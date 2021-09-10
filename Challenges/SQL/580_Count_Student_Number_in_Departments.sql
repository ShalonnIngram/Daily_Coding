select dept_name,
       count(student_id) student_number
from student s
right join department d
on s.dept_id = d.dept_id
group by 1 
order by 2 desc
