from PyQt5 import QtWidgets,QtCore
from clientui import Ui_ExampleMessenger
import clientui
import requests
from datetime import datetime



class MessengerWindow(QtWidgets.QMainWindow,clientui.Ui_ExampleMessenger):
    def __init__(self):
        super(MessengerWindow,self).__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.sendMessage)
        self.create_user_button.pressed.connect(self.addUser)
        self.last_message_time = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getUpdates)
        self.timer.start(1000)

    def addUser(self):
        username = self.login.text()
        password = self.password.text()
        response = requests.post('http://127.0.0.1:5000/new_user',
            json={"username":username,"password":password})
        if response.json()['ok']:
            self.addText('Пользователь добавлен')
        else:
            self.addText('Такой пользователь существует')

    def sendMessage(self):
        username = self.login.text()
        password = self.password.text()
        message = self.message.toPlainText()
        if not username:
            self.addText('Не заполненно поле login')
            return
        if not password:
            self.addText('Не заполненно поле password')
            return
        if not message:
            self.addText('Не заполненно поле message')
            return
        response = requests.post('http://127.0.0.1:5000/send',
            json={"username":username,"password":password,"text":message})
        if not response.json()['ok']:
            self.addText('В доступе отказано')
        self.message.clear()
        self.message.repaint()

    def addText(self,text_error):
        self.textBrowser.append(text_error)
        self.textBrowser.repaint()

    def getUpdates(self):
        response = requests.get('http://127.0.0.1:5000/history', params={'after':self.last_message_time})
        data = response.json()
        for message in data['messages']:
            beauty_time = datetime.fromtimestamp(message['time'])
            beauty_time = beauty_time.strftime('%Y/%m/%d %H:%M:%S')
            self.addText(beauty_time + ' ' + message['username'])
            self.addText(message['text'])
            self.addText('')
            self.last_message_time = message['time']




app = QtWidgets.QApplication([])
window = MessengerWindow()
window.show()
app.exec_()
