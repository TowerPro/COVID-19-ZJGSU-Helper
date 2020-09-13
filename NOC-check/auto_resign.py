#encoding=utf8
import json
import uuid
import re
import requests
import datetime

user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'

data = {
    'currentResd': '',
    'fromHbToZjDate': '',
    'fromHbToZj': 'C',
    'fromWtToHzDate': '',
    'fromWtToHz': 'B',
    'meetDate': '',
    'meetCase': 'C',
    'travelDate': '',
    'travelCase': 'D',
    'medObsvReason': '',
    'medObsv': 'B',
    'belowCaseDesc': '',
    'belowCase': 'D',
    'temperature': '',
    'notApplyReason': '',
    'hzQRCode': 'A',
    'specialDesc': ''
}

with open('data.json',encoding='utf-8') as f:
    users = json.load(f)
for user in users:
    ui = uuid.uuid1()
    data['uuid']=str(ui)
    data['currentResd']=user['home']
    header = {'User-Agent': user_agent}
    res = requests.post('https://nco.zjgsu.edu.cn/login', data=user, headers=header)
    cookieValue = ''
    for item in res.cookies:
        cookieValue += item.name + '=' + item.value + ';'
    cookieValue += ' _ncov_uuid=' + str(ui) + '; _ncov_username=' + user['name'] + '; _ncov_psswd=' + user['psswd']

    header = {'User-Agent': user_agent,
              'Cookie': cookieValue}

    res = requests.post('https://nco.zjgsu.edu.cn/', data=data, headers=header)
    print(datetime.datetime.now().strftime('%Y-%m-%d'), user['name'],'报送情况：',
          re.search('报送成功', str(res.content, encoding='utf-8')) is not None)
