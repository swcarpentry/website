select p.username || ',' || p.gender || ',' || count(*)
from workshops_person as p join workshops_task as t join workshops_role as r join workshops_event as e
where p.id=t.person_id
and t.role_id=r.id
and t.event_id=e.id
and r.name='instructor'
and e.start>='2015-01-01'
and e.start<='2015-12-31'
group by p.username
order by p.username;
