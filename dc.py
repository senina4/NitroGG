import requests
import json
import time, random
headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
}

json_data = {
    'partnerUserId': 'c2175c1985c3d6a935533be81a2bd939ac1db22651be3187420cb65e2bea1c18',
}
ts = "https://discord.com/billing/partner-promotions/1180231712274387115/"
f = open('output.txt', 'a')
times = 1
while True:
    response = requests.post('https://api.discord.gx.games/v1/direct-fulfillment', headers=headers, json=json_data)
    print(f"Time: {times}")
    if response.status_code == 200:
        tk= json.loads(response.text)
        ass = ts + tk['token']
        f.write(ass + "\n")
        print(ass)
    else:
        print(f"Fail: {response.status_code}")
        time.sleep(3)
    times += 1