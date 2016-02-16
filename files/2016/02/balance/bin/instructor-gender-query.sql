select p.gender || ',' || count(*)
from workshops_person as p join workshops_award as a join workshops_badge as b
where b.name='swc-instructor'
and a.badge_id=b.id
and a.person_id=p.id
group by p.gender;
