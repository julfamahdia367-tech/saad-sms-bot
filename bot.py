import telebot
from telebot import types
import requests

# আপনার তথ্যগুলো এখানে দিন
API_TOKEN = '8574927098:AAGXeQdA8VNU2lM8Bh4fqjHWSMBbJVkmn7s' # BotFather থেকে পাওয়া টোকেন
FIVE_SIM_API_KEY = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE4MDY1NTk1MjQsImlhdCI6MTc3NTAyMzUyNCwicmF5IjoiMDYxNjc1Mzc2MTFmYzRmOTA5NzNiMWQxYjM3ZmFhMDAiLCJzdWIiOjM5MjczNTV9.aTTdwcqYSpUFe-RQBVKuzPUOuU1hzF1GVF9t2-AVh_ixyGc5mldXdUvpmC5FwSBvnViznqJRbyPViq4UvvVoKIy1CkNTlZFaeBSlanZncGhoK0nRvaCHS2BGO9cGDT5PxeCegt9VF7iE3WcmHN7Z1G-ZfOptuPgnSujbZdXK_gQUdas81fZzEoPZn-vn9903FsJD9oO_qEuBN7C6XVMZR9hSpzet3j5w587Wzq7PTymwCqo0GmwqgMORS0fImGkfEBXZgtrH6HJDxzounVZh-CLW3Od1k0olV375uOywfFTQ5I7UDJUpFDiXpfZpFJKwFYkFd12lxU6j5bzXNILjAQ' # ৫সিম থেকে পাওয়া চাবি

bot = telebot.TeleBot(API_TOKEN)

# /start কমান্ড এবং কিবোর্ড ডিজাইন
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    
    # আপনার স্ক্রিনশট অনুযায়ী বাটনগুলো সাজানো হলো
    btn1 = types.KeyboardButton('📲 Get Number')
    btn2 = types.KeyboardButton('💰 Balance')
    btn3 = types.KeyboardButton('👥 Refer & Earn')
    btn4 = types.KeyboardButton('💬 Support')
    btn5 = types.KeyboardButton('📊 Status')
    
    markup.add(btn1)
    markup.row(btn2, btn3)
    markup.row(btn4, btn5)
    
    welcome_text = "⚡ **Welcome to Saad SMS Pro** ⚡\n\nFast delivery & Secure numbers!"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

# বাটনগুলোর কাজ (Handling Clicks)
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == '📲 Get Number':
        bot.send_message(message.chat.id, "Which country do you want? 🌍\n(এখান থেকে আপনি কান্ট্রি লিস্ট যোগ করতে পারবেন)")

    elif message.text == '💰 Balance':
        # ৫সিম থেকে ব্যালেন্স চেক করার রিয়েল কোড
        headers = {'Authorization': 'Bearer ' + FIVE_SIM_API_KEY, 'Accept': 'application/json'}
        try:
            response = requests.get('https://5sim.net/v1/user/profile', headers=headers)
            data = response.json()
            balance = data.get('balance', 'Error')
            bot.send_message(message.chat.id, f"💳 Your Balance: **{balance} Rubles**", parse_mode='Markdown')
        except:
            bot.send_message(message.chat.id, "❌ Could not fetch balance. Check API Key.")

    elif message.text == '👥 Refer & Earn':
        bot.send_message(message.chat.id, "📢 Invite your friends and earn 5% bonus on every deposit!")

    elif message.text == '💬 Support':
        bot.send_message(message.chat.id, "🆘 Contact Admin: @আপনার_ইউজারনেম")

    elif message.text == '📊 Status':
        bot.send_message(message.chat.id, "✅ Server: **Online**\n📈 System: **Stable**", parse_mode='Markdown')

bot.infinity_polling()
