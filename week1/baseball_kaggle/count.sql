select * from player P
join
hall_of_fame H
on (P.player_id=H.player_id)
join player_college PC
on (P.player_id=PC.player_id and H.player_id=PC.player_id)
where H.inducted='Y'
group by PC.college_id;
