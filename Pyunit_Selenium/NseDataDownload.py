import urllib.response
import zipfile
import requests

# objzpFil =zipfile.ZipFile('C:/Users/DELL/Downloads/hakija-master.zip')
# objzpFil.extractall('C:/Users/DELL/Downloads/')
# objzpFil.close
# print('Done')


objurl = requests.get('https://www1.nseindia.com/content/historical/EQUITIES/2020/JAN/cm16JAN2020bhav.csv.zip', stream =True)
print('download completed')
if objurl.status_code =='200' :
    with open('C:/Users/DELL/Downloads/EOD.zip') as f:
        f.write(objurl.content)

print("EOD DATA")