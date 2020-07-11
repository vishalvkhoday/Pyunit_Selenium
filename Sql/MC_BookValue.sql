select si.Script_Name,si.Market_Cap,si.EPS,si.PE,si.BookValue,si.PriceBook,si.Div,si.Industry_PE ,round((select avg(PriceBook) from Stock_Info where [Quarter] = (select max([Quarter]) from Stock_Info)
and Sector = 'COMPUTERS - SOFTWARE' ),2)Avg_BTP,(select avg(PE)  from Stock_Info where [Quarter] = (select max([Quarter]) from Stock_Info)
and Sector = 'COMPUTERS - SOFTWARE' )Avg_PE from Stock_Info si
where [Quarter] = (select max([Quarter]) from Stock_Info)
and Sector = 'COMPUTERS - SOFTWARE'
group by si.Script_Name,si.Market_Cap,si.EPS,si.PE,si.BookValue,si.PriceBook,si.Div,si.Industry_PE

select * from Stock_Info si inner join (
select round(avg(PE),2)avg_PE,sector from Stock_Info
where [Quarter] = (select max([Quarter]) from Stock_Info)
group by Sector
)as s on 
si.Sector = s.Sector
where [Quarter] = (select max([Quarter]) from Stock_Info)
and s.avg_PE is not null
and si.PE > s.avg_PE
and si.Div > 0
and si.DivYeild > 5

order by s.Sector, si.Script_Name

