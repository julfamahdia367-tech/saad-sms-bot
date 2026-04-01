from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# আপনার সঠিক টোকেনটি এখানে বসান (BotFather থেকে পাওয়া)
TOKEN = "8574927098:AAGXeQdA8VNU2lM8Bh4fqjHWSMBbJVkmn7s"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Buy Number 📱", callback_data='buy')],
        [InlineKeyboardButton("Balance 💰", callback_data='balance')],
        [InlineKeyboardButton("Support 🛠️", url='https://t.me/your_username')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to SAAD SMS BOT! How can I help you?", reply_markup=reply_markup)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
