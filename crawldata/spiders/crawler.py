import scrapy,json,os,platform
from crawldata.functions import *
from datetime import datetime

class CrawlerSpider(scrapy.Spider):
    name = 'vivino'
    DATE_CRAWL=datetime.now().strftime('%Y-%m-%d')
    #custom_settings={'LOG_FILE':'./log/'+name+'_'+DATE_CRAWL+'.log'}
    if platform.system()=='Linux':
        URL='file:////' + os.getcwd()+'/scrapy.cfg'
    else:
        URL='file:///' + os.getcwd()+'/scrapy.cfg'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Referer': 'https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NTBQS660TStSS7Z1DQ1SKwDKpqfZliUWZaaWJOao5Rel2CYWJ6vlJ1XaFhRlJqcCAJI8FVc%3D','Alt-Used': 'www.vivino.com','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Priority': 'u=0, i'}
    cookies = {'first_time_visit': 'aulCmw9JsDyqx9WySg%2FlKWXQfgPl%2FaT2xhpIUI2ljG%2B2hSwqHp%2F4vKjdc3dlAuHEocwEwTIdyFYkdeoF20jhViwmPmy%2FoMvIJypx7Vmu%2BVViGf%2FJCcrfWIN%2FERrRjyeXYPE%3D--%2F%2F6nNnpSyo5KchAs--gUXYCGdJH1DiyUP2JRy56Q%3D%3D','client_cache_key': '5ZKP3xuymtpTQgAun5pkL7dm6pOIB0LUc0eKlRhyP47LA03l95yEvjdu9bxxNjYU6kzZfcXIY%2B6%2F6xWSb1WtxGrNnneOTv3dcdQ1%2F%2Fh81nlKUA2xMyMXXmZ7tMSxa3bOJmGpsZEUyiOvmYz2k0ZXhWpc--pHJHdgWwZza7txjK--n0HtZjrFeJApvMhvSxZw8A%3D%3D','anonymous_tracking_id': 'ZVyQb0zx9S40EdPAsefMMv6I7QGaBHelgGHjU%2BYsMQYCGGE3CI%2F7IMqncLU9hol99tjUjX6kBKziXwhQu0cclFNZgJ%2F5%2FYSkkrTF5uAHexZvpAL8a%2BkNdrkFnx1RKdIYRWn4fJn9BtX4S%2BAcWmVdgluVtWCcoeNOT6uP3qtsT7Iz0sNnOCaWQZIYdLRlXfMmxZ2u--yKmHqvG0aVnpuWib--pDkndJ0So7JbZ36ENCIUjA%3D%3D','csrf_token': 'EZn5Vtw4VFY0OUMYXGPLqbc_cIEfbFz8wUDPE2ayY83l6RkqeY_WP5qJzHMbANLdEDA8d4WhcyAySiZfcwyNnA','_ruby-web_session': 'oa3rRu9%2BX40ElUoe%2B6vtYGW14uAWZz4dAlphvMB2eGF0LiQblQPyDEuhewvs24AALEIvHX7p4j0TECWSgb6RzijyVI6tmnVrXUL4pE0lM5GySV6nb%2BR9mDBU%2FDil%2Bk2WVl%2FlK3oX3RqFienEtxccrrR8sWDgEmeFLqK8g21nTZaNHywSi0VOuzJsBJNm2e7pDyqhoVKbVQMVu8OZQfbYfsaW%2FKLmIPCrcedYg5fUkVCbXCQGK5eBZbTeXMLHwQ1Gpd8xcuPDam5utsRmNvErOvhMtRhyq2KwQcEFhPPxfCTVsaf0PuxUC8cZ7D8E4aDgdLHCEkpZ%2B37CXnKUFBy4oyzRv4THyoXHL6u6%2BZgxm0wEGVsBkc0cTE4HOooGcZAIlS97kgXQqTO7C2Zqph7a3mR1N2PhWjHQ2yrOi2eSz9AeGAe%2BAgGGQh8QDTHGbN%2BCPFXY1dc9v2rJEeeKHJSYj4XE%2B7RLV1mEkJykb%2BoPZU4VUGvg%2Bl4%2Bz7gzVODLbRUZ26tZV03JK2M2rW4qMMsgnR3O1e7tYe%2BEEQDF3d7sBQ%3D%3D--L3p1HvmO%2FrZ%2BAThZ--gnFJwNvFS4QnCSjDaPDhsA%3D%3D','eeny_meeny_explorer_card_v2': 'NyWWEvbmO4ONwbr8k8JSgr9bXcDv%2BVTVOLZKPRR46XjXOfHCNsoiVyxV%2FSjK8WdB%2BD0N4GJjjZgzMqQbKgNfmA%3D%3D','_pin_unauth': 'dWlkPU1EYzJPV0l6TldJdFltWmxZaTAwTXpNNUxUbG1OVE10T0dNeFlXWmhaamsxTlRjeQ','_gcl_au': '1.1.838658046.1732073029','_ga_D35SJB5ZNL': 'GS1.1.1732073028.1.1.1732073307.55.0.0','_ga': 'GA1.2.533927524.1732073029','_attn_': 'eyJ1Ijoie1wiY29cIjoxNzMyMDczMDI5OTY1LFwidW9cIjoxNzMyMDczMDI5OTY1LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjE1ZDg1MjhmZmE5MTQ4YjE4ZTRiNmFiMjE5YzYxODY4XCJ9In0=','__attentive_id': '15d8528ffa9148b18e4b6ab219c61868','__attentive_cco': '1732073029966','_dd_s': 'rum=0&expire=1732074239784','mp_bee7544764ece4336acb3b402265c80c_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A193479902091470-08aa7f4cadfd898-432c2f36-1fa400-193479902091470%22%2C%22%24device_id%22%3A%20%22193479902091470-08aa7f4cadfd898-432c2f36-1fa400-193479902091470%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D','_gid': 'GA1.2.149701949.1732073030','ab.storage.sessionId.932da152-bffc-4d62-a719-894efe56ebac': 'g%3A92be8de7-0aeb-b055-6dd7-8a7e0a14f431%7Ce%3A1732075113217%7Cc%3A1732073030219%7Cl%3A1732073313217','ab.storage.deviceId.932da152-bffc-4d62-a719-894efe56ebac': 'g%3A600f5d50-3dd6-71f3-b4d6-81f78cb01638%7Ce%3Aundefined%7Cc%3A1732073030221%7Cl%3A1732073030221','_fbp': 'fb.1.1732073030420.581314976529932478','__attentive_dv': '1','__attentive_pv': '7','__attentive_ss_referrer': 'ORGANIC','_clck': 'vllsc4%7C2%7Cfr1%7C0%7C1785','idw-fe-id': '3e51959b-6910-4316-9c71-2bfce523973a','_clsk': 'v5xji2%7C1732073305602%7C9%7C0%7Cu.clarity.ms%2Fcollect','cto_bundle': 'PgJ1h19nWTJMUlBHeERzVUNCZWpENmZRSzgxak95OGZET0FaZEtQQ202YTd1cjI2dTd3c1c5VzRBaEJDeDJsS1ZoUEp5Y3BRRUFFWWpOSGtldXcwMExLNDAlMkZTRkNhbjJzWU9YUFVPYUgycU84cEdrbkV0cEE3d2tDcFZRRWoydzhIU3Zha2NUVUlQa3Zsb00zYk9Ydmp3UlpuUSUzRCUzRA','_gat_UA-222490-2': '1','_uetsid': 'dd01bb30a6ee11efacf1b5ed5f5b5212','_uetvid': 'dd020080a6ee11ef8b399f73cc4a168a'}
    KEYS=[]
    PROXY=[]
    def start_requests(self):
        url='https://www.vivino.com/explore?e=eJwNyTEOgCAQBMDfbI302_kDY2UszgMJiQgBNfJ7nXZS5YAUTxokeWkNtPNuUM7TiPJn2PlIjf6SA7k6Ot8UeessNapHWFZaNKp8nRQY6g%3D%3D'
        yield scrapy.Request(url,callback=self.parse,dont_filter=True,headers=self.headers,cookies=self.cookies,meta={'url':url})

    def parse(self, response):
        Title=response.xpath('//h2/text()').get()
        print(Title)
        json_data=response.xpath('//script[@data-component-name="ExplorePage"]/text()').get()
        try:
            DATA=json.loads(json_data)
            if not response.meta['proxy'] in self.PROXY:
                self.PROXY.append(response.meta['proxy'])
                open('proxy.txt','a').write("\n"+response.meta['proxy'])
        except:
            DATA=None
            yield scrapy.Request(response.meta['url'],callback=self.parse,dont_filter=True,headers=self.headers,cookies=self.cookies,meta={'page':page,'url':response.meta['url']})
        if DATA:
            Data=DATA['initialExploreResults']['records']
            for row in Data:
                url='https://www.vivino.com/FR/en/'+row['vintage']['seo_name']+'/w/'+str(row['vintage']['wine']['id'])+'?year='+str(row['vintage']['year'])+'&price_id='+str(row['price']['id'])
                K=key_MD5(url)
                if not K in self.KEYS:
                    self.KEYS.append(K)
                    yield scrapy.Request(url,callback=self.parse_data,dont_filter=True,headers=self.headers,cookies=self.cookies,meta={'ROW':row,'url':url})
                else:
                    print('Duplicate URL:',url)
            if response.xpath('//li/div[contains(@class,"explorerPagination-module__next--")]/a[not(@aria-disabled)]'):
                url='https://www.vivino.com'+response.xpath('//li/div[contains(@class,"explorerPagination-module__next--")]/a[not(@aria-disabled)]/@href').get()
                yield scrapy.Request(url,callback=self.parse,dont_filter=True,headers=self.headers,cookies=self.cookies,meta={'url':url})
    def parse_data(self,response):
        ROW=response.meta['ROW']
        # json_data=response.xpath('//script[@data-component-name="WineLocationHeader"]/text()').get()
        json_data=response.xpath('//script[@data-component-name="PurchaseAvailability"]/text()').get()
        try:
            Data=json.loads(json_data)['pageInformation']
            if not response.meta['proxy'] in self.PROXY:
                self.PROXY.append(response.meta['proxy'])
                open('proxy.txt','a').write("\n"+response.meta['proxy'])
        except:
            Data=None
            yield scrapy.Request(response.meta['url'],callback=self.parse_data,dont_filter=True,headers=self.headers,cookies=self.cookies,meta={'ROW':ROW,'url':response.meta['url']})
        if Data:
            row=Data['vintage']
            item={}
            item['Winery']=row['wine']['winery']['name']
            item['Wine name']=row['wine']['name']
            item['Wine type']=response.xpath('//a[@data-cy="breadcrumb-winetype"]/text()').get().strip()
            Gras=row['wine']['grapes']
            Gap=[]
            for rs in Gras:
                Gap.append(rs['name'])
            item['Grapes']=", ".join(Gap)
            if len(Gras)==1:
                item['Grapes']="100% "+item['Grapes']
            item['Vintage']=row['year']
            item['Region']=row['wine']['region']['name']
            item['Country']=row['wine']['region']['country']['name']
            item['Tasting notes']=''
            try:
                item['Price']=Data['price']['amount']
            except:
                item['Price']=Data['prices_and_availability']['availability']['price']['amount']
            Tas=response.xpath('//table[contains(@class,"tasteStructure__tasteStructure--")]//tr')
            TAS=[]
            for rs in Tas:
                txt1=rs.xpath('./td[1]/div/text()').get()
                val=(str(rs.xpath('./td[2]/div/span/@style').get()).split(";")[-1]).replace("left:","")
                txt2=rs.xpath('./td[3]/div/text()').get()
                TAS.append(txt1+" - "+txt2+": "+val)
            item['Tasting notes']=', '.join(TAS)
            item['Tasting summary']=response.xpath('//div[@data-testid="average-of-reviews"]/text()').get()
            if item['Tasting summary']:
                item['Tasting summary']=str(item['Tasting summary']).strip()
            item['Aromas']={}
            try:
                data=Data['tastes']['flavor']
            except:
                data=None
            if data:
                for rs in data:
                    if 'primary_keywords' in rs:
                        item['Aromas'][str(rs['group']).replace("_"," ").title()]=[]
                        for rcs in rs['primary_keywords']:
                            item['Aromas'][str(rs['group']).replace("_"," ").title()].append(rcs['name'])
            item['Aromas']=str(item['Aromas'])
            item['url']=response.url
            yield(item)