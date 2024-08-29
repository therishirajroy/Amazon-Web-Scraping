from bs4 import BeautifulSoup
import requests
import time
import datetime
import pandas as pd
import smtplib

def check_price():
    URL = 'https://www.amazon.in/IDEAL-HANDICRAFTS-Chesterfield-Blue-TWO_SEATER/dp/B0CZ4M6NF9/?_encoding=UTF8&pd_rd_w=oxnif&content-id=amzn1.sym.3c2b84ed-45d0-4019-a3c4-1242ac7f4d23&pf_rd_p=3c2b84ed-45d0-4019-a3c4-1242ac7f4d23&pf_rd_r=QA7AX9XDAARN2V160NFY&pd_rd_wg=geuT4&pd_rd_r=e795b473-eb51-4b17-8ff2-d3f65a5e5ef2&ref_=pd_hp_d_btf_ls_gwc_pc_en2_'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='apex_offerDisplay_desktop').get_text()

    price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

while(True):
    check_price()
    time.sleep(86400)