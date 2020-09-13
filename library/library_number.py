import requests
import pymysql
from bs4 import BeautifulSoup
import time
def getNum():
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36 Edg/85.0.564.51',
    }
    session = requests.Session()
    data = requests.get("http://libwx2.zjgsu.edu.cn:85/home/book/more/lib/11/type/4",headers=headers)
    data = data.text
    data = data.encode('ascii', 'ignore').decode('utf-8', 'ignore')
    soup = BeautifulSoup(data,'lxml')
    number = soup.find("div","col-xs-12 col-md-4").find('span').string
    return number

def Connect():
    db = pymysql.connect("ip","user","password","db")
    cursor = db.cursor()
    num = getNum()
    t = time.localtime()
    t = time.strftime("%H:%M:%S",t)
    sql = "insert into libnum(time,number)values('%s', '%s')"%(t,num)
    cursor.execute(sql)
    db.commit()
    db.close()
if "__main__" == __name__:
    while True:
        Connect()
        time.sleep(5)
