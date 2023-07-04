#!/usr/bin/env python
import sys,os
import requests
import json

from common import *

input_file = "player_name.list"
output_file = "player_id.list"

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

with open(output_file,'w') as ofp:
    for line in open(input_file):
        query_name = line.strip()
        url = f"https://boardgamearena.com/omnibar/omnibar/search.html?query={query_name}"
        r = requests.get(url,cookies=cookies, headers = headers )
        tmp = json.loads(r.text)
        for a in tmp['data']['players']:
            if a['fullname'] == query_name:
                ofp.write(f"{a['fullname']} {a['id']}\n")


