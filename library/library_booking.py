#encoding=utf-8
import re
import requests
import time
from aip import AipOcr
import datetime
import smtplib
from email.mime.text import MIMEText
import pymysql

LB_HOST = "http://libwx2.zjgsu.edu.cn:85"
WEB_URI = LB_HOST + "/home/book/more/lib/11/type/4"
LOGIN_URI = LB_HOST + "/api.php/login"
CAPTCHA_URI = LB_HOST + "/api.php/check"
BOOKING_URI = LB_HOST + "/api.php/activities/%s/application2?mobile=%s"

APP_ID = "baidu-aip-id""
APP_KEY = "baidu-aip-key"
APP_SECRET_KEY = "baidu-aip-secret-key"

replace_table = {
    "o": 0, "O": 0, "。": 0,
    "I": 1, "l": 1,
    "z": 2, "Z": 2,
    "A": 4,
    "s": 5, "S": 5, "与": 5,
    "G": 6, "b": 6,
    ">": 7,
    "e": 8,
    "q": 9,
}

client = AipOcr(APP_ID,APP_KEY,APP_SECRET_KEY)

def recognize_captcha(session):
    retry_time = 5
    captcha = ''
    recognized = False

    while retry_time:
        retry_time -= 1
        time.sleep(1)
        recognized = True

        try:
            with session.get(CAPTCHA_URI,headers={"Referer":WEB_URI}) as r:
                image = r.content

            result = client.basicGeneral(image,{})
            result = result['words_result'][0]["words"]
        except Exception:
            result = ""

        if len(result)!=4:
            recognized = False
            continue

        captcha = ''
        for digit in result:
            if digit in "1234567890":
                captcha += digit
            elif digit in replace_table:
                captcha += str(replace_table[digit])
            else:
                recognized = False
                continue

        break

    if not recognized:
        print("one more time")

    return captcha

def sendEmal(message,name,to_addr):
    msg = MIMEText(message, 'plain', 'utf-8')
    from_addr = 'mail@qq.com'
    password = 'plqigufjgfvubcda'
    smtp_server = 'smtp.qq.com'
    msg['From'] = "Library_booking"
    msg['To'] = name
    msg['Subject'] = 'library booking result'
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def book(date,student_id,password,phone,mail_address):
    session = requests.Session()
    retry_time = 3
    while retry_time:
        retry_time -= 1

        try:
            captcha = recognize_captcha(session)
        except:
            print("captcha error")
        data={'username':student_id,'password':password,'verify':captcha}
        with session.post(LOGIN_URI,data=data,headers={"Referer":WEB_URI}) as r:
            result = r.json()

        break

    with session.get(get_date_url(date)) as r:
        html = r.content.decode()
    act_id = re.search(
             '<a href="/book/notice/act_id/(\d+)/type/4/lib/11">', html, flags=re.S).group(1)
    with session.get(BOOKING_URI % (act_id,phone)) as r:
        result = r.json()
    if result['msg'] == '申请成功':
        words = "今天是"+date+",图书馆预约成功，今天又是美好的一天！"
    else:
        words = "今天是"+date+"图书馆预约失败，请自行预约。"
    sendEmal(words,name=student_id,to_addr=mail_address)


def get_date_url(date):
    return WEB_URI + '/day/' + str(date)

def Connect(time):
    db = pymysql.connect("ip","user","password","db")
    cursor = db.cursor()
    cursor.execute("select * from libraryBooking;")
    data = cursor.fetchall()
    for i in range(len(data)):
        book(time,data[i][0],data[i][1],data[i][2],data[i][3])
    db.close()

if "__main__" == __name__:
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    Connect(time)
