select * from player P
join
hall_of_fame H
on (P.player_id=H.player_id)
join player_college PC
on (P.player_id=PC.player_id and H.player_id=PC.player_id)
where H.inducted='Y'
group by PC.college_id;

select player.player_id, name_first, name_last, college_id
from player
inner join hall_of_fame
on player.player_id = hall_of_fame.player_id
inner join player_college
on player.player_id = player_college.player_id
where hall_of_fame.inducted = 'Y'
group by player.player_id, college_id
order by college_id;

select college_id, count(distinct player.player_id) c
from player
inner join hall_of_fame
on player.player_id = hall_of_fame.player_id
inner join player_college
on player.player_id = player_college.player_id
where hall_of_fame.inducted = 'Y'
group by college_id
order by c desc
;
