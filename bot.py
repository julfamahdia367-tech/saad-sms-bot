import telebot
from telebot import types
import requests
from flask import Flask
from threading import Thread

# আপনার টোকেন এবং এপিআই কি এখানে বসান
API_TOKEN = '8574927098:AAGXeQdA8VNU2lM8Bh4fqjHWSMBbJVkmn7s' 
FIVE_SIM_API_KEY = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE4MDY1NTk1MjQsImlhdCI6MTc3NTAyMzUyNCwicmF5IjoiMDYxNjc1Mzc2MTFmYzRmOTA5NzNiMWQxYjM3ZmFhMDAiLCJzdWIiOjM5MjczNTV9.aTTdwcqYSpUFe-RQBVKuzPUOuU1hzF1GVF9t2-AVh_ixyGc5mldXdUvpmC5FwSBvnViznqJRbyPViq4UvvVoKIy1CkNTlZFaeBSlanZncGhoK0nRvaCHS2BGO9cGDT5PxeCegt9VF7iE3WcmHN7Z1G-ZfOptuPgnSujbZdXK_gQUdas81fZzEoPZn-vn9903FsJD9oO_qEuBN7C6XVMZR9hSpzet3j5w587Wzq7PTymwCqo0GmwqgMORS0fImGkfEBXZgtrH6HJDxzounVZh-CLW3Od1k0olV375uOywfFTQ5I7UDJUpFDiXpfZpFJKwFYkFd12lxU6j5bzXNILjAQ'

bot = telebot.TeleBot(API_TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Bot is Alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(types.KeyboardButton('📲 Get Number'), types.KeyboardButton('💰 Balance'))
    markup.row(types.KeyboardButton('👥 Refer & Earn'), types.KeyboardButton('💬 Support'))
    markup.row(types.KeyboardButton('📊 Status'))
    bot.send_message(message.chat.id, "⚡ **Welcome to Saad SMS Pro** ⚡", reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == '💬 Support')
def support(message):
    # আপনার ইউজারনেমটি এখানে দিন (@ ছাড়া)
    url = "SaadsmsproBot" 
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Contact Admin", url=url))
    bot.send_message(message.chat.id, "যেকোনো সমস্যার জন্য এডমিনের সাথে যোগাযোগ করুন:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    if message.text == '💰 Balance':
        headers = {'Authorization': 'Bearer ' + FIVE_SIM_API_KEY, 'Accept': 'application/json'}
        try:
            r = requests.get('https://5sim.net/v1/user/profile', headers=headers)
            bot.send_message(message.chat.id, f"💳 Balance: {r.json().get('balance')} Rubles")
        except:
            bot.send_message(message.chat.id, "Error fetching balance!")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
