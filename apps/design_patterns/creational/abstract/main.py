"""
ABSTRACT FACTORY PATTERN (Soyut Fabrika Deseni)
================================================

TANIM:
Abstract Factory, birbiriyle iliskili veya bagimlı nesne ailelerini somut siniflarini
belirtmeden olusturmak icin bir arayuz saglayan yaratici (creational) bir tasarim desenidir.

Ne Zaman Kullanilir:
--------------------
- Sistem, urunlerinin nasil olusturuldugu, birlestirildiginden bagimsiz olmalidir
- Sistem, birden fazla urun ailesinden biriyle yapilandirilmalidir
- Iliskili urun nesnelerinin birlikte kullanilmasi gerektiginde
- Sadece arayuzleri gostermek ve uygulamalari gizlemek istedigimizde

Avantajlari:
------------
+ Somut siniflardan izole eder
+ Urun aileleri arasinda gecis kolaydir
+ Urunler arasi tutarlilik saglar
+ Single Responsibility Principle'i destekler

Dezavantajlari:
--------------
- Yeni urun turleri eklemek zor olabilir
- Kod karmasikligi artabilir

Gercek Hayattan Ornekler:
-------------------------
1. VERITABANI BAGLANTILARI:
   - MySQL, PostgreSQL, MongoDB icin farkli baglanti fabrikalari
   - Her fabrika kendi Connection, Query, Transaction nesnelerini uretir

2. GUI KUTUPHANELERI:
   - Windows, MacOS, Linux icin farkli UI eleman fabrikalari
   - Her fabrika kendi Button, TextBox, Checkbox'larini olusturur

3. E-TICARET SISTEMLERI:
   - Farkli ulkeler icin odeme sistemleri (TR: Iyzico, US: Stripe, EU: PayPal)
   - Her fabrika kendi Payment, Invoice, Shipping nesnelerini uretir

4. OYUN GELISTIRME:
   - Farkli oyun modlari icin dusman fabrikalari
   - Kolay mod: yavas ve zayif dusmanlar, Zor mod: hizli ve guclu dusmanlar

Asagidaki Ornekte:
------------------
GeeksforGeeks portal icin kurs fabrikasi ornegi gosterilmektedir.
Farkli kurs turleri (DSA, STL, SDE) abstract factory pattern kullanilarak olusturulmaktadir.
"""

# Python Code for object
# oriented concepts using
# the abstract factory
# design pattern

import random


class Course_At_GFG:
    """ GeeksforGeeks portal for courses """

    def __init__(self, courses_factory=None):
        """course factory is out abstract factory"""

        self.course_factory = courses_factory

    def show_course(self):
        """creates and shows courses using the abstract factory"""

        course = self.course_factory()

        print(f'We have a course named {course}')
        print(f'its price is {course.Fee()}')


class DSA:
    """Class for Data Structure and Algorithms"""

    def Fee(self):
        return 11000

    def __str__(self):
        return "DSA"


class STL:
    """Class for Standard Template Library"""

    def Fee(self):
        return 8000

    def __str__(self):
        return "STL"


class SDE:
    """Class for Software Development Engineer"""

    def Fee(self):
        return 15000

    def __str__(self):
        return 'SDE'


def random_course():
    """A random class for choosing the course"""

    return random.choice([SDE, STL, DSA])()


if __name__ == "__main__":

    course = Course_At_GFG(random_course)

    for i in range(5):
        course.show_course()