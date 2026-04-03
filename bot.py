import requests
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# এই দুটি চাবি আপনার নিজের গুলো বসান
TOKEN = "8574927098:AAGXeQdA8VNU2lM8Bh4fqjHWSMBbJVkmn7s"
API_KEY = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE4MDY1NTk1MjQsImlhdCI6MTc3NTAyMzUyNCwicmF5IjoiMDYxNjc1Mzc2MTFmYzRmOTA5NzNiMWQxYjM3ZmFhMDAiLCJzdWIiOjM5MjczNTV9.aTTdwcqYSpUFe-RQBVKuzPUOuU1hzF1GVF9t2-AVh_ixyGc5mldXdUvpmC5FwSBvnViznqJRbyPViq4UvvVoKIy1CkNTlZFaeBSlanZncGhoK0nRvaCHS2BGO9cGDT5PxeCegt9VF7iE3WcmHN7Z1G-ZfOptuPgnSujbZdXK_gQUdas81fZzEoPZn-vn9903FsJD9oO_qEuBN7C6XVMZR9hSpzet3j5w587Wzq7PTymwCqo0GmwqgMORS0fImGkfEBXZgtrH6HJDxzounVZh-CLW3Od1k0olV375uOywfFTQ5I7UDJUpFDiXpfZpFJKwFYkFd12lxU6j5bzXNILjAQ"

# Render-এর জন্য ছোট একটি ওয়েব সার্ভার
app = Flask('')
@app.route('/')
def home(): return "Bot is Online!"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Buy Number 📱", callback_data='buy_menu')],
                [InlineKeyboardButton("Balance 💰", callback_data='balance')]]
    await update.message.reply_text("Welcome! Bot is active.", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'balance':
        headers = {'Authorization': f'Bearer {API_KEY}', 'Accept': 'application/json'}
        r = requests.get('https://5sim.net/v1/user/profile', headers=headers)
        balance = r.json().get('balance', 0)
        await query.message.edit_text(f"Your Balance: {balance} Rubles")

def main():
    keep_alive() # এটি বটকে মরতে দেবে না
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_buttons))
    application.run_polling()

if __name__ == '__main__':
    main()
