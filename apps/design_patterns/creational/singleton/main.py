"""
SINGLETON PATTERN (Tekil Nesne Deseni)
=======================================

TANIM:
Singleton Pattern, bir sinifin sadece bir orneginin (instance) olusturulmasini garanti
eden ve bu orneğe global erisim noktasi saglayan yaratici (creational) bir tasarim
desenidir. Sinif, kendi tek ornegini yonetir ve baska ornek olusturulmasini engeller.

Ne Zaman Kullanilir:
--------------------
- Bir sinifin sadece bir ornegi olmalidir
- Global erisim noktasi gerektiginde
- Lazy initialization gerektiginde
- Paylasilan kaynaklari yonetmek istedigimizde
- Nesne olusturma maliyeti yuksek oldugunda

Avantajlari:
------------
+ Sinifin sadece bir ornegine sahip olmanizi garanti eder
+ Global erisim noktasi saglar
+ Lazy initialization - sadece ihtiyac duyuldugunda olusturulur
+ Bellek tasarrufu saglar
+ Paylasilan kaynaklari yonetmek icin idealdir

Dezavantajlari:
--------------
- Global state yaratir (test edilebilirlik azalir)
- Single Responsibility Principle'i ihlal edebilir
- Multi-thread ortamlarda dikkatli kullanilmalidir
- Unit test yazmak zorlasir
- Gizli bagimliliklar olusturabilir

Gercek Hayattan Ornekler:
-------------------------
1. VERITABANI BAGLANTISI:
   # Tum uygulama boyunca tek bir veritabani baglantisi
   db = Database.getInstance()
   db.query("SELECT * FROM users")

   # Baska bir yerde tekrar cagirilsa ayni instance doner
   db2 = Database.getInstance()  # db ile ayni nesne

2. LOGGER (GUNLUK KAYDEDICI):
   # Tum uygulama tek bir log dosyasina yazar
   logger = Logger.getInstance()
   logger.log("Uygulama basladi")

   # Baska modullerde
   logger2 = Logger.getInstance()  # Ayni logger
   logger2.log("Islem tamamlandi")

3. KONFIGURASYON YONETIMI:
   # Uygulama ayarlarini tek bir yerden yonet
   config = Configuration.getInstance()
   api_key = config.get("API_KEY")
   db_host = config.get("DB_HOST")

4. CACHE YONETIMI:
   # Tum uygulama icin tek bir cache
   cache = Cache.getInstance()
   cache.set("user_123", user_data)
   user = cache.get("user_123")

5. YAZICI SPOOL:
   # Sistemdeki yazici kuyrugunu yonet
   printer_spooler = PrinterSpooler.getInstance()
   printer_spooler.add_job(document)

6. OYUN YONETICISI:
   # Oyun durumunu tutan tek bir yonetici
   game_manager = GameManager.getInstance()
   game_manager.start_game()
   score = game_manager.get_score()

DIKKAT EDILMESI GEREKENLER:
---------------------------
- Thread-safe implementasyon gerekebilir (multi-threading)
- Test ederken mock objeler olusturmak zor olabilir
- Asiri kullanim "anti-pattern" haline gelebilir
- Dependency Injection alternatif olabilir

Asagidaki Ornekte:
------------------
Klasik Singleton implementasyonu gosterilmektedir. Sinif, kendi tek ornegini
yonetir ve getInstance() metodu ile bu orneğe erisim saglar.
"""

# classic implementation of Singleton Design pattern
class Singleton:
    __shared_instance = 'GeeksforGeeks'

    @staticmethod
    def getInstance():
        """Static Access Method"""
        if Singleton.__shared_instance == 'GeeksforGeeks':
            Singleton()
        return Singleton.__shared_instance

    def __init__(self):
        """virtual private constructor"""
        if Singleton.__shared_instance != 'GeeksforGeeks':
            raise Exception("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self


# main method
if __name__ == "__main__":
    # create object of Singleton Class
    obj = Singleton()
    print(obj)

    # pick the instance of the class
    obj = Singleton.getInstance()
    print(obj)