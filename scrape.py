import requests
from bs4 import BeautifulSoup
import time
import csv


#To avoid bot request most websites usually have scripts. Here we use this header to mimic our request as a browser.
header={'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

csv_file=open('scrape.csv','w')
csv_write=csv.writer(csv_file)
csv_write.writerow(['Stock Title','Current Price','Previous Close','Open','Bid','Ask',"Day's Range",'52 Week Range','Volume','Avg. Volume'])

urls=['https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.trsc=fin-srch','https://finance.yahoo.com/quote/JPM?p=JPM&.tsrc=fin-srch','https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch','https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch']
for url in urls:
    stock=[]
    html_page=requests.get(url,headers=header)
    #print(html_page.content)

    soup=BeautifulSoup(html_page.content,'lxml')  #lxml is a very fast and reliable parser
    #print(soup.title) or
    #print(soup.find('title').get_text())
    
    stock_title=soup.find_all('div',id='quote-header-info')[0].find('h1').get_text() #Static value retrieval
    current_price=soup.find_all('div',id='quote-header-info')[0].find('div',class_='My(6px) Pos(r) smartphone_Mt(6px)').find('span').get_text() #class is a keyword hence to extract the class value of a particular html tag we use class_
    # print(stock_title)
    # print(current_price)
    stock.append(stock_title)
    stock.append(current_price)
    
    table_info=soup.find_all('div',class_='D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')[0].find_all('tr')
    # print(table_info)

    for i in range(0,8):
        # heading=table_info[i].find_all('td')[0].get_text()
        value=table_info[i].find_all('td')[1].get_text()
        stock.append(value)
        # print(heading + ' : ' + value)
        
    csv_write.writerow(stock)
    time.sleep(5)

csv_file.close()