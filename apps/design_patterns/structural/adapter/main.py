"""
ADAPTER PATTERN (Adaptör/Cevirici Deseni)
==========================================

TANIM:
Adapter Pattern, uyumsuz arayuzlere sahip siniflarin birlikte calismasi ni saglayan
yapisal (structural) bir tasarim desenidir. Var olan bir sinifin arayuzunu, istemcinin
bekledigi baska bir arayuze cevirir. "Wrapper" olarak da bilinir.

Ne Zaman Kullanilir:
--------------------
- Var olan bir sinifi kullanmak istiyoruz ama arayuzu uyumsuzsa
- Birlikte calisma si beklenmeyen siniflari birlestirmek gerektiginde
- Ucuncu taraf kutuphaneleri entegre ederken
- Legacy (eski) kod ile yeni kod arasinda kopru kurmak gerektiginde
- Farkli arayuzlere sahip benzer islevleri standartlastirmak istedigimizde

Avantajlari:
------------
+ Single Responsibility - arayuz donusumu ayri bir sinifta
+ Open/Closed - yeni adapter'lar kolayca eklenebilir
+ Kod yeniden kullanilabilirlik artar
+ Legacy kod degistirilmeden yeni sistemle calisir
+ Ucuncu taraf kutuphaneleri uyumlastirabilir

Dezavantajlari:
--------------
- Kod karmasikligi artar (yeni sinif gerekir)
- Bazen kaynak sinifi degistirmek daha basittir
- Cok fazla adapter performans sorunlarina yol acabilir

Gercek Hayattan Ornekler:
-------------------------
1. ELEKTRIK PRIZE ADAPTORU:
   # Avrupa prizi (2 pin) -> Turkiye prizi (3 pin)
   european_plug = EuropeanPlug()
   adapter = PlugAdapter(european_plug)
   adapter.connect_to_turkish_socket()  # Calisiyor!

2. VERI FORMATI DONUSUMU:
   # XML verisini JSON bekleyen sisteme adaptla
   xml_data_source = XMLDataSource()
   adapter = XMLToJSONAdapter(xml_data_source)
   json_data = adapter.get_data()  # JSON formatinda doner

3. ODEME SISTEMI ENTEGRASYONU:
   # Farkli odeme gateway'lerini ayni arayuze adaptla
   stripe_adapter = StripeAdapter(stripe_api)
   paypal_adapter = PayPalAdapter(paypal_api)
   iyzico_adapter = IyzicoAdapter(iyzico_api)

   # Hepsi ayni arayuzu kullanir
   stripe_adapter.process_payment(amount)
   paypal_adapter.process_payment(amount)
   iyzico_adapter.process_payment(amount)

4. VERITABANI BAGLANTI ADAPTORU:
   # Legacy MySQL kodunu PostgreSQL'e adaptla
   old_db = MySQLConnection()
   adapter = DatabaseAdapter(old_db)

   # Yeni kod PostgreSQL arayuzu bekliyor
   adapter.query("SELECT * FROM users")

5. LOG SISTEMI ADAPTORU:
   # Farkli log kutuphanelerini standart arayuze adaptla
   log4j_logger = Log4jLogger()
   loguru_logger = LoguruLogger()

   log4j_adapter = Log4jAdapter(log4j_logger)
   loguru_adapter = LoguruAdapter(loguru_logger)

   # Her ikisi de ayni log() metodunu kullanir
   log4j_adapter.log("Mesaj")
   loguru_adapter.log("Mesaj")

6. MEDYA OYNATICI:
   # MP4 oynatici sadece MP4 destekliyor
   # AVI dosyalarini adaptorle oynat
   avi_file = AVIFile("movie.avi")
   adapter = AVIToMP4Adapter(avi_file)
   media_player.play(adapter)

7. API VERSIYONLAMA:
   # Eski API (v1) -> Yeni API (v2) adaptoru
   legacy_api = APIv1()
   adapter = APIv1ToV2Adapter(legacy_api)

   # Yeni kod v2 bekliyor
   adapter.get_user_data(user_id)

Adapter vs Facade:
------------------
- Adapter: Mevcut arayuzu baska bir arayuze cevirir
- Facade: Karmasik sistemi basit arayuzle sarar

Adapter vs Decorator:
---------------------
- Adapter: Arayuzu degistirir
- Decorator: Arayuzu ayni tutar, islevsellik ekler

Asagidaki Ornekte:
------------------
Farkli tasit siniflari (MotorCycle, Truck, Car) farkli metod isimleri
kullaniyor (TwoWheeler, EightWheeler, FourWheeler). Adapter pattern
kullanilarak hepsi ayni "wheels()" arayuzune adapt edilmistir.
"""

# Dog - Cycle
# human - Truck
# car - Car

class MotorCycle:
    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:
    """Class for Truck"""

    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"


class Car:
    """Class for Car"""

    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"


class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__


""" main method """
if __name__ == "__main__":

    """list to store objects"""
    objects = []

    motorCycle = MotorCycle()
    objects.append(Adapter(motorCycle, wheels=motorCycle.TwoWheeler))

    truck = Truck()
    objects.append(Adapter(truck, wheels=truck.EightWheeler))

    car = Car()
    objects.append(Adapter(car, wheels=car.FourWheeler))

    for obj in objects:
        print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))