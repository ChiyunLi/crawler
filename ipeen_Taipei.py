#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:16:36 2018
@author: rikigei
"""
import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd 

rows=[['店名','電話','地址','營業時間','評價']]  #先設定一個list

key_word = '咖啡'
place = '台北'
start = 1
pages = 20  #控制頁數

for i in range(1,pages+1):
    url = 'http://www.ipeen.com.tw/search/all/000/1-0-0-0/'+key_word+'/?p='+str(i)+'&adkw='+place
    resp = requests.get(url)  
    resp.encoding='utf-8'
    soup = BeautifulSoup(resp.text,'html.parser') 
    list1 = soup.find_all('article', {'class':'serItem'})  
    
    for ii in list1:
        try:
            if len(ii)!=1:
                print(ii.a['href'])   #先抓到所有超連結
                
                #然後是一篇文章的
                pre_url = 'http://www.ipeen.com.tw'+str(ii.a['href'])
                resp = requests.get(pre_url, verify=False)
                resp.encoding='utf-8'
                soup = BeautifulSoup(resp.text,'html.parser')
                
                #店名 
                lista = soup.find_all('div',{'class':'info'})
                a = lista[0].find_all('span')
                print(a[0].text)
                
                #電話
                listb = soup.find_all('div',{'class':'brief'})
                b = listb[0].find_all('p',{'class':'tel i'})
                print(b[0].text)
                
                #地址
                c = listb[0].find_all('p',{'class':'addr i'}) 
                print(c[0].text)
    
                #營業時間
                listc = soup.find_all('div',{'class':'businessHour-left'})
                d = listc[0].find_all('span')
                print(d[0].text)
                
                #評價
                listd = soup.find_all('span',{'class':'score-bar large'})
                for e in listd:
                    e1 = e.meter['value']
                    print(e1)
                
                tmp = [a[0].text,
                       b[0].text,
                       c[0].text,
                       d[0].text,
                       e1]
                
                rows.append(tmp)
        
        except Exception as err:
            print(err)  
             
        
#輸出至excel            
df = pd.DataFrame(rows, columns = rows.pop(0))
df.to_excel('Ipeen_Taipei_carol.xls')
            
            

