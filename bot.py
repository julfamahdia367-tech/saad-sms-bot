from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# আপনার বটের টোকেনটি এখানে বসান
TOKEN = "8574927098:AAGXeQdA8VNU21M8Bh4fqjHWSMBbJVkmn7s"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # রঙিন বাটনগুলো তৈরি করা
    keyboard = [
        [InlineKeyboardButton("📲 Get Number", callback_data='get_num'),
         InlineKeyboardButton("💰 Balance", callback_data='balance')],
        [InlineKeyboardButton("👥 Refer & Earn", callback_data='refer'),
         InlineKeyboardButton("💬 Support", callback_data='support')],
        [InlineKeyboardButton("📊 Status", callback_data='status')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        "👋 Welcome to **SAAD SMS PRO**!\n\n"
        "⚡ Fast delivery\n"
        "🔒 Secure numbers\n"
        "♻️ Change anytime"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'balance':
        await query.edit_message_text(text="💵 আপনার বর্তমান ব্যালেন্স: **০.০০ টাকা**", parse_mode='Markdown')
    elif query.data == 'support':
        await query.edit_message_text(text="👨‍💻 সাহায্য পেতে অ্যাডমিনকে নক দিন: @YourUsername")
    elif query.data == 'get_num':
        await query.edit_message_text(text="⚠️ নাম্বার পেতে হলে আপনাকে API কানেক্ট করতে হবে।")
    else:
        await query.edit_message_text(text="⚠️ এই বাটনটি এখনো সেটআপ করা হয়নি।")

def main():
    # অ্যাপ তৈরি এবং হ্যান্ডলার যোগ করা
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))
    
    print("বটটি এখন সার্ভারে রান করার জন্য প্রস্তুত...")
    app.run_polling()

if __name__ == "__main__":
    main()
