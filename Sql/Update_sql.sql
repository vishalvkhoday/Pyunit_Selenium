
Declare @scr as varchar(50)
Declare @days as int
set @scr ='HINDUNILVR'
set @days = 90
select ne.Script_Name,avg(ne.Change)chg,count(*)cnt,s.Sector from NSE_EOD ne inner join Sector s on
ne.Script_Name = s.Script_Name
where Trnx_date in  (select Trnx_date from NSE_EOD where Script_Name =@scr and Change>0  and Trnx_date > GETDATE()-@days)
and ne.Script_Name not in ('_ADVANCE','_DECLINE','_UNCHANGED')
and Change > 0
group by ne.Script_Name,s.Sector
having count(*)>=(select count(*) from NSE_EOD where Script_Name =@scr and Change>0  and Trnx_date > GETDATE()-@days)-5
order by s.Sector,2 desc,ne.Script_Name






select br.Script_Name,COUNT(*)CNT,ne.[Close] cls,s.Sector  from Bse_Results br inner join NSE_EOD ne on
br.Script_Name = ne.Script_Name
inner join Sector s on 
ne.Script_Name =s.Script_Name
where br.Script_Name in (
select Script_Name from Bse_Results where [Quarter] = (select max([Quarter]) from Bse_Results)
) and year([Quarter]) = '2019' and Net_Profit >=0
and ne.Trnx_date = (select max(Trnx_date) from NSE_EOD)
and ne.[Close] between 20 and 250
group by br.Script_Name,ne.[Close],s.Sector
having count(*) =4
order by br.Script_Name



select ne.Script_Name,sum(ne.Change)chg,DATEPART(WEEK,ne.Trnx_date)WeekNos,s.Sector,avg(ne.[Close]) Cls from NSE_EOD ne inner join Sector s on
ne.Script_Name = s.Script_Name
and year(ne.Trnx_date) = '2019'
group by ne.Script_Name,DATEPART(WEEK,ne.Trnx_date),s.Sector
having DATEPART(WEEK,ne.Trnx_date) > 49
order by chg desc

