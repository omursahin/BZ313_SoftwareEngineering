"""
MEDIATOR PATTERN (Arabulucu Deseni)
====================================

TANIM:
Mediator Pattern, nesneler arasindaki karmasik iletisimi ve bagimliliklari azaltarak
nesnelerin birbirleriyle dolayli olarak iletisim kurmasini saglayan davranissal
(behavioral) bir tasarim desenidir.

Ne Zaman Kullanilir:
--------------------
- Nesneler arasi karmasik iletisim agı varsa
- Nesnelerin cok sikica bagimli oldugu durumlarda
- Bir grup nesne iyi tanimlanmis ama karmasik sekilde etkilesim yapiyorsa
- Nesneleri yeniden kullanilabilir yapmak istedigimizde
- İletisim mantigi merkezilestirmek gerektiginde

Avantajlari:
------------
+ Single Responsibility - iletisim mantigi tek yerde
+ Nesneler arasi gevşek baglanti
+ Nesnelerin yeniden kullanilabilirligini arttirir
+ İletisim mantigi kolayca degistirilebilir
+ Karmasik iliski agi basitlesir

Dezavantajlari:
--------------
- Mediator cok karmasik hale gelebilir
- "God Object" anti-pattern riski
- Performans problemi olusabilir

Gercek Hayattan Ornekler:
-------------------------
1. HAVA TRAFIK KONTROL KULESI:
   # Ucaklar birbirleriyle degil, kule ile konusur
   plane1 = Airplane("THY123")
   plane2 = Airplane("PGT456")
   control_tower = AirTrafficControl()

   control_tower.register(plane1)
   control_tower.register(plane2)

   plane1.request_landing()  # Kule diger ucaklari bilgilendirir
   control_tower.coordinate_landing(plane1)

2. CHAT ODASI:
   # Kullanicilar birbirleriyle degil, chat odasi uzerinden mesaj gonderir
   chat_room = ChatRoom()

   user1 = User("Ahmet")
   user2 = User("Mehmet")
   user3 = User("Ayse")

   chat_room.register(user1)
   chat_room.register(user2)
   chat_room.register(user3)

   user1.send("Merhaba!")  # Tum kullanicilar alir
   user2.send_private(user3, "Selam Ayse")  # Sadece Ayse alir

3. GUI DIALOG YONETIMI:
   # Form elemanlari dialog uzerinden etkilesir
   dialog = Dialog()

   username_field = TextField("username")
   password_field = TextField("password")
   login_button = Button("Login")
   remember_checkbox = Checkbox("Remember me")

   # Username bossa button devre disi
   # Checkbox isaretliyse password kaydet

   dialog.register_all([username_field, password_field, login_button, remember_checkbox])

4. AKILLI EV SISTEMI:
   home_hub = SmartHomeHub()

   motion_sensor = MotionSensor()
   lights = SmartLights()
   camera = SecurityCamera()
   alarm = Alarm()

   home_hub.register_all([motion_sensor, lights, camera, alarm])

   # Hareket algilandi
   motion_sensor.detect_motion()
   # Hub otomatik olarak:
   # - Isiklari ac
   # - Kamerayi kaydet
   # - Ev sahibini bilgilendir

5. BORSA ISLEM PLATFORMU:
   exchange = StockExchange()

   buyer1 = Trader("Buyer1")
   seller1 = Trader("Seller1")
   buyer2 = Trader("Buyer2")

   exchange.register(buyer1)
   exchange.register(seller1)
   exchange.register(buyer2)

   seller1.place_order("SELL", "AAPL", 100, price=150)
   buyer1.place_order("BUY", "AAPL", 50, price=150)
   # Exchange eslestirmeyi yapar

Asagidaki Ornekte:
------------------
Kurs sistemi icin basit bir mediator ornegi gosterilmektedir.
Course sinifi mediator rolundedir ve kullanicilarin kurs bilgilerini
merkezilestirerek yonetir.
"""

class Course(object):
    """Mediator class."""

    def displayCourse(self, user, course_name):
        print("[{}'s course ]: {}".format(user, course_name))


class User(object):
    '''A class whose instances want to interact with each other.'''

    def __init__(self, name):
        self.name = name
        self.course = Course()

    def sendCourse(self, course_name):
        self.course.displayCourse(self, course_name)

    def __str__(self):
        return self.name


"""main method"""

if __name__ == "__main__":
    mayank = User('Mayank')  # user object
    lakshya = User('Lakshya')  # user object
    krishna = User('Krishna')  # user object

    mayank.sendCourse("Data Structures and Algorithms")
    lakshya.sendCourse("Software Development Engineer")
    krishna.sendCourse("Standard Template Library")
