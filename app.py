from flask import Flask
from flask import request
from twilio.rest import Client
import os
from marketstack import get_stock_price
app =Flask(__name__)

ACCOUNT_ID= os.environ.get("TWILIO_ACCOUNT")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
client = Client(ACCOUNT_ID, TWILIO_TOKEN)
TWILIO_NUMBER ="whatsapp:+14155238886"

def process_msg(msg):
    response =""
    if msg=="Hi":
        response = "HELLO , Welcome to the Khote's Stock Market BOT!"
        response += "\n Type Sym:<stock_symbol> to know the price of Stock "
    elif 'Sym:' in msg:
        data= msg.split(":")
        stock_symbol=  data[1]
        stock_price = get_stock_price(stock_symbol)
        last_price= stock_price['last_price']
        last_price_str= str(last_price)
        response= "The stock price of "+ stock_symbol + " is : $"+ last_price_str
    else:
        response ="Plzzz type Hi to get started"
    return response

def send_msg(msg,recipient):
    client.messages.create(
        from_= TWILIO_NUMBER, 
        body= msg,
        to= recipient
    )
@app.route("/")
def hello():
    return{"Result":" you successfully created first route"}

@app.route("/webhook", methods=["POST"])
def webhook():
    f= request.form
    msg =f['Body']
    sender =f['From']
    response = process_msg(msg)
    send_msg(response,sender)
    return "OK" ,200


#set TWILIO_ACCOUNT=AC9dd70848d2c912098df523050524a137
#set TWILIO_TOKEN=f1bf94c2d4b286147ebc79271235abea    