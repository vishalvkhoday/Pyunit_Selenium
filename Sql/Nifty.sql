
select scr,round(avg(Hi),2) Hi,round(Avg(lw),2) Lw,round((avg(Hi) + Avg(lw))/2,2) Avg_HnL,round(sqrt(avg(Hi) * Avg(lw)),2)Sqrt_HnL,
round(((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)),2)/2 pvtpoint,ne.[Close]Cls,ne.Trnx_date from (
select Script scr,max([High])Hi,Min([Low])Lw from Nifty where Trnx_date > = (
select top 1 trnx from (
select distinct top 120  Trnx_date  trnx from Nifty
order by Trnx_date desc
) as T1 order by 1 
) group by Script
union all

select Script scr,max([High])Hi,Min([Low])Lw from Nifty where Trnx_date > = (
select top 1 trnx from (
select distinct top 90  Trnx_date  trnx from Nifty
order by Trnx_date desc
) as T1 order by 1 
)group by Script
union all

select Script scr,max([High])Hi,Min([Low])Lw from Nifty where Trnx_date > = (
select top 1 trnx from (
select distinct top 60  Trnx_date  trnx from Nifty
order by Trnx_date desc
) as T1 order by 1 
)group by Script
union all

select Script scr,max([High])Hi,Min([Low])Lw  from Nifty where Trnx_date > = (
select top 1 trnx from (
select distinct top 30  Trnx_date  trnx from Nifty
order by Trnx_date desc
) as T1 order by 1 
)group by Script

) as T2  inner join Nifty ne on 
ne.Script =T2.scr
--and ne.Trnx_date = (select max(Trnx_date) from Nifty)
group by scr,ne.[Close],ne.Trnx_date
having ne.[Close] between (round(((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)),2)/2) -(round(((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)),2)/2)*0.075
and (round(((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)),2)/2) +(round(((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)),2)/2)*0.075
--having ne.[Close] >=round((avg(Hi) + Avg(lw))/2,2) 
order by 8 desc