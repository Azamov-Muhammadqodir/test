import telebot
import wikipedia
wikipedia.set_lang('uz')
bot=telebot.TeleBot('5112077016:AAEdoRqCXob8zhMb84v_G_rs23xPNBkKMDE')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Salom')
@bot.message_handler(content_types=['text'])
def text(message):
    final=message.text.strip()
    try:
        mess=wikipedia.page(final).content
        if len(mess)>4096:
            for x in range(0,len(mess),4096):
                bot.send_message(message.chat.id,mess[x:x+4096])
        else:
            bot.send_message(message.chat.id,mess)
    except wikipedia.DisambiguationError:
        bot.send_message(message.chat.id,"Malumot kop yuklandi")
    except wikipedia.PageError:
        bot.send_message(message.chat.id,"Xatolik")
bot.polling()