#!/usr/bin/env python
import sys,os
from bs4 import BeautifulSoup
import requests

from common import *

cookies = requests.cookies.RequestsCookieJar()
cookies.set("TournoiEnLigneid",tmp_id)
cookies.set("TournoiEnLignetk",tmp_tk)

headers =  {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,lb;q=0.5",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-request-token": tmp_id,
    "x-requested-with": "XMLHttpRequest",
    "referrer": "https://boardgamearena.com",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "body": "",
    "method": "GET",
    "mode": "cors",
    "credentials": "include",
}

if not os.path.isdir("Player_Flag"):
    os.mkdir("Player_Flag")


country = dict()
for line in open("all.csv"):
    items = line.strip().split("\t")
    oppo_id = items[3]

    if os.path.isfile(f"Player_Flag/{oppo_id}"):
        continue
    try:
        turl = f"https://boardgamearena.com/player?id={oppo_id}"
        print(turl)
        #sys.exit()
        r = requests.get(turl,cookies=cookies, headers = headers )
#        print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')

        a = soup.find_all(class_ = "bga-flag")[0]
        flag = a.parent.text.lstrip().strip()
    except Exception as e:
        print(e)
        flag = "ERROR"

    with open(f"Player_Flag/{oppo_id}",'w') as ofp:
        ofp.write(flag)
        ofp.write("\n")
    print( items[1], oppo_id, flag )



