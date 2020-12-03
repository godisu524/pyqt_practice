#-*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout
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







    





class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setFixedSize(100,20)
        
        #self.te.setAcceptRichText(False)
        self.lbl2 = QLabel('싱가폴 환전금액')
        self.lbl3 = QLabel('싱가폴 환전금액')
        self.lbl4 = QLabel('싱가폴 환전금액')
        self.lbl5 = QLabel('싱가폴 환전금액')



        self.te.textChanged.connect(self.text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addWidget(self.lbl3)
        vbox.addWidget(self.lbl4)
        vbox.addWidget(self.lbl5)

        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('환율계산기 - 띵')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self):
        won = int(self.te.toPlainText())
        
        self.lbl2.setText("싱가포르 : "+str(round(float(won)/float(singapore),3))) 
        self.lbl3.setText("말레이시아 : "+str(round(float(won)/float(malezia),3)))
        self.lbl4.setText("태국 : "+str(round(float(won)/float(taeguk),3)))
        self.lbl5.setText("홍콩 : "+str(round(float(won)/float(hongkong),3)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    