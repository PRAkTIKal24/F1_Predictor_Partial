from selenium import webdriver
from time import sleep
import requests
import lxml.html as lh
import pandas as pd




class F1Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def getTable_to_csv(self):
        url = self.url
        page = requests.get(url)
        doc = lh.fromstring(page.content)
        tr_elements = doc.xpath('//tr')
        
        col=[]
        i=0
        
        for t in tr_elements[0]:
            i+=1
            name=t.text_content()
            print('%d:"%s"'%(i,name))
            col.append((name,[]))

        for j in range(1,len(tr_elements)):
            T=tr_elements[j]
            
            if len(T)!=8:
                break
            
            i=0
            for t in T.iterchildren():
                data=t.text_content() 
                if i>0:
                    try:
                        data=int(data)
                    except:
                        pass
                col[i][1].append(data)
                i+=1

        Dict={title:column for (title,column) in col}
        df=pd.DataFrame(Dict)
        print(df.head())

        out_name = 'Res_'+self.name+'.csv'

        df.to_csv (out_name, index = False, header=True)          

    def login(self):
        self.driver.get('https://www.formula1.com/en/results.html/2019/races.html')

        sleep(2)

        cookie_btn = self.driver.find_element_by_xpath('//*[@id="truste-consent-button"]')
        cookie_btn.click()

        sleep(2)

        pop_btn = self.driver.find_element_by_xpath('//*[@id="sailthru-overlay-container"]/div/div[1]/button')
        pop_btn.click()

        aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/a')
        aus_btn.click()

        self.url = self.driver.current_url
        self.name = 'aus'

        self.getTable_to_csv()

        # bah_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[3]/a/span')
        # bah_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1001/bahrain/race-result.html'
        self.name = 'bah'

        self.getTable_to_csv()

        # chi_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[4]/a')
        # chi_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1002/china/race-result.html'
        self.name = 'chi'

        self.getTable_to_csv()

        # bak_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[5]/a/span')
        # bak_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1003/azerbaijan/race-result.html'
        self.name = 'bak'

        self.getTable_to_csv()

        # cat_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[6]/a/span')
        # cat_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1004/spain/race-result.html'
        self.name = 'cat'

        self.getTable_to_csv()

        # mon_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[7]/a/span')
        # mon_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1005/monaco/race-result.html'
        self.name = 'mon'

        self.getTable_to_csv()

        # can_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[8]/a/span')
        # can_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1006/canada/race-result.html'
        self.name = 'can'

        self.getTable_to_csv()

        # fra_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[9]/a/span')
        # fra_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1007/france/race-result.html'
        self.name = 'fra'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[10]/a/span')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1008/austria/race-result.html'
        self.name = 'aus'

        self.getTable_to_csv()

        # uk_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[11]/a/span')
        # uk_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1009/great-britain/race-result.html'
        self.name = 'uk'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[12]/a/span')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1010/germany/race-result.html'
        self.name = 'ger'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[13]/a/span')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1011/hungary/race-result.html'
        self.name = 'hun'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[14]/a/span')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1012/belgium/race-result.html'
        self.name = 'spa'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[15]/a/span')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1013/italy/race-result.html'
        self.name = 'ita'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[16]/a/span')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1014/singapore/race-result.html'
        self.name = 'sin'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[17]/a/span')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1015/russia/race-result.html'
        self.name = 'rus'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[18]/a/span')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1016/japan/race-result.html'
        self.name = 'jap'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[19]/a/span')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1017/mexico/race-result.html'
        self.name = 'mex'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[20]/a/span')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1018/united-states/race-result.html'
        self.name = 'usa'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[21]/a/span')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1019/brazil/race-result.html'
        self.name = 'bra'

        self.getTable_to_csv()

        # aus_btn = self.driver.find_element_by_xpath('/html/body/div[2]/main/article/div/div[2]/div[1]/div[3]/ul/li[22]/a')
        # aus_btn.click()

        self.url = 'https://www.formula1.com/en/results.html/2019/races/1020/abu-dhabi/race-result.html'
        self.name = 'abu'

        self.getTable_to_csv()




bot = F1Bot()
bot.login()