SELECT 
    st.student_id, 
    st.student_name, 
    su.subject_name, 
    IFNULL(COUNT(e.subject_name), 0) AS attended_exams
FROM 
	Students st 
JOIN 
	Subjects su 
LEFT JOIN
	Examinations e 
ON 
	st.student_id = e.student_id 
AND 
	su.subject_name = e.subject_name
GROUP BY 
	1, 3 
ORDER BY 
	1, 3


