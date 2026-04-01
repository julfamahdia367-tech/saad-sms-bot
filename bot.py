import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# নিচের এই দুটি চাবি সাবধানে বসান
TOKEN = "আপনার_বট_টোকেন_এখানে"
API_KEY = "8574927098:AAGXeQdA8VNU2lM8Bh4fqjHWSMBbJVkmn7s"

# স্টার্ট কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Buy Number 📱", callback_data='buy_menu')],
        [InlineKeyboardButton("My Balance 💰", callback_data='check_balance')],
        [InlineKeyboardButton("Support 🛠️", url='https://t.me/your_username')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to SAAD SMS BOT! Choose an option:", reply_markup=reply_markup)

# বাটন ক্লিক হ্যান্ডলার
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'check_balance':
        # 5sim থেকে ব্যালেন্স চেক করার কোড
        headers = {'Authorization': f'Bearer {API_KEY}', 'Accept': 'application/json'}
        try:
            response = requests.get('https://5sim.net/v1/user/profile', headers=headers)
            data = response.json()
            balance = data.get('balance', 0)
            await query.message.edit_text(f"Your 5sim Balance: {balance} Rubles")
        except:
            await query.message.edit_text("API Error! Please check your API Key.")

    elif query.data == 'buy_menu':
        await query.message.edit_text("Fetching country list... Please wait.")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_buttons))
    print("Bot is alive and kicking!")
    application.run_polling()

if __name__ == '__main__':
    main()
