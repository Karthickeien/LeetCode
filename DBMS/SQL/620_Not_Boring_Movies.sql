select id, movie, description, rating 
from Cinema 
where id mod 2 != 0  and description !='boring'
order by rating desc
