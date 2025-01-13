try:
    from os import system as s
    import requests as r
    from telebot import TeleBot
    import re
except:
    s("pip install requests")

bot = TeleBot("7805179496:AAF-ygkfSWxtVf-oGGV1qiXLsaNpP_O7EyE")

class Wkaie:
    def banner():
        s("cls")
        banner = """░█──░█ ░█─▄▀ ─█▀▀█ ▀█▀ ░█▀▀▀ \n░█░█░█ ░█▀▄─ ░█▄▄█ ░█─ ░█▀▀▀ \n░█▄▀▄█ ░█─░█ ░█─░█ ▄█▄ ░█▄▄▄"""
        print(banner, "\n\n")
        
    def generator():
        url = "https://random-hadith-generator.vercel.app/bukhari/"
        load = r.get(url).json()
        book = "Book: <b>" + str(load['data']["book"]) + "</b>"
        bookName = "Book name: <b>" + str(load['data']["bookName"]).replace("\t", "").replace("\n", "") + "</b>"
        chapter = "Chapter name: <b>" + str(load['data']["chapterName"]).replace("Chapter:", "").replace("\n", "") + "</b>"
        ref = "Reference no: <b>" + str(load['data']["refno"]) + "</b>"
        hadith = "Hadith: <b>" + str(load['data']["hadith_english"]) + "</b>"
        
        return book, bookName, chapter, ref, hadith
        
@bot.message_handler(func=lambda messx: True)
def hadith(messx):
    print(str(messx.text).lower)
    if re.search("^hello", str(messx.text).lower):
        book = Wkaie.generator()
        bot.send_message(messx.chat.id, text=book[0], parse_mode="HTML")
        bot.send_message(messx.chat.id, text=book[1], parse_mode="HTML")
        bot.send_message(messx.chat.id, text=book[2], parse_mode="HTML")
        bot.send_message(messx.chat.id, text=book[3], parse_mode="HTML")
        bot.send_message(messx.chat.id, text=book[4], parse_mode="HTML")
        print(messx.chat.first_name, "runned")

if __name__ == "__main__":
    Wkaie.banner()    
    bot.infinity_polling(none_stop=True)