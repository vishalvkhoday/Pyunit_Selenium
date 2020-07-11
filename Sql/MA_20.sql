

select sl.Script_Name,sl.[Low],sl.Trnx_date SLTrnx,ne.[Open],ne.[High],ne.[Low],ne.[Close],ne.Volume,round(((ne.[Close]-sl.[Low])/sl.[Low])*100,2) chg,
v_MA20.MA20,s.Sector
from v_Script_Low sl inner join Index_Stock ISS on
sl.Script_Name = ISS.Script_Name
and iss.Index_Name ='Nifty100'
inner join NSE_EOD ne on 
ne.Script_Name = sl.Script_Name
and ne.Trnx_date = (select max(trnx_date) from NSE_EOD)
inner join Sector s on
ne.Script_Name = s.Script_Name
inner join v_MA20  on
ne.Script_Name =v_MA20.Script_Name
and v_MA20.trnx = (select max(trnx_date) from NSE_EOD)
where round(((ne.[Close]-sl.[Low])/sl.[Low])*100,2) between 20 and 55

