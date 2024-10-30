import threading as th
import os
import gtts
import webbrowser
import audioplayer
import pywhatkit as pw
import wikipedia as wi
import requests as rq
import smtplib
import pyttsx3 as pt
from email.message import EmailMessage
import speech_recognition as sr
import datetime as dt
from googletrans import Translator
import pafy
from PyQt5 import QtCore, QtGui, QtWidgets
import vlchttp
import pyfirmata 


board = pyfirmata.Arduino()
pin11 = board.digital[7]
pin10 = board.digital[10]
pin9 = board.digital[9]
pin8 = board.digital[8]
pin5 = board.digital[5]
pin3 = board.digital[3]




pin11.mode  = pyfirmata.INPUT
pin10.mode = pyfirmata.INPUT
pin9.mode = pyfirmata.OUTPUT
pin8.mode = pyfirmata.OUTPUT
pin5.mode = pyfirmata.OUTPUT
pin3.mode = pyfirmata.OUTPUT
class Ui_Form(object):

    
    def setupUi(root, Form):
        Form.setObjectName("Form")
        Form.resize(413, 335)
        Form.setWindowIcon(QtGui.QIcon( "./logo.png"))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(413, 335))
        Form.setMaximumSize(QtCore.QSize(413, 335))
        global pushButton, label_3, textBrowser
        pushButton = QtWidgets.QPushButton(Form)
        pushButton.setGeometry(QtCore.QRect(5, 225, 91, 101))
        pushButton.setObjectName("pushButton")
        pushButton.clicked.connect(lambda: thr())
        pushButton_2 = QtWidgets.QPushButton(Form)
        pushButton_2.setGeometry(QtCore.QRect(315, 225, 91, 101))
        pushButton_2.setObjectName("pushButton_2")
        pushButton_2.clicked.connect(lambda: thkill())
        pushButton_3 = QtWidgets.QPushButton(Form)
        pushButton_3.setGeometry(QtCore.QRect(150, 285, 121, 41))
        pushButton_3.setObjectName("pushButton_3")
        pushButton_3.clicked.connect(lambda: main1())
        pushButton_4 = QtWidgets.QPushButton(Form)
        pushButton_4.setGeometry(QtCore.QRect(150, 225, 121, 44))
        pushButton_4.setObjectName("pushButton_4")
        pushButton_4.clicked.connect(lambda: main())
        root.label = QtWidgets.QLabel(Form)
        root.label.setGeometry(QtCore.QRect(0, 0, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        root.label.setFont(font)
        root.label.setAlignment(QtCore.Qt.AlignCenter)
        root.label.setObjectName("label")
        textBrowser = QtWidgets.QLabel(Form)
        textBrowser.setWordWrap(True)
        textBrowser.setGeometry(QtCore.QRect(1, 110, 411, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        textBrowser.setFont(font)
        textBrowser.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        textBrowser.setObjectName("textBrowser")
        root.label_2 = QtWidgets.QLabel(Form)
        root.label_2.setGeometry(QtCore.QRect(20, 56, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        root.label_2.setFont(font)
        root.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        root.label_2.setObjectName("label_2")
        label_3 = QtWidgets.QLabel(Form)
        label_3.setGeometry(QtCore.QRect(150, 56, 170, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        label_3.setFont(font)
        label_3.setAlignment(QtCore.Qt.AlignLeading |
                             QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        label_3.setObjectName("label_3")
        label_3.setText("ksjfd")
        pushButton.setText("Start")
        pushButton_2.setText("Stop")
        pushButton_3.setText("Show all commends(bn)")
        pushButton_4.setText("Show all commends(en)")
        root.label.setText("Welcome to Nova")
        root.label_2. setText("Status: ")
        label_3.setText("Stop")

 ######################bndilog##############################

        def main():
            root = QtWidgets.QDialog()
            root.setObjectName("root")
            root.resize(550, 250)
            root.setMinimumSize(QtCore.QSize(550, 250))
            root.setMaximumSize(QtCore.QSize(550, 250))
            root.label = QtWidgets.QLabel(root)
            root.label.setGeometry(QtCore.QRect(0, 0, 551, 41))
            font = QtGui.QFont()
            font.setPointSize(20)
            root.label.setFont(font)
            root.label.setAlignment(QtCore.Qt.AlignCenter)
            root.label.setObjectName("label")
            root.label_2 = QtWidgets.QLabel(root)
            root.label_2.setGeometry(QtCore.QRect(20, 40, 143, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_2.setFont(font)
            root.label_2.setObjectName("label_2")
            root.label_3 = QtWidgets.QLabel(root)
            root.label_3.setGeometry(QtCore.QRect(20, 60, 181, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_3.setFont(font)
            root.label_3.setObjectName("label_3")
            root.label_4 = QtWidgets.QLabel(root)
            root.label_4.setGeometry(QtCore.QRect(20, 80, 171, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_4.setFont(font)
            root.label_4.setObjectName("label_4")
            root.label_5 = QtWidgets.QLabel(root)
            root.label_5.setGeometry(QtCore.QRect(20, 100, 241, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_5.setFont(font)
            root.label_5.setObjectName("label_5")
            root.label_6 = QtWidgets.QLabel(root)
            root.label_6.setGeometry(QtCore.QRect(20, 184, 144, 18))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_6.setFont(font)
            root.label_6.setObjectName("label_6")
            root.label_7 = QtWidgets.QLabel(root)
            root.label_7.setGeometry(QtCore.QRect(20, 119, 143, 20))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_7.setFont(font)
            root.label_7.setObjectName("label_7")
            root.label_8 = QtWidgets.QLabel(root)
            root.label_8.setGeometry(QtCore.QRect(20, 140, 143, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_8.setFont(font)
            root.label_8.setObjectName("label_8")
            root.label_9 = QtWidgets.QLabel(root)
            root.label_9.setGeometry(QtCore.QRect(20, 162, 143, 18))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_9.setFont(font)
            root.label_9.setObjectName("label_9")
            root.label_10 = QtWidgets.QLabel(root)
            root.label_10.setGeometry(QtCore.QRect(20, 203, 143, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_10.setFont(font)
            root.label_10.setObjectName("label_10")
            root.label_11 = QtWidgets.QLabel(root)
            root.label_11.setGeometry(QtCore.QRect(20, 220, 143, 23))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_11.setFont(font)
            root.label_11.setObjectName("label_11")
            root.label_12 = QtWidgets.QLabel(root)
            root.label_12.setGeometry(QtCore.QRect(260, 201, 143, 18))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_12.setFont(font)
            root.label_12.setObjectName("label_12")
            root.label_13 = QtWidgets.QLabel(root)
            root.label_13.setGeometry(QtCore.QRect(260, 98, 143, 22))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_13.setFont(font)
            root.label_13.setObjectName("label_13")
            root.label_14 = QtWidgets.QLabel(root)
            root.label_14.setGeometry(QtCore.QRect(260, 178, 201, 19))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_14.setFont(font)
            root.label_14.setObjectName("label_14")
            root.label_15 = QtWidgets.QLabel(root)
            root.label_15.setGeometry(QtCore.QRect(260, 40, 291, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_15.setFont(font)
            root.label_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            root.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
            root.label_15.setFrameShadow(QtWidgets.QFrame.Plain)
            root.label_15.setObjectName("label_15")
            root.label_16 = QtWidgets.QLabel(root)
            root.label_16.setGeometry(QtCore.QRect(260, 215, 251, 31))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_16.setFont(font)
            root.label_16.setObjectName("label_16")
            root.label_17 = QtWidgets.QLabel(root)
            root.label_17.setGeometry(QtCore.QRect(260, 140, 201, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_17.setFont(font)
            root.label_17.setObjectName("label_17")
            root.label_18 = QtWidgets.QLabel(root)
            root.label_18.setGeometry(QtCore.QRect(260, 155, 201, 27))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_18.setFont(font)
            root.label_18.setObjectName("label_18")
            root.label_19 = QtWidgets.QLabel(root)
            root.label_19.setGeometry(QtCore.QRect(260, 120, 143, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_19.setFont(font)
            root.label_19.setObjectName("label_19")
            root.label_20 = QtWidgets.QLabel(root)
            root.label_20.setGeometry(QtCore.QRect(260, 60, 311, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_20.setFont(font)
            root.label_20.setObjectName("label_20")
            root.label_21 = QtWidgets.QLabel(root)
            root.label_21.setGeometry(QtCore.QRect(260, 80, 391, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_21.setFont(font)
            root.label_21.setObjectName("label_21")
            root.label.setText("সমস্ত প্রশংসা দেখান ( বাং)")
            root.label_2.setText("১.বর্তমান সময় বল")
            root.label_3.setText("২.বর্তমান আবহাওয়া বল")
            root.label_4.setText("৩.বর্তমান তাপমাত্রা বল")
            root.label_5.setText("৪.আনুবাদ কর( কিছু(  বাং থেকে ইং )) ")
            root.label_6.setText("৮.আজকে কি বার")
            root.label_7.setText("৫.তুমি কি কর")
            root.label_8.setText("৬.তোমার সম্পর্কে বল")
            root.label_9.setText("৭.আজকে কত তারিখ")
            root.label_10.setText("৯.এটা কি মাস")
            root.label_11.setText("১০.গান বাজাউ ( কিছু)")
            root.label_12.setText("১৯.মেইল পাঠাও")
            root.label_13.setText("১৪.( কিছু) সম্পর্কে বল")
            root.label_14.setText("১৮.( কিছু) অনুসন্ধান করুন")
            root.label_15.setText(
                "১১.গান্ চালাউ ( যদি ১০.নং প্রসঙ্গটি চালু থাকে)")
            root.label_16.setText("২০.খোল (গুগল , সফটওয়্যার ইত্যাদি)")
            root.label_17.setText("১৬.ইংরাজিতে সুইচ কর")
            root.label_18.setText("১৭.ইউটুবে ( কিছু) চালাও ")
            root.label_19.setText("১৫.বাংলাতে সুইচ কর")
            root.label_20.setText(
                "১২.গান্ বিরতি ( যদি ১০.নং প্রসঙ্গটি চালু থাকে)")
            root.label_21.setText(
                "১৩.গান্ বন্ধ ( যদি ১০.নং প্রসঙ্গটি চালু থাকে)")
            root.show()
            root.exec_()


# ==========================================================

        def main1():
            root = QtWidgets.QDialog()
            root.setObjectName("root")
            root.resize(550, 250)
            root.setMinimumSize(QtCore.QSize(550, 250))
            root.setMaximumSize(QtCore.QSize(550, 250))
            root.label = QtWidgets.QLabel(root)
            root.label.setGeometry(QtCore.QRect(0, 0, 551, 41))
            font = QtGui.QFont()
            font.setPointSize(20)
            root.label.setFont(font)
            root.label.setAlignment(QtCore.Qt.AlignCenter)
            root.label.setObjectName("label")
            root.label_2 = QtWidgets.QLabel(root)
            root.label_2.setGeometry(QtCore.QRect(20, 40, 143, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_2.setFont(font)
            root.label_2.setObjectName("label_2")
            root.label_3 = QtWidgets.QLabel(root)
            root.label_3.setGeometry(QtCore.QRect(20, 60, 181, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_3.setFont(font)
            root.label_3.setObjectName("label_3")
            root.label_4 = QtWidgets.QLabel(root)
            root.label_4.setGeometry(QtCore.QRect(20, 80, 171, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_4.setFont(font)
            root.label_4.setObjectName("label_4")
            root.label_5 = QtWidgets.QLabel(root)
            root.label_5.setGeometry(QtCore.QRect(20, 100, 241, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_5.setFont(font)
            root.label_5.setObjectName("label_5")
            root.label_6 = QtWidgets.QLabel(root)
            root.label_6.setGeometry(QtCore.QRect(20, 184, 144, 18))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_6.setFont(font)
            root.label_6.setObjectName("label_6")
            root.label_7 = QtWidgets.QLabel(root)
            root.label_7.setGeometry(QtCore.QRect(20, 119, 143, 20))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_7.setFont(font)
            root.label_7.setObjectName("label_7")
            root.label_8 = QtWidgets.QLabel(root)
            root.label_8.setGeometry(QtCore.QRect(20, 140, 143, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_8.setFont(font)
            root.label_8.setObjectName("label_8")
            root.label_9 = QtWidgets.QLabel(root)
            root.label_9.setGeometry(QtCore.QRect(20, 162, 143, 18))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_9.setFont(font)
            root.label_9.setObjectName("label_9")
            root.label_10 = QtWidgets.QLabel(root)
            root.label_10.setGeometry(QtCore.QRect(20, 203, 143, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_10.setFont(font)
            root.label_10.setObjectName("label_10")
            root.label_11 = QtWidgets.QLabel(root)
            root.label_11.setGeometry(QtCore.QRect(20, 220, 143, 23))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_11.setFont(font)
            root.label_11.setObjectName("label_11")
            root.label_12 = QtWidgets.QLabel(root)
            root.label_12.setGeometry(QtCore.QRect(260, 201, 143, 18))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_12.setFont(font)
            root.label_12.setObjectName("label_12")
            root.label_13 = QtWidgets.QLabel(root)
            root.label_13.setGeometry(QtCore.QRect(260, 98, 143, 22))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_13.setFont(font)
            root.label_13.setObjectName("label_13")
            root.label_14 = QtWidgets.QLabel(root)
            root.label_14.setGeometry(QtCore.QRect(260, 178, 201, 19))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_14.setFont(font)
            root.label_14.setObjectName("label_14")
            root.label_15 = QtWidgets.QLabel(root)
            root.label_15.setGeometry(QtCore.QRect(260, 40, 291, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_15.setFont(font)
            root.label_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            root.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
            root.label_15.setFrameShadow(QtWidgets.QFrame.Plain)
            root.label_15.setObjectName("label_15")
            root.label_16 = QtWidgets.QLabel(root)
            root.label_16.setGeometry(QtCore.QRect(260, 215, 251, 31))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_16.setFont(font)
            root.label_16.setObjectName("label_16")
            root.label_17 = QtWidgets.QLabel(root)
            root.label_17.setGeometry(QtCore.QRect(260, 140, 201, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_17.setFont(font)
            root.label_17.setObjectName("label_17")
            root.label_18 = QtWidgets.QLabel(root)
            root.label_18.setGeometry(QtCore.QRect(260, 155, 201, 27))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_18.setFont(font)
            root.label_18.setObjectName("label_18")
            root.label_19 = QtWidgets.QLabel(root)
            root.label_19.setGeometry(QtCore.QRect(260, 120, 143, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_19.setFont(font)
            root.label_19.setObjectName("label_19")
            root.label_20 = QtWidgets.QLabel(root)
            root.label_20.setGeometry(QtCore.QRect(260, 60, 311, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_20.setFont(font)
            root.label_20.setObjectName("label_20")
            root.label_21 = QtWidgets.QLabel(root)
            root.label_21.setGeometry(QtCore.QRect(260, 80, 391, 17))
            font = QtGui.QFont()
            font.setPointSize(11)
            root.label_21.setFont(font)
            root.label_21.setObjectName("label_21")
            root.label.setText("Show all commends(en)")
            root.label_2.setText("1.Tell the current time")
            root.label_3.setText("2.Tell the current weather")
            root.label_4.setText("3.Tell the current temperaturer")
            root.label_5.setText("4.translate (somethimg(en))")
            root.label_6.setText("8.What are you doing")
            root.label_7.setText("5.Tell me about you")
            root.label_8.setText("6.What time is it today")
            root.label_9.setText("7.What a date today")
            root.label_10.setText("9.Switch to bangla")
            root.label_11.setText("10.pause song (if 18.NO comand are runing)")
            root.label_12.setText("19.What month is it now")
            root.label_13.setText("14.Swiftch to english")
            root.label_14.setText("18.Play music (something)")
            root.label_15.setText("11.Tell me about (something)")
            root.label_16.setText("20.Stop song (if 18.NO comand are runing)")
            root.label_17.setText("16.Play song (if 18.NO comand are runing)")
            root.label_18.setText("17.Search (something)")
            root.label_19.setText("15.Send mail")
            root.label_20.setText("12.Play youtube (something)")
            root.label_21.setText("13.Open(like softwer,  google, anywebsite)")
            root.show()
            root.exec_()
        global langus, imlangus
        langus = 'en-IN'
        imlangus = 'bn'

      


     

      
        global condit
        condit = True

        def command():
            global condit
            r = sr.Recognizer()
            try:
                with sr.Microphone() as sucrce:
                    r.adjust_for_ambient_noise(sucrce)
                   
                    r.pause_threshold = 0.5
                    if condit:
                        speech("i am Listening")
                    
                    label_3.setText("Listening...")
                    audio = r.listen(sucrce)
                    
                    label_3.setText("Processing...")
                    commends = r.recognize_google(
                        audio_data=audio, language=langus)
                    commends = str(commends).lower()
                    return commends
            except Exception as e:
                pass

        def mailsub():
            sub = command()
            textBrowser.setText(sub)
            speech(f'your email subject is {sub}. is that right')
            issub = command()
            textBrowser.setText(issub)
            return [sub, issub]

        def mailmess():
            mail = command()
            textBrowser.setText(mail)
            speech(f'your email message is {mail}. is that right')
            ismail = command()
            textBrowser.setText(ismail)
            return [mail, ismail]

        def mailto():
            to = command()
            textBrowser.setText(to)
            speech(f'your email to address is {to}. is that right')
            isto = command()
            textBrowser.setText(isto)
            return [to, isto]

        def mail(fro, to, message, sub, passw):
            mes = EmailMessage()
            mes['subject'] = sub
            mes['to'] = to
            mes['from'] = fro
            mes.set_content(message)
            asr = smtplib.SMTP('smtp.gmail.com', 587)
            asr.starttls()
            asr.login(fro, passw)
            asr.sendmail(to_addrs=to, from_addr=fro, msg=mes.as_string())
            speech('your email send succesfully')

        global cond, a, welcome
        contuctmail = {'nova': 'rifatmondol1235@gmail.com'}
        a = ''

        def welcome():
            speech("Hi, i am nova. welcome to our app")
            time = int(dt.datetime.now().strftime('%H'))

            if 0 <= time <= 12:
                speech("Good morning, sir")

            elif 13 <= time <= 16:
                speech("Good afternoon, sir")

            elif 17 <= time <= 19:
                speech("Good evening, sir")
            elif 20 <= time <= 24:
                speech("Good night, sir")
            speech("how can i help you")

        cond = False

        def thkill():
            global cond
            cond = True
            label_3.setText("Stoping")

        def mainfunc():
            global condit, cond, textBrowser
            while True:
                try:
                    if cond:
                        cond = False
                        label_3.setText("Stoped")
                        break
                    label_3.setText("Runing...")
                    t = command()
                    if t == None:
                        condit = False
                        textBrowser.setText("None")

                        continue
                    condit = True
                    textBrowser.setText(t)
                    if langus == 'bn-BD':
                        t = translateall(text=t, lan='en').text
                        t = str(t).lower()
                    t = t.replace("-", " ")

                    weather = rq.get(
                        url='https://api.openweathermap.org/data/2.5/weather?q=rajshahi&appid=af1bdf3712cd947157d347f53a794631')
                    allweather = weather.json()

                    if 'translate' in t:
                        if langus == 'bn-BD':
                            t = translateall(text=t, lan='bn').text
                            filteryou = t.replace('অনুবাদ করুন', '')
                            global a
                            a = 'english'
                        else:
                            filteryou = t.replace('translate', '')
                            a = 'bangla'
                        try:
                            speech(
                                f'ok. i am translateing {filteryou} to {a}. please wait')
                            translator = Translator()
                            te = translator.translate(filteryou, dest=imlangus)
                            speechbn(te.text, imlangus)
                        except Exception as s:
                            speech('i am fail . please try again')

                    elif t == "stop":
                        break

                    elif 'is the time' in t or 'current time' in t:
                        time = dt.datetime.now().strftime('%I:%M %p')
                        speech(f'current time Is {time}')

                    elif 'doing' in t or t in "do":
                        speech("I am listen your commend")

                    elif 'about you' in t:
                        speech(
                            "My name is nova. I was born in 09/04/2022. I was developed by Md. Rifat")

                    elif 'date' in t:
                        date = dt.datetime.now().strftime('%d day %m month %Y year')
                        speech(f'today date Is {date}')

                    elif 'today' in t:
                        day = dt.datetime.now().strftime('%A')
                        speech(f'today Is {day}')

                    elif 'month' in t or t in "what is it":
                        month = dt.datetime.now().strftime('%B')
                        speech(f'this month Is {month}')

                    elif 'play music' in t:
                        filteryou = t.replace('play music', '')
                        try:
                            
                            url = pw.playonyt(filteryou, open_video=False)
                            video = pafy.new(url)
                            best = video.getbestaudio()
                            playurl = best.url
                            global player
                            player = vlchttp.MediaPlayer(playurl)
                            speech(f"ok i am playing {filteryou} on youtube")
                            player.play()

                        except Exception as e:
                            os.startfile(os.getcwd() + "\\vlc.exe")
                            continue

                    elif 'play song' == t:

                        player.play()
                    elif 'pause song' == t:
                        player.pause()

                    elif 'stop song' == t:
                        player.stop()

                    elif 'tell me about' in t:
                        filterwi = t.replace('tell me about', '')
                        speech(f'ok. i am searching {filterwi}. please wait')
                        try:
                            wp = wi.summary(filterwi, sentences=10)
                            speech(wp)
                        except Exception as e:
                            speech(
                                'i am fail . please try again'
                            )

                    elif "switch to" in t:
                        filte = t.replace("switch to ", "")
                        if filte in "bangla":
                            if langus == 'en-IN':
                                langbn()
                                speech("ঠিক আছে । আমি বাংলাতে সুইচ করেছি")
                        elif filte in "english":
                            if langus == 'bn-BD':

                                langen()
                                speech("ok. i am switch to english")

                    elif 'play youtube' in t:
                        filteryou = t.replace('play youtube', '')
                        try:
                            speech(
                                f'ok. i am playing {filteryou}. please wait')
                            pw.playonyt(filteryou, open_video=True)
                        except:
                            speech('i am fail . please try again')
                    elif 'search' in t:
                        filteryou = t.replace('search', '')
                        try:
                            speech(
                                f'ok. i am searching {filteryou}. please wait')
                            pw.search(filteryou)
                        except:
                            speech('i am fail . please try again')
                    elif 'current weather' in t:
                        try:
                            wp = allweather['weather'][0]['main']
                            speech(f'current weather is {wp}')
                        except:
                            speech(
                                'i am fail . please try again'
                            )
                    elif "stop first machine" in t or "stop fast machine" in t:
                       
                        pin8.write(0)
                        pin9.write(1)
                       
                    elif "stop second machine" in t:
                           
                       
                  
                        pin8.write(1)
                        pin9.write(0)
                        
                    elif "start first machine" in t or "start fast machine" in t :
                                
                        pin8.write(1)
                        pin9.write(0)
                    elif "start second machine" in t:
                                    
                       pin8.write(0)
                       pin9.write(1)

                    elif "start both machine" in t or "start book making" in t:
                                                        
                        pin8.write(0)
                        pin9.write(0)

                    elif "stop both machine" in t:
                                                                            
                         pin8.write(1)
                         pin9.write(1)

                    elif 'current temperature' in t:
                        try:
                            wp = int(int(allweather['main']['temp']) - 273.15)
                            speech(f'current weather is {wp}℃')
                        except:
                            speech(
                                'i am fail . please try again'
                            )
                    elif 'open' in t:
                        filte = t.replace('open ', '').replace(" ", '')
                        if filte in "code":
                            os.system("code")

                        elif filte in 'daraz':
                            webbrowser.open("www.daraz.com.bd")

                        else:
                            webbrowser.open(f"www.{filte}.com")

                    elif 'send mail' in t:
                        speech('ok. please answer my qustions')
                        speech('say your email subject')
                        try:
                            while True:
                                sub = mailsub()
                                if sub[1] == 'yes':
                                    speech('say your email message')
                                    while True:
                                        mails = mailmess()
                                        if mails[1] == 'yes':
                                            speech('say your email to address')
                                            while True:
                                                to = mailto()
                                                if to[1] == 'yes':
                                                    try:
                                                        mail(
                                                            '', to=contuctmail[to[0]], message=mails[0],
                                                            sub=sub[0], passw='')
                                                    except Exception as e:
                                                        pass

                                                    break

                                                else:
                                                    speech(
                                                        'please say again your email to address')
                                            break
                                        else:
                                            speech(
                                                'please say again your email message')
                                    break
                                else:
                                    speech('please say again email subject')

                        except Exception as e:
                            speech(
                                'i am fail . please try again'
                            )
                except Exception as e:
                    continue

        def thr():
            global th1
            th1 = th.Thread(target=lambda: mainfunc())
            th1.start()
def speechbn(text, lan):
            tt = gtts.gTTS(text=text, lang=lan)
            tt.save('save.mp3')
            audioplayer.AudioPlayer('save.mp3').play(block=True)
            os.remove('save.mp3')
def translateall(text, lan):
            trans = Translator().translate(text=text, dest=lan)
            return trans
def speech(text):
            if langus == 'bn-BD':
                t = translateall(text=text, lan='bn').text
                speechbn(text=t, lan='bn')
            else:
                try:
                
                    main = pt.init()
                
            
                    voice = main.getProperty('voices')
                    main.setProperty('voice', voice[0].id)
                    main.setProperty('rate', 125)
                    main.say(text)
                    main.runAndWait()
                except Exception as e:
                    pass
def langbn():
            global langus, imlangus
            langus = 'bn-BD'
            imlangus = 'en' 

def langen():
            global langus, imlangus
            langus = 'en-IN'
            imlangus = 'bn' 
if __name__ == "__main__":
    def buzzerTimer(t , i):
           for i in range(i): 
                pin3.write(1)
                import time
                time.sleep(t)
                pin3.write(0)
                time.sleep(t)




    def sensormotion():
        prevmoSensor = int(pin11.read())
        pin3.write(0)
        while True:
            import time
            time.sleep(0.01)
            motionstatus = int(pin11.read())
            print(motionstatus)
            
            if prevmoSensor != motionstatus:
                prevmoSensor = motionstatus
                print(motionstatus)
                if motionstatus == 1 :
                    speech("Please be alart Don't get too closer to the machine")
                    import threading
                    buzzerTimer(0.5 , 5)
                    
                  
                  
    


    def sensorIR():
          pin8.write(0)
          pin9.write(0)
          speech("starting 1st machine")
          pin8.write(1)
          pin9.write(0)
          previousIR = int( pin10.read())
          import threading
          thre = th.Thread( target= lambda:buzzerTimer(0.1 , 100))
          while True:     
                import time
                time.sleep(0.01)
                irState =int( pin10.read())
                if previousIR != irState:

                    previousIR = irState

                    if irState == 1 :
                      
                        speech("starting 1st machine")
                        pin8.write(1)
                        pin9.write(0)
                    elif irState == 0 :
                        pin8.write(1)
                        pin9.write(1)
                        speech("starting 2nd machine")
                        pin9.write(1)
                        pin8.write(0)
                        
                        


    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
   
    UTI  = pyfirmata.util.Iterator(board)
    UTI.start()
    Form.show()
    # langbn()
    # speech("আসসালামুআলাইকুমওয়ারাহমাতুল্লাহিওয়াবারাকাতুহ")
    langen()
    speech("welcom to our ai based smart industry")
    th1 = th.Thread(target=lambda:sensormotion())
    th1.start()
    th2 = th.Thread(target=lambda:sensorIR())
    th2.start()  
    
    app.exec_()
    os._exit(0)
