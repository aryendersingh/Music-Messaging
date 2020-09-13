
from flask import Flask
from twilio.rest import Client

app = Flask(__name__)


@app.route('/')
def send_message():
    account_sid = ""
    auth_token = ""

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="", 
        from_="",
        body="Hello from Music Messaging! \n What kinda music you into, Pop, Rock, Classical or Rap!?")

    return message.sid



if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=8080, debug=True)

