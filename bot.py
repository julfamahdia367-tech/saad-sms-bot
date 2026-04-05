# নিচের মেনু বাটনগুলো তৈরি করার অংশ
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    # এখানে বাটনগুলোর নাম আগের মতোই থাকবে
    btn1 = types.KeyboardButton('📲 Get Number')
    btn2 = types.KeyboardButton('💰 Balance')
    btn3 = types.KeyboardButton('👥 Refer & Earn')
    btn4 = types.KeyboardButton('💬 Support')
    btn5 = types.KeyboardButton('📊 Status')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "Welcome to Saad SMS Pro!", reply_markup=markup)

# কেউ '💬 Support' বাটনে ক্লিক করলে এই ফাংশনটি কাজ করবে
@bot.message_handler(func=lambda message: message.text == '💬 Support')
def contact_admin(message):
    # ইনলাইন বাটন তৈরি (মেসেজের সাথে লেগে থাকবে)
    inline_markup = types.InlineKeyboardMarkup()
    # 'your_username' এর জায়গায় আপনার আসল ইউজারনেম দিন (যেমন: https://t.me/@SaadsmsproBot)
    support_link = types.InlineKeyboardButton(text="Contact Admin", url="https://t.me/your_username")
    inline_markup.add(support_link)
    
    bot.send_message(message.chat.id, "যেকোনো সমস্যার জন্য নিচের বাটনে ক্লিক করে এডমিনের সাথে যোগাযোগ করুন:", reply_markup=inline_markup)
