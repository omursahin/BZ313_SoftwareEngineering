"""
FACADE PATTERN (Cephe/On Yuz Deseni)
====================================

TANIM:
Facade Pattern, karmasik bir alt sisteme basit bir arayuz saglayan yapisal (structural)
bir tasarim desenidir. Alt sistemdeki siniflar kumesine birlestirilmis tek bir arayuz
saglar ve alt sistemin kullanim ini kolaylastirir.

Ne Zaman Kullanilir:
--------------------
- Karmasik bir alt sistemi basit arayuzle saklamak istedigimizde
- Alt sistem cok karmasik ve kullanimi zor oldugunda
- İstemciyi alt sistem bagimliliklarindan yalitmak istedigimizde
- Alt sistemleri katmanlara ayirmak gerektiginde
- Cok sayida sinifla etkilesim gerektiren islemlerde

Avantajlari:
------------
+ Alt sistem karmasikligini gizler
+ İstemci kodu basitlesir
+ Gevşek baglanti (loose coupling) saglar
+ Kod okunabilirligi artar
+ Alt sistem kolayca degistirilebilir

Dezavantajlari:
--------------
- Facade "God Object" haline gelebilir
- Cok fazla sorumluluk tasiYabilir
- Alt sisteme dogrudan erisim kaybolabilir
- Asiri soyutlama yapilabilir

Gercek Hayattan Ornekler:
-------------------------
1. BILGISAYAR ACMA (Karmasik alt sistem):
   computer = ComputerFacade()

   # Arka planda: CPU.start(), Memory.load(), HardDrive.read(), etc.
   computer.start()  # Tek metod!

   # Manuel yapmak cok karmasik olurdu:
   # cpu.freeze()
   # memory.load(BOOT_ADDRESS, hardDrive.read(BOOT_SECTOR, SECTOR_SIZE))
   # cpu.jump(BOOT_ADDRESS)
   # cpu.execute()

2. ONLINE ALISVERIS:
   shop = OnlineShopFacade()

   # Arka planda: Inventory check, Payment process, Shipping arrange
   shop.place_order(product, payment_details, shipping_address)

   # Manuel:
   # inventory.check_availability(product)
   # payment_gateway.process(payment_details)
   # shipping.create_label(address)
   # notification.send_confirmation(email)

3. VIDEO DONUSTURUCU:
   converter = VideoConverterFacade()

   # Arka planda: Codec, BitrateReader, AudioMixer, etc.
   converter.convert("video.avi", "mp4")

   # Manuel cok karmasik olurdu:
   # codec = CodecFactory.extract(file)
   # buffer = BitrateReader.read(file, codec)
   # result = BitrateReader.convert(buffer, format)
   # audio = AudioMixer.fix(result)
   # File.save(result, new_file)

4. VERITABANI ISLEMLERI:
   db_facade = DatabaseFacade()

   # Basit arayuz
   users = db_facade.get_all_users()
   db_facade.create_user(user_data)

   # Arka planda: Connection, Query Builder, Result Parser, Cache, Logger
   # connection.open()
   # query = builder.select().from("users")
   # result = query.execute()
   # parsed = parser.parse(result)
   # cache.store(parsed)
   # connection.close()

5. EV SINEMA SISTEMI:
   home_theater = HomeTheaterFacade()

   # Tek komutla tum sistemi hazirla
   home_theater.watch_movie("Inception")

   # Arka planda:
   # amplifier.on()
   # amplifier.setDvd(dvd)
   # amplifier.setVolume(5)
   # dvd.on()
   # dvd.play(movie)
   # projector.on()
   # projector.wideScreenMode()
   # lights.dim(10)
   # screen.down()
   # popper.on()
   # popper.pop()

6. BANKACILIK SISTEMI:
   bank_facade = BankingServiceFacade()

   # Basit arayuz
   bank_facade.transfer_money(from_account, to_account, amount)

   # Arka planda: Account validation, Balance check, Transaction log,
   # Notification, Security check, etc.

7. API KUTUPHANESI:
   api = WeatherAPIFacade()

   # Basit kullanim
   weather = api.get_current_weather("Istanbul")

   # Arka planda: HTTP request, Authentication, JSON parsing,
   # Error handling, Caching, Rate limiting

Facade vs Adapter:
------------------
- Facade: Karmasik alt sistemi basitlestirir, yeni arayuz tanimlar
- Adapter: Mevcut arayuzu baska bir arayuze cevirir

Facade vs Mediator:
-------------------
- Facade: Tek yonlu (istemci -> alt sistem)
- Mediator: Iki yonlu (nesneler arasi iletisim)

Asagidaki Ornekte:
------------------
Camasir makinesi (WashingMachine) facade'i gosterilmektedir.
startWashing() metodu, Washing, Rinsing ve Spinning alt sistemlerini
koordine ederek basit bir arayuz saglar.
"""

"""Facade pattern with an example of WashingMachine"""


class Washing:
    '''Subsystem # 1'''

    def wash(self):
        print("Washing...")


class Rinsing:
    '''Subsystem # 2'''

    def rinse(self):
        print("Rinsing...")


class Spinning:
    '''Subsystem # 3'''

    def spin(self):
        print("Spinning...")


class WashingMachine:
    '''Facade'''

    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()


""" main method """
if __name__ == "__main__":
    washingMachine = WashingMachine()
    washingMachine.startWashing()
