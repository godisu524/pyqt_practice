import datetime
import requests
APIKEY="3DMEEZ8ESFM4TlxSbLKB9EqfQpJZt1xw"
now = datetime.date.today()
now = str(now)
now=now.replace("-","")
URL = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey="+APIKEY+"&searchdate="+now+"&data=AP01"


r = requests.get(url = URL)

countries= r.text.split("},")

#singapore = -3
temp_singapore = countries[-3].split("ttb\":\"")[1]
singapore=""
for let in temp_singapore:
    if let !="\"":
        singapore+=let
    else:
        break

#malezia = -8
temp_malezia = countries[-8].split("ttb\":\"")[1]
malezia=""
for let in temp_malezia:
    if let !="\"":
        malezia+=let
    else:
        break

#taeguk = -2
temp_taeguk = countries[-2].split("ttb\":\"")[1]
taeguk=""
for let in temp_taeguk:
    if let !="\"":
        taeguk+=let
    else:
        break
#hongkong = 10
temp_hongkong = countries[10].split("ttb\":\"")[1]
hongkong=""
for let in temp_hongkong:
    if let !="\"":
        hongkong+=let
    else:
        break

#daeman = ?
#vietnam = ?
#philiphine = ?



won = int(input("원을 입력하세요: "))
print("싱가포르 : "+str(round(float(won)/float(singapore),3))) 
print("말레이시아 : "+str(round(float(won)/float(malezia),3)))
print("태국 : "+str(round(float(won)/float(taeguk),3)))
print("홍콩 : "+str(round(float(won)/float(hongkong),3)))


    
