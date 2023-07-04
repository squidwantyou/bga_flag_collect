#!/usr/bin/env python
import sys,os
import requests
import json


input_file = "player_id.list"

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

for line in open(input_file):
    p_id = int(line.split()[-1] )
    os.system(f"mkdir games_data/{p_id}")
    
    i = 1
    while True:
        if i == 1:
            j = 1
        else :
            j = 0
        turl = f"https://boardgamearena.com/gamestats/gamestats/getGames.html?player={p_id}&opponent_id=0&game_id=30&start_date=1688227200&finished=0&page={i}&updateStats={j}"
        r = requests.get(turl,cookies=cookies, headers = headers )
        tmp = json.loads(r.text)


        if len(tmp['data']['tables'] ) == 0:
            break
        else:
            with open(f"games_data/{p_id}/{i}.json",'w') as ofp:
                ofp.write(r.text)

        if i == 100:
            break
        i += 1
    
