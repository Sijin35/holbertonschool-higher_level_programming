-- Lists number of records with same score in second_table
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
HAVING COUNT(*) >= 1
ORDER BY score DESC;
