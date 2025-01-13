try:
    from os import system as s
    import requests as r
except:
    s("pip install requests")

class Wkaie:
    def banner():
        banner = """░█──░█ ░█─▄▀ ─█▀▀█ ▀█▀ ░█▀▀▀ \n░█░█░█ ░█▀▄─ ░█▄▄█ ░█─ ░█▀▀▀ \n░█▄▀▄█ ░█─░█ ░█─░█ ▄█▄ ░█▄▄▄"""
        print(banner, "\n\n")
        
    def generator():
        url = "https://random-hadith-generator.vercel.app/bukhari/"
        load = r.get(url).json()
        book = str(load['data']["book"])
        bookName = str(load['data']["bookName"]).replace("\t", "").replace("\n", "")
        chapter = str(load['data']["chapterName"]).replace("Chapter:", "").replace("\n", "")
        ref = str(load['data']["refno"])
        hadith = str(load['data']["hadith_english"])

        print("Book:", book)
        print("Book name:", bookName)
        print("Chapter name:", chapter)
        print("Reference no:", ref)
        print("Hadith:", hadith)
        
    def wkaie():
        Wkaie.banner()
        Wkaie.generator()
        
if __name__ == "__main__":
    s("cls")
    Wkaie.wkaie()