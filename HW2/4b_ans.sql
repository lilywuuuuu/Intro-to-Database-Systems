with 
avg_case20(country_code, avg_case) as
(select country_code, avg(confirmed_cases)
 from cases
 where date between '2020-05-26' and '2020-06-01'
 group by country_code
),

avg_case21(country_code, avg_case) as
(select country_code, avg(confirmed_cases)
 from cases
 where date between '2021-05-26' and '2021-06-01'
 group by country_code
),

avg_case22(country_code, avg_case) as
(select country_code, avg(confirmed_cases)
 from cases
 where date between '2022-05-26' and '2022-06-01'
 group by country_code
),

overstr20(continent_code, date, max_overstr) as
(select cn.continent_code, i.date, max(i.stringency_fd/a.avg_case)
 from countries as ct, continents as cn, index as i, place as p, avg_case20 as a
 where p.continent_code = cn.continent_code
	and ct.country_code = p.country_code
	and i.country_code = p.country_code
 	and a.country_code = i.country_code
 	and i.date = '2020-06-01'
 group by (cn.continent_code, i.date)
),

overstr21(continent_code, date, max_overstr) as
(select cn.continent_code, i.date, max(i.stringency_fd/a.avg_case)
 from countries as ct, continents as cn, index as i, place as p, avg_case21 as a
 where p.continent_code = cn.continent_code
	and ct.country_code = p.country_code
	and i.country_code = p.country_code
 	and a.country_code = i.country_code
	and i.date = '2021-06-01'
 group by (cn.continent_code, i.date)
),

overstr22(continent_code, date, max_overstr) as
(select cn.continent_code, i.date, max(i.stringency_fd/a.avg_case)
 from countries as ct, continents as cn, index as i, place as p, avg_case22 as a
 where p.continent_code = cn.continent_code
	and ct.country_code = p.country_code
	and i.country_code = p.country_code
	and a.country_code = i.country_code
	and i.date = '2022-06-01'
 group by (cn.continent_code, i.date)
)

(select ct.country_name, cn.continent_name, s.max_overstr, s.date
from countries as ct, continents as cn, index as i, place as p, overstr22 as s, avg_case22 as a
where p.continent_code = cn.continent_code
	and ct.country_code = p.country_code
	and i.country_code = p.country_code
	and i.date = '2022-06-01'
	and i.date = s.date
	and i.stringency_fd/a.avg_case = s.max_overstr
	and p.continent_code = s.continent_code
	and a.country_code = i.country_code)
union
(select ct.country_name, cn.continent_name, s.max_overstr, s.date
from countries as ct, continents as cn, index as i, place as p, overstr21 as s, avg_case21 as a
where p.continent_code = cn.continent_code
	and ct.country_code = p.country_code
	and i.country_code = p.country_code
	and i.date = '2021-06-01'
	and i.date = s.date
	and i.stringency_fd/a.avg_case = s.max_overstr
	and p.continent_code = s.continent_code
	and a.country_code = i.country_code)
union
(select ct.country_name, cn.continent_name, s.max_overstr, s.date
from countries as ct, continents as cn, index as i, place as p, overstr20 as s, avg_case20 as a
where p.continent_code = cn.continent_code
	and ct.country_code = p.country_code
	and i.country_code = p.country_code
	and i.date = '2020-06-01'
	and i.date = s.date
	and i.stringency_fd/a.avg_case = s.max_overstr
	and p.continent_code = s.continent_code
	and a.country_code = i.country_code)
order by date, continent_name

