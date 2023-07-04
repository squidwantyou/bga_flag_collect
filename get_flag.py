#!/usr/bin/env python
import sys,os
from bs4 import BeautifulSoup
import requests

tmp_id = "wRQA9BlBGgb4RI8"
tmp_tk = "q2OLFXoopyoudVAO5owuE8Pg3OHxFTqKLRXiEhWRmQxmiSNdtyh0dAyUH9jt96Pc"

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


country = dict()
for line in open("all.csv"):
    turl = f"https://boardgamearena.com/player?id=83898877"
    r = requests.get(turl,cookies=cookies, headers = headers )
    soup = BeautifulSoup(r.text, 'html.parser')

    a = soup.find_all(class_ = "flag")[0]
    print(a.parent.text.lstrip().strip())


