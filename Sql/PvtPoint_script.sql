

select scr,round(avg(Hi),2) Hi,round(Avg(lw),2) Lw,round((avg(Hi) + Avg(lw))/2,2) Avg_HnL,round(sqrt(avg(Hi) * Avg(lw)),2)Sqrt_HnL,
round(((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)),2)/2 pvtpoint,
round(((((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)))/2) +((((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)))/2)*0.075,2) pvt_UpRange,
 day60H.Day60High pvt_UpRange1,
round(((((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)))/2) -((((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)))/2)*0.075,2) pvt_LowRange,
Day60L.Day60Low pvt_DownRange1,
ne.[Close]Cls ,s.Sector,iss.Index_Name 
from (
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
and ne.Script_Name like '%%'
and ne.[close] > 10
and ne.Trnx_date = (select max(Trnx_date) from NSE_EOD)
inner join Sector s on 
s.Script_Name =ne.Script_Name
inner join (select ne1.Script_Name,max(ne1.[High]) Day60High from NSE_EOD ne1
where ne1.Trnx_date >= (select top 1 Trnx_date from (select distinct top 60 Trnx_date from NSE_EOD n1 order by n1.Trnx_date desc) as t1 order by 1 )
group by ne1.Script_Name
)as Day60H on 
ne.Script_Name = Day60H.Script_Name
inner join (select ne1.Script_Name,min(ne1.[Low]) Day60Low from NSE_EOD ne1
where ne1.Trnx_date >= (select top 1 Trnx_date from (select distinct top 60 Trnx_date from NSE_EOD n1 order by n1.Trnx_date desc) as t1 order by 1 )
group by ne1.Script_Name
)as Day60L on 
ne.Script_Name = Day60L.Script_Name
left outer join Index_Stock iss ON
--inner join Index_Stock iss on
ne.Script_Name = iss.Script_Name
and iss.Index_Name like '%Nifty50%'
--and iss.Index_Name ='Nifty50'
group by scr,ne.[Close],s.Sector,iss.Index_Name,Day60High,Day60Low
--having ne.[Close] > round(((((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)))/2) +((((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)))/2)*0.075,2)
--and  round(((((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)))/2) +((((avg(Hi) + Avg(lw))/2) + sqrt(avg(Hi) * Avg(lw)))/2)*0.075,2)
order by 1