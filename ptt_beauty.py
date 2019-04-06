# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 16:04:48 2018

@author: linzino
"""
import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd 


rows = []

#迴圈開始
for i in range(2706,2695,-1):
    url = 'https://www.ptt.cc/bbs/Beauty/index'+ str(i)+'.html'
    resp = requests.get(url)  
    soup = BeautifulSoup(resp.text,'html.parser')
    
    ta1 = soup.find_all('div',re.compile('title'))
    for i in ta1:
        if len(i)!=1:
            print(i.a['href'])
   
            pre_url = 'https://www.ptt.cc'+str(i.a['href'])
            resp = requests.get(pre_url)  
            soup = BeautifulSoup(resp.text,'html.parser')
            ta2 = soup.find_all('span',re.compile('article-meta-value'))
            for j in ta2:
                if len(j)!=1:
                    print(ta2[3].text)
                    print(ta2[0].text)
                    print(ta2[1].text)
                    print(ta2[2].text)
            
        
            tmp = {'時間':ta2[3].text,
                   '作者':ta2[0].text,
                   '看板':ta2[1].text,
                   '標題':ta2[2].text}
           
            rows.append(tmp)
                       
            df = pd.DataFrame(rows)
            df.to_excel('ptt200.xls')