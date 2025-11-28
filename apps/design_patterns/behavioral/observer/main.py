"""
OBSERVER PATTERN (Gozlemci Deseni)
===================================

TANIM:
Observer Pattern, bir nesnedeki degisiklikleri bagimli nesnelere otomatik olarak bildiren
davranissal (behavioral) bir tasarim desenidir. "Publish-Subscribe" veya "Event-Listener"
olarak da bilinir.

Ne Zaman Kullanilir:
--------------------
- Bir nesnedeki degisiklik diger nesneleri etkilediginde
- Nesnenin kac tane gozlemcisi oldugunu onceden bilmedigimizde
- Event-driven (olay tabanli) mimari gerektiginde
- Gevşek baglanti (loose coupling) istedigimizde
- One-to-many bagimliligi varsa

Avantajlari:
------------
+ Open/Closed Principle - yeni subscriber'lar kolayca eklenebilir
+ Runtime'da iliskiler kurulabilir
+ Gevşek baglanti saglar
+ Broadcast iletisim destekler
+ Event-driven programming destegi

Dezavantajlari:
--------------
- Observer'lar rastgele sirada bildirim alir
- Bellek sizintisi riski (observer kaydini silmezsek)
- Performans problemi (cok fazla observer)
- Debug edilmesi zor olabilir

Gercek Hayattan Ornekler:
-------------------------
1. HABER ABONELIGI (Newsletter):
   newspaper = Newspaper()

   subscriber1 = EmailSubscriber("ahmet@example.com")
   subscriber2 = SMSSubscriber("+905551234567")
   subscriber3 = PushNotificationSubscriber("user123")

   newspaper.subscribe(subscriber1)
   newspaper.subscribe(subscriber2)
   newspaper.subscribe(subscriber3)

   # Yeni haber yayinlandi
   newspaper.publish("Onemli haber!")  # Tum aboneler bildirim alir

2. SOSYAL MEDYA TAKIP SISTEMI:
   influencer = SocialMediaAccount("tech_guru")

   follower1 = User("user1")
   follower2 = User("user2")
   follower3 = User("user3")

   influencer.add_follower(follower1)
   influencer.add_follower(follower2)
   influencer.add_follower(follower3)

   influencer.post("Yeni video!")  # Tum takipciler bildirim alir

3. HISSE SENEDI FIYAT TAKIBI:
   stock = Stock("AAPL", price=150)

   trader1 = Trader("trader1")
   trader2 = Trader("trader2")
   analyst = MarketAnalyst()

   stock.add_observer(trader1)
   stock.add_observer(trader2)
   stock.add_observer(analyst)

   stock.set_price(155)  # Fiyat degisti, herkes bilgilendirildi
   # trader1: "AAPL 155'e cikti"
   # trader2: "AAPL 155'e cikti"
   # analyst: "AAPL 155'e cikti, analiz yapiliyor..."

4. GUI EVENT LISTENER:
   button = Button("Submit")

   button.add_click_listener(lambda: print("Form gonderiliyor"))
   button.add_click_listener(lambda: validate_form())
   button.add_click_listener(lambda: analytics.track("button_clicked"))

   button.click()  # Tum listener'lar calisir

5. DOSYA DEGISIKLIK IZLEYICI:
   file_watcher = FileWatcher("config.json")

   config_manager = ConfigManager()
   cache_cleaner = CacheCleaner()
   logger = Logger()

   file_watcher.add_observer(config_manager)
   file_watcher.add_observer(cache_cleaner)
   file_watcher.add_observer(logger)

   # Dosya degisti
   file_watcher.detect_change()  # Tum observer'lar bilgilendirilir

6. ISIK SENSORU SISTEMI:
   light_sensor = LightSensor()

   auto_lights = AutomaticLights()
   blinds = AutomaticBlinds()
   alarm = SecurityAlarm()

   light_sensor.add_observer(auto_lights)
   light_sensor.add_observer(blinds)
   light_sensor.add_observer(alarm)

   light_sensor.detect_darkness()
   # auto_lights: Isiklari ac
   # blinds: Panjurlari kapat
   # alarm: Gece moduna gec

Asagidaki Ornekte:
------------------
Veri degisikliklerini farkli gorunumlerde (Decimal, Hex, Octal) gosteren
observer pattern ornegi bulunmaktadir. Data nesnesi degistiginde tum
viewer'lar (observer'lar) otomatik olarak guncellenir.
"""

class Subject:
    """Represents what is being observed"""

    def __init__(self):

        """create an empty observer list"""

        self._observers = []

    def notify(self, modifier=None):

        """Alert the observers"""

        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):

        """If the observer is not in the list,
        append it into the list"""

        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):

        """Remove the observer from the observer list"""

        try:
            self._observers.remove(observer)
        except ValueError:
            pass


class Data(Subject):
    """monitor the object"""

    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexViewer:
    """updates the Hexviewer"""

    def update(self, subject):
        print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))


class OctalViewer:
    """updates the Octal viewer"""

    def update(self, subject):
        print('OctalViewer: Subject' + str(subject.name) + 'has data ' + str(oct(subject.data)))


class DecimalViewer:
    """updates the Decimal viewer"""

    def update(self, subject):
        print('DecimalViewer: Subject % s has data % d' % (subject.name, subject.data))


"""main function"""

if __name__ == "__main__":
    """provide the data"""

    obj1 = Data('Data 1')
    obj2 = Data('Data 2')

    view1 = DecimalViewer()
    view2 = HexViewer()
    view3 = OctalViewer()

    obj1.attach(view1)
    obj1.attach(view2)
    obj1.attach(view3)

    obj2.attach(view1)
    obj2.attach(view2)
    obj2.attach(view3)

    obj1.data = 10
    obj2.data = 15
