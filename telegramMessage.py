import telepot

send_telegram_msg()
def send_telegram_msg():
    msg = ""
    chatid = settings.TEL_CHATID
    token = settings.TEL_TOKEN
    bot = telepot.Bot(token=token)
    bot.sendMessage(chat_id=chatid, text=msg)
