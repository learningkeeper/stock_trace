# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup 
import re   
import subprocess

pattern = re.compile(r'^\d+\s+\D+$')
url1 = "http://isin.twse.com.tw/isin/C_public.jsp?strMode=" + str(2)
url2 = "http://isin.twse.com.tw/isin/C_public.jsp?strMode=" + str(4)
        
def crawler(url):
    res = requests.get(url)
    html = BeautifulSoup(res.text, "lxml")
    for entry in html.select('td'):
        result =re.findall(pattern, entry.text)
        if result:
            try:
                for i in result:
                    with open('/home/pi/tsec/stocknumber.txt', 'a+') as outfile:
                        my_cmd = 'echo' + " " + i + "\n"
                        subprocess.call(my_cmd, shell=True, stdout=outfile, stderr=subprocess.STDOUT)
            except Exception,e:
                print str(e)

open('stocknumber.txt', 'w').close()
crawler(url1)
crawler(url2)
