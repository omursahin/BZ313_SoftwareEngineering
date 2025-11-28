"""
BRIDGE PATTERN (Kopru Deseni)
==============================

TANIM:
Bridge Pattern, soyutlamayi (abstraction) uygulamasindan (implementation) ayirarak
ikisinin bagimsiz olarak degisebilmesini saglayan yapisal (structural) bir tasarim
desenidir. Buyuk sinif hiyerarsilerini iki ayri hiyerarsiye boldugu icin "implementor"
olarak da bilinir.

Ne Zaman Kullanilir:
--------------------
- Soyutlama ve uygulamayi ayirmak istedigimizde
- Hem soyutlama hem uygulama genisletilmek istendiginde
- Runtime'da uygulama degistirmek gerektiginde
- Sinif sayisi patlamasi (class explosion) onlenmek istendiginde
- Bir sinifin farkli varyantlari varsa

Avantajlari:
------------
+ Platform bagimsizlik saglar
+ Soyutlama ve uygulama bagimsiz gelistirilebilir
+ Open/Closed Principle - her iki taraf ayri genisleyebilir
+ Single Responsibility - her seviye kendi sorumluluguna odaklanir
+ Client kodu uygulama detaylarindan izole edilir

Dezavantajlari:
--------------
- Tasarim karmasikligi artar
- Yuksek duzeyde baglantili tasarim gerektiri r
- Basit senaryolar icin gereksiz olabilir

Gercek Hayattan Ornekler:
-------------------------
1. GRAFIK CIZDIRME (Cross-Platform GUI):
   # Abstraction: Shapes
   circle = Circle(drawing_api)
   rectangle = Rectangle(drawing_api)

   # Implementation: Drawing API
   circle.set_drawing_api(WindowsDrawingAPI())  # Windows'ta ciz
   circle.draw()

   circle.set_drawing_api(LinuxDrawingAPI())    # Linux'ta ciz
   circle.draw()

   circle.set_drawing_api(MacOSDrawingAPI())    # macOS'ta ciz
   circle.draw()

2. UZAKTAN KUMANDA VE CIHAZLAR:
   # Abstraction: Remote Control
   basic_remote = BasicRemote(device)
   advanced_remote = AdvancedRemote(device)

   # Implementation: Devices
   tv = TV()
   radio = Radio()

   basic_remote.set_device(tv)
   basic_remote.toggle_power()

   advanced_remote.set_device(radio)
   advanced_remote.mute()

3. MESAJ GONDERME SISTEMI:
   # Abstraction: Message Types
   text_message = TextMessage(sender)
   encrypted_message = EncryptedMessage(sender)

   # Implementation: Senders
   email_sender = EmailSender()
   sms_sender = SMSSender()
   push_sender = PushNotificationSender()

   text_message.set_sender(email_sender)
   text_message.send("Merhaba")

   encrypted_message.set_sender(sms_sender)
   encrypted_message.send("Gizli mesaj")

4. VERITABANI BAGLANTI:
   # Abstraction: Query Types
   simple_query = SimpleQuery(db_driver)
   optimized_query = OptimizedQuery(db_driver)

   # Implementation: Database Drivers
   mysql_driver = MySQLDriver()
   postgres_driver = PostgreSQLDriver()
   mongodb_driver = MongoDBDriver()

   simple_query.set_driver(mysql_driver)
   simple_query.execute("SELECT * FROM users")

   optimized_query.set_driver(postgres_driver)
   optimized_query.execute_with_cache("SELECT * FROM users")

5. DOSYA FORMATI DONUSUMU:
   # Abstraction: Document Types
   pdf_doc = PDFDocument(converter)
   word_doc = WordDocument(converter)

   # Implementation: Converters
   online_converter = OnlineConverter()
   offline_converter = OfflineConverter()

   pdf_doc.set_converter(online_converter)
   pdf_doc.convert_to("DOCX")

   word_doc.set_converter(offline_converter)
   word_doc.convert_to("PDF")

6. ODEME SISTEMI:
   # Abstraction: Payment Types
   one_time_payment = OneTimePayment(gateway)
   subscription_payment = SubscriptionPayment(gateway)

   # Implementation: Payment Gateways
   stripe_gateway = StripeGateway()
   paypal_gateway = PayPalGateway()

   one_time_payment.set_gateway(stripe_gateway)
   one_time_payment.process(100)

   subscription_payment.set_gateway(paypal_gateway)
   subscription_payment.process_monthly(50)

Bridge vs Adapter:
------------------
- Bridge: Onceden tasarlanir, soyutlama ve uygulamayi ayirir
- Adapter: Sonradan eklenir, uyumsuz arayuzleri uyumlu hale getirir

Asagidaki Ornekte:
------------------
Cuboid (abstraction) sinifi, ProducingAPI1 ve ProducingAPI2 (implementation)
olmak uzere farkli uretim API'leri kullanabilir. Bu sayede Cuboid'in mantigi
ve uretim detaylari birbirinden bagimsiz sekilde degisebilir.
"""

"""Code implemented with Bridge Method.
   We have a Cuboid class having three attributes
   named as length, breadth, and height and three
   methods named as produceWithAPIOne(), produceWithAPItwo(),
   and expand(). Our purpose is to separate out implementation
   specific abstraction from implementation-independent
   abstraction"""


class ProducingAPI1:
    """Implementation specific Abstraction"""

    def produceCuboid(self, length, breadth, height):
        print(f'API1 is producing Cuboid with length = {length}, '
              f' Breadth = {breadth} and Height = {height}')


class ProducingAPI2:
    """Implementation specific Abstraction"""

    def produceCuboid(self, length, breadth, height):
        print(f'API2 is producing Cuboid with length = {length}, '
              f' Breadth = {breadth} and Height = {height}')


class Cuboid:

    def __init__(self, length, breadth, height, producingAPI):
        """Initialize the necessary attributes
           Implementation independent Abstraction"""

        self._length = length
        self._breadth = breadth
        self._height = height

        self._producingAPI = producingAPI

    def produce(self):
        """Implementation specific Abstraction"""

        self._producingAPI.produceCuboid(self._length, self._breadth, self._height)

    def expand(self, times):
        """Implementation independent Abstraction"""

        self._length = self._length * times
        self._breadth = self._breadth * times
        self._height = self._height * times


"""Instantiate a cuboid and pass to it an
   object of ProducingAPIone"""

cuboid1 = Cuboid(1, 2, 3, ProducingAPI1())
cuboid1.produce()

cuboid2 = Cuboid(19, 19, 19, ProducingAPI2())
cuboid2.produce()