from flask import Flask, request
from datetime import datetime
import time
from database import *

app = Flask(__name__)

@app.route("/new_user", methods=['POST'])
def new_user():
    """
    request:{'username':"str",'password':"str"}
    response:{"ok":True}
    """
    data = request.json
    username = data['username']
    password = data['password']
    if is_unique(username):
        add_user(username,password)
        return {"ok":True}


@app.route("/send", methods=['POST'])
def send():
    """
    request:{"username":"str","password":"str","text":"str"}
    response:{"ok":true}
    """
    data = request.json
    username = data['username']
    password = data['password']
    text = data['text']
    if authorization(username,password):
        send_message(username,text)
        return {"ok":True}
    else:
        return {"ok":False}

@app.route("/history")
def history():
    """
    request: ?after=16515151151.45
    response: {
        'messages':{
             {"username":"str","text":"str","time":float}
        }
    }
    """
    after = float(request.args['after'])
    filtered_messages = []
    for message in get_messages_after(after):
        if after < message[2]:
            filtered_messages.append({'username':message[0],'text':message[1],'time':message[2]})
    return {'messages':filtered_messages}

app.run()
