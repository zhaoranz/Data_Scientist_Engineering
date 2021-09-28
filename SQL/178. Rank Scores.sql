## Write your MySQL query statement below
select a.Score as Score,
(select count(distinct b.Score) from Scores b where b.Score>=a.Score) as `Rank`
from Scores a
order by a.Score desc

# Write your MySQL query statement below
##Faster, more efficient

select t.score Score,t.rank `Rank` from scores join
(
    SELECT p.score score , @rank:=@rank+1 `rank` FROM 
        (SELECT distinct(score) score FROM Scores ORDER BY score DESC) p , (SELECT @rank:=0 ) q
) t 
on scores.score = t.score
order by score desc
