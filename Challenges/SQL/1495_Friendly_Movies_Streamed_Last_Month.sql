select monthname(program_date) month,
       title, 
       kids_content,
       content_type
from tvprogram t
join content c
on t.content_id = c.content_id
)
select title
from cte
where month = 'June' and content_type = 'Movies' and kids_content = 'Y'
