"""
PROTOTYPE PATTERN (Prototip Deseni)
====================================

TANIM:
Prototype Pattern, mevcut nesneleri klonlayarak yeni nesneler olusturmaya yarayan
yaratici (creational) bir tasarim desenidir. Bu desen, nesnelerin tam bir kopyasini
olusturmak icin kullanilir ve nesne olusturma maliyetini azaltir.

Ne Zaman Kullanilir:
--------------------
- Nesne olusturma maliyeti yuksek oldugunda (veritabani sorgusu, agir hesaplamalar)
- Benzer nesneler olusturulmasi gerektiginde
- Siniflar runtime'da dinamik olarak yuklendigi nde
- Alt sinif sayisini azaltmak istedigimizde
- Nesne olusturma sureci karmasik oldugunda

Avantajlari:
------------
+ Performans artisi (mevcut nesne kopyalanir, sifirdan olusturulmaz)
+ Alt sinif sayisini azaltir
+ Runtime'da nesne ekleme/cik arma kolayligi
+ Karmasik nesneleri kolayca kopyalayabilme
+ Alternative to subclassing

Dezavantajlari:
--------------
- Dongusal referanslar iceren nesneleri klonlamak zor olabilir
- Deep copy vs Shallow copy karisikligi
- Her sinif clone metodu implement etmelidir

Gercek Hayattan Ornekler:
-------------------------
1. OYUN GELISTIRME - Dusman Kopyalama:
   # Temel bir dusman olustur ve ozellikleri ayarla
   base_enemy = Enemy("Goblin", health=100, damage=10)

   # Ayni ozelliklere sahip 50 dusman kopyala
   enemies = [base_enemy.clone() for _ in range(50)]

2. DOKUMAN SABLONLARI:
   # Standart bir sozlesme sablonu
   contract_template = Document("Sozlesme Sablonu")
   contract_template.add_header()
   contract_template.add_footer()

   # Her musteri icin kopyala ve ozelleştir
   customer_contract = contract_template.clone()
   customer_contract.set_customer("Ahmet Yilmaz")

3. GRAFIK EDITORU - Sekil Kopyalama:
   # Karmasik bir sekil olustur
   complex_shape = Shape()
   complex_shape.add_gradient()
   complex_shape.add_shadow()
   complex_shape.add_border()

   # Ayni ozelliklere sahip kopyalar olustur
   shape_copy1 = complex_shape.clone()
   shape_copy2 = complex_shape.clone()

4. VERITABANI BAGLANTISI:
   # Varsayilan ayarlara sahip baglanti
   db_template = DatabaseConnection("localhost", port=5432)

   # Farkli veritabanlari icin kopyala
   db1 = db_template.clone()
   db1.set_database("users_db")

   db2 = db_template.clone()
   db2.set_database("products_db")

Asagidaki Ornekte:
------------------
GeeksforGeeks kurs sistemi icin prototype pattern ornegi gosterilmektedir.
Kurs nesneleri bir cache'te saklanir ve gerektiginde klonlanarak yeni nesneler
olusturulur. Bu sayede her seferinde yeni nesne olusturma maliyeti onlenir.
"""

# import the required modules

from abc import ABCMeta, abstractmethod
import copy


# class - Courses at GeeksforGeeks
class Courses_At_GFG(metaclass=ABCMeta):

    # constructor
    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


# class - DSA course
class DSA(Courses_At_GFG):
    def __init__(self):
        super().__init__()
        self.type = "Data Structures and Algorithms"

    def course(self):
        print("Inside DSA::course() method")


# class - SDE Course
class SDE(Courses_At_GFG):
    def __init__(self):
        super().__init__()
        self.type = "Software Development Engineer"

    def course(self):
        print("Inside SDE::course() method.")


# class - STL Course
class STL(Courses_At_GFG):
    def __init__(self):
        super().__init__()
        self.type = "Standard Template Library"

    def course(self):
        print("Inside STL::course() method.")


# class - Courses At GeeksforGeeks Cache
class Courses_At_GFG_Cache:
    # cache to store useful information
    cache = {}

    @staticmethod
    def get_course(sid):
        COURSE = Courses_At_GFG_Cache.cache.get(sid, None)
        return COURSE.clone()

    @staticmethod
    def load():
        sde = SDE()
        sde.set_id("1")
        Courses_At_GFG_Cache.cache[sde.get_id()] = sde

        dsa = DSA()
        dsa.set_id("2")
        Courses_At_GFG_Cache.cache[dsa.get_id()] = dsa

        stl = STL()
        stl.set_id("3")
        Courses_At_GFG_Cache.cache[stl.get_id()] = stl


# main function
if __name__ == '__main__':
    Courses_At_GFG_Cache.load()

    sde = Courses_At_GFG_Cache.get_course("1")
    print(sde.get_type())

    dsa = Courses_At_GFG_Cache.get_course("2")
    print(dsa.get_type())

    stl = Courses_At_GFG_Cache.get_course("3")
    print(stl.get_type())