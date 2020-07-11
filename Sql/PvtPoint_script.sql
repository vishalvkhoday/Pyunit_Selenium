

select scr,round(avg(Hi),2) Hi,round(Avg(lw),2) Lw,round((avg(Hi) + Avg(lw))/2,2) Avg_HnL,round(sqrt(avg(Hi) * Avg(lw)),2)Sqrt_HnL,
round(((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)),2)/2 pvtpoint,ne.[Close]Cls ,s.Sector from (
select Script_Name scr,max([High])Hi,Min([Low])Lw from NSE_EOD where Trnx_date > = (
select top 1 trnx from (
select distinct top 120  Trnx_date  trnx from NSE_EOD
order by Trnx_date desc
) as T1 order by 1 
) group by Script_Name
union all

select Script_Name scr,max([High])Hi,Min([Low])Lw from NSE_EOD where Trnx_date > = (
select top 1 trnx from (
select distinct top 90  Trnx_date  trnx from NSE_EOD
order by Trnx_date desc
) as T1 order by 1 
)group by Script_Name
union all

select Script_Name scr,max([High])Hi,Min([Low])Lw from NSE_EOD where Trnx_date > = (
select top 1 trnx from (
select distinct top 60  Trnx_date  trnx from NSE_EOD
order by Trnx_date desc
) as T1 order by 1 
)group by Script_Name
union all

select Script_Name scr,max([High])Hi,Min([Low])Lw  from NSE_EOD where Trnx_date > = (
select top 1 trnx from (
select distinct top 30  Trnx_date  trnx from NSE_EOD
order by Trnx_date desc
) as T1 order by 1 
)group by Script_Name

) as T2  inner join NSE_EOD ne on 
ne.Script_Name =T2.scr
and ne.Trnx_date = (select max(Trnx_date) from NSE_EOD)
and ne.Script_Name like '%%'
and ne.[close] > 10
inner join Sector s on 
s.Script_Name =ne.Script_Name
group by scr,ne.[Close],s.Sector
having ne.[Close] between (round(((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)),2)/2) -(round(((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)),2)/2)*0.05
and (round(((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)),2)/2) +(round(((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)),2)/2)*0.05
--having ne.[Close] >=round((avg(Hi) + Avg(lw))/2,2) 
order by 1

