with str(continent_code, date, max_str) as 
(select cn.continent_code, i.date, max(i.stringency_fd)
from countries as ct, continents as cn, index as i, place as p
where p.continent_code = cn.continent_code
	and ct.country_code = p.country_code
	and i.country_code = p.country_code
	and (i.date = '2022-06-01' or i.date = '2021-06-01' or i.date = '2020-06-01')
group by (cn.continent_code, i.date))

select ct.country_name, cn.continent_name, s.date
from countries as ct, continents as cn, index as i, place as p, str as s
where p.continent_code = cn.continent_code
	and ct.country_code = p.country_code
	and i.country_code = p.country_code
	and (i.date = '2022-06-01' or i.date = '2021-06-01' or i.date = '2020-06-01')
	and i.date = s.date
	and i.stringency_fd = s.max_str
	and p.continent_code = s.continent_code
order by date, cn.continent_name
