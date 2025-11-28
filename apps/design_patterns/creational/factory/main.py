"""
FACTORY METHOD PATTERN (Fabrika Metodu Deseni)
===============================================

TANIM:
Factory Method, ust sinifta nesneler olusturmak icin bir arayuz tanimlar, ancak
alt siniflarin olusturulacak nesne turunu degistirmesine izin verir. Bu yaratici
(creational) bir tasarim desenidir.

Ne Zaman Kullanilir:
--------------------
- Olus turacak nesnenin tam turunu onceden bilemedigimizde
- Nesne olusturma mantigi karmasik oldugunda
- Nesne olusturmayi merkezilestirmek istedigimizde
- Sinif, olusturacagi nesnelerin sorumluluklarini alt siniflara devretmek istediginde

Avantajlari:
------------
+ Gevşek baglanti (Loose Coupling) saglar
+ Yeni turleri eklemek kolay (Open/Closed Principle)
+ Kod tekrarini azaltir
+ Nesne olusturmayi merkezilestiri r
+ Test edilebilirlik artar

Dezavantajlari:
--------------
- Basit durumlar icin asiri karmasik olabilir
- Cok fazla alt sinif gerektirebilir

Gercek Hayattan Ornekler:
-------------------------
1. LOJISTIK SISTEMI:
   # Deniz ve kara lojistik icin fabrika
   transport = TransportFactory.create("Sea")  # Ship nesnesi doner
   transport = TransportFactory.create("Road") # Truck nesnesi doner

2. ODEME SISTEMLERI:
   # Kredi karti, PayPal, Kripto odeme
   payment = PaymentFactory.create("CreditCard")
   payment = PaymentFactory.create("PayPal")
   payment = PaymentFactory.create("Crypto")

3. DOKUMAN OLUSTURUCU:
   # PDF, Word, Excel dokumanlari
   doc = DocumentFactory.create("PDF")
   doc = DocumentFactory.create("Word")

4. VERITABANI BAGLANTILARI:
   # MySQL, PostgreSQL, MongoDB
   db = DatabaseFactory.create("MySQL")
   connection = db.connect()

5. BILDIRIM SISTEMI:
   # Email, SMS, Push Notification
   notification = NotificationFactory.create("Email")
   notification.send("Mesaj")

Asagidaki Ornekte:
------------------
Dil yerellestirme (localization) sistemi icin factory method ornegi gosterilmektedir.
Farkli diller icin (French, Spanish, English) localizer nesneleri fabrika metodu
kullanilarak olusturulmaktadir.
"""

# Python Code for factory method
# it comes under the creational
# Design Pattern

class FrenchLocalizer:
    """ it simply returns the french version """

    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle": "cyclette"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle": "ciclo"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg


def Factory(language="English"):
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()


if __name__ == "__main__":

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))