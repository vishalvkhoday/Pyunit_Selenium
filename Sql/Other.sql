

select * from MF_Holding mf1 inner join Sector s on
mf1.Script_Name=s.Script_Name
where No_of_Shares in(select max(No_of_Shares) from MF_Holding mf2  where mf2.Script_Name=mf1.Script_Name)
and [Quarter] = (select max([Quarter]) from MF_Holding)
order by mf1.No_of_Shares desc,mf1.Mutal_Funds,s.Sector,mf1.Script_Name



select mf1.scrName,mf3.Mutal_Funds,mf3.No_of_Shares,mf3.[Quarter] from v_MF_Holding mf1 inner join MF_Holding mf3 on 
mf1.scrName=mf3.Script_Name
and mf1.Qtr=mf3.[Quarter]
where mf1.T_noShare = (select max(T_noShare) from v_MF_Holding mf2 where mf1.scrName=mf2.scrName)
and convert(date,[Qtr]) = '2019-05-24'
order by scrName

select mf1.scrName,mf3.Mutal_Funds,mf3.No_of_Shares,mf3.[Quarter],s.Sector from v_MF_Holding mf1 inner join MF_Holding mf3 on 
mf1.scrName=mf3.Script_Name
and mf1.Qtr=mf3.[Quarter]
inner join Sector s on
mf1.scrName=s.Script_Name
where mf1.T_noShare = (select max(T_noShare) from v_MF_Holding mf2 where mf1.scrName=mf2.scrName)
and convert(date,[Qtr]) = '2019-05-24'
order by scrName



-- select * from v_MF_Holding
select distinct sh.Script_Name,sh.High,sl.Low,sh.Trnx_date High_Dt,sl.Trnx_date Low_Dt,ne.[Close],ne.Volume,
ROUND(((NE.[Close] - SL.Low)/SL.Low)*100,2) l_AGE,ROUND(((sh.High - ne.[Close])/ne.[Close])*100,2) H_AGE,
s.Sector,DATEDIFF(DAY,sh.Trnx_date,sl.Trnx_date)DaysDif from Script_High sh inner join Script_Low sl on 
sh.Script_Name=sl.Script_Name
and sh.[Year] = sl.[Year]
inner join Sector s on 
sh.Script_Name = s.Script_Name
inner join NSE_EOD ne on
ne.Script_Name = sh.Script_Name
and ne.Script_Name =sl.Script_Name
WHERE sl.Script_Name not in ('_ADVANCE','_DECLINE','_UNCHANGED')
and sh.Script_Name not like '%ETF%'
--and year(sh.Trnx_date)='2019' and year(sl.Trnx_date)='2019'
--and DATEDIFF(DAY,sh.Trnx_date,sl.Trnx_date) < 0 
and DATEDIFF(DAY,sh.Trnx_date,sl.Trnx_date) between -180 and 0
--and MONTH(sh.Trnx_date)  4
and sl.Trnx_date > GETDATE() -70
and ne.Trnx_date = (select max(Trnx_date) from NSE_EOD)
and ne.Volume > 10000
order by 8


select distinct sh.Script_Name,sh.High,sh.Trnx_date H_dt,sl.Low,sl.Trnx_date L_dt,ne.[Close],ne.Volume ,DATEDIFF(DAY,sh.Trnx_date,sl.Trnx_date)Dt_Diff,		
round(((ne.[Close] - sl.Low)/sl.Low)*100,2) Pagr,round(((sh.High-sl.Low)/sh.High)*100,2)Diff_Age,s.Sector
from v_Script_High sh inner join v_Script_Low sl on sh.Script_Name=sl.Script_Name
inner join NSE_EOD ne on sh.Script_Name=ne.Script_Name
and sl.Script_Name=ne.Script_Name inner join Sector s on 
sh.Script_Name=s.Script_Name 
where ne.Trnx_date= (select max(Trnx_date)from NSE_EOD)
and sl.Trnx_date > GETDATE()-10
and round(((ne.[Close] - sl.Low)/sl.Low)*100,2) < 8
and ne.[Close]between 25 and 275
and round(((sh.High-sl.Low)/sh.High)*100,2) >45
order by s.Sector



select br1.Script_Name,br1.[Quarter],br1.Total_Income,br1.Net_Profit,round((br1.Net_Profit/br1.Total_Income)*100,2)Pro_Age,s.Sector from Bse_Results br1
inner join Sector s on
br1.Script_Name=s.Script_Name
where Net_Profit = (select max(Net_Profit) from Bse_Results br2 where br1.Script_Name=br2.Script_Name)
and Total_Income!=0
and br1.[Quarter] ='2019-03-01 00:00:00.000'
and s.Sector like '%logi%'
and round((br1.Net_Profit/br1.Total_Income)*100,2) >0
order by 5,Script_Name




select br.Script_Name,round(avg(br.Revenue),2)Revenue,round(avg(br.Total_Income),2) TotalIncome,round(avg(br.Net_Profit),2)NetProfit,
round(avg((br.Net_Profit/br.Total_Income)*100),2)Prof_age,round(avg((br.EPS)*4),2)EPS,ne.[Close] ,round(ne.[Close]/avg((br.EPS)*4),2)PE,bs.Total_Debt,
bs.Total_Assets,bs.Total_Share_Capital,br.Sector,count(*)Occr  from Bse_Results br inner join NSE_EOD ne on 
 ne.Script_Name = br.Script_Name
 inner join Bal_sheet bs on
 bs.Script_Name=ne.Script_Name
 and ne.Script_Name = bs.Script_Name
 where convert(date,br.[Quarter]) in ('2019-06-01','2019-03-01','2018-12-01','2018-09-01') 
 and ne.Trnx_date = (select max(Trnx_date)from NSE_EOD )
 and bs.[Quarter] = (select max([Quarter]) from Bal_sheet )
 and br.EPS > 0  and br.Net_Profit > 0 and br.Total_Income !=0 and br.PBDT > 0 and br.PBT > 0
 and br.Total_Income > bs.Total_Debt
 and ne.[Close] < 1000
group by br.Script_Name,br.Sector,ne.[Close],bs.Total_Debt,bs.Total_Assets,bs.Total_Share_Capital
having count(*)>=2 and avg(br.Net_Profit)>0 and avg(br.Revenue) > 10
order by br.Script_Name



select x1.Script_Name,closing,Trnx_date,round(DMA20,2)DMA20,round(DMA30,2)DMA30,iif(closing < DMA20,'Below','Above')DMA20Sig,iif(closing < DMA30,'Below','Above')DMA30Sig,s.Sector from (
select x.*,avg(closing) over (partition by script_name order by trnx_date rows between 19 preceding and current row) as DMA20
,avg(closing) over (partition by script_name order by trnx_date rows between 29 preceding and current row) as DMA30
from (select script_name,avg([close]) as closing,trnx_date from NSE_EOD group by Script_Name,Trnx_date) x
) x1 inner join Sector s on
x1.Script_Name =s.Script_Name
where Trnx_date = convert(date,getdate(),104)
and iif(closing < DMA30,'Below','Above') = 'Above'
and closing between 20 and 100
and DMA20 > DMA30
 