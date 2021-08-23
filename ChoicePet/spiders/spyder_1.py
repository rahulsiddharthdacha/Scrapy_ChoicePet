import scrapy
from ..items import ChoicepetItem
import re
def func(val):
    val=val.replace(' ','')
    pos=['MON','TUE','WED','THU','FRI','SAT','SUN']
    if len(val)>17:
        time=val[:13]
        s=val[13:16]
        y=val[17:]
        ans=''
        for i in pos[pos.index(s):pos.index(y)+1]:
            ans+=i+'->'+time+'|'
        return ans 
    else:
        time=val[:13]
        s=val[13:16]
        return s+'->'+time+'|'

    
class Spyder1Spider(scrapy.Spider):
    name = 'spyder_1'
    start_urls = ['https://choicepet.com/pages/locations-1']

    def parse(self, response):
        items=ChoicepetItem()
        rows=response.xpath("//div[@class='locations-pg-container']/div[@id='accordionExample']/div[@class='card']//div[@class='row loc-pg-row']/div[@class='col-md-6']")
        for row in rows:
            items['Country']='USA'
            items['Phone']="".join(row.xpath("div[contains(@class,'col-sm-8')]/p[last()]/strong/text()").extract())
            name="".join(row.xpath("div[contains(@class,'col-sm-8')]/p/text()").extract()).split(',')
            loc="".join(row.xpath("div[contains(@class,'col-sm-4')]/a/@href").extract())
            times=row.xpath("div[contains(@class,'col-sm-8')]/ul/li/text()").extract()
            items['Duration']="".join(map(func,times))

            if len(name)==1:
                pass
            else:
                x = re.search("@", loc).start()
                y=re.search(',-',loc).start()
                items['Latitude']=loc[x+1:x+9]
                items['Longitude']=loc[y+1:y+9]
                if len(name[1].strip().split())==3:
                    x=name[1]
                    n,y,z=x.split()
                    name[1]=n+y+' '+z
                items['Street']=name[0]
                items['City']=name[1].split()[0][:-2]
                state,items['Zipcode']=name[1].split()
                items['State']=state[-2:]  
                items['StoreName']='ChoicePet'+'|'+state[-2:]
                yield items
            
