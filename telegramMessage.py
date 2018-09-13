import telepot

send_telegram_msg()

def send_telegram_msg():
    msg = ""
    chatid = ""
    token = ""
    bot = telepot.Bot(token=token)
    bot.sendMessage(chat_id=chatid, text=msg)
