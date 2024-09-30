-- Write query to find the number of grade A's given by the teacher who has graded the most assignments

SELECT COUNT(*)
FROM assignments
WHERE grade = 'A'
AND graded_by = (
    SELECT graded_by
    FROM assignments
    GROUP BY graded_by
    ORDER BY COUNT(*) DESC
    LIMIT 1
);