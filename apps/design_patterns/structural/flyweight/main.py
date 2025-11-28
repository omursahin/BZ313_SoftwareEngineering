"""
FLYWEIGHT PATTERN (Sinek Siklet Deseni)
========================================

TANIM:
Flyweight Pattern, cok sayida benzer nesne olusturulurken bellek kullanimini
azaltmak icin nesneler arasinda ortak verileri paylastiran yapisal (structural)
bir tasarim desenidir. İcsel (intrinsic) ve dissel (extrinsic) durum ayrimina dayanir.

Ne Zaman Kullanilir:
--------------------
- Cok fazla sayida benzer nesne olusturuluyorsa
- Nesne olusturma maliyeti yuksekse
- Bellek kullanimi kritik oldugunda
- Nesnelerin cogu ozelligi ortaksa
- Nesnelerin kimlik (identity) degil durum (state) onemli oldugunda

Avantajlari:
------------
+ RAM kullanimi azalir
+ Performans artisi saglar
+ Nesne olusturma maliyeti azalir
+ Buyuk olcekli uygulamalarda etkilidir

Dezavantajlari:
--------------
- Kod karmasikligi artar
- CPU dongusu (icsel/dissel ayirma) artar
- Multi-threading icin ekstra dikkat gerekir
- Basit senaryolar icin gereksiz olabilir

Gercek Hayattan Ornekler:
-------------------------
1. METIN EDITORU - KARAKTER RENDERING:
   # Her karakter icin ayri nesne yerine, ayni karakterler ortak nesne kullanir
   # 1 milyon 'a' karakteri = 1 nesne (icsel: font, size, color)
   # Her 'a'nin pozisyonu farkli (dissel: x, y koordinatlari)

   char_factory = CharacterFactory()

   # 'A' karakteri icin bir kere olustur
   a_char = char_factory.get_character('A', font="Arial", size=12)

   # Farkli pozisyonlarda kullan (icsel veri paylasiliyor)
   a_char.display(x=10, y=20)   # Dissel veri
   a_char.display(x=30, y=20)   # Dissel veri
   a_char.display(x=50, y=20)   # Dissel veri

2. OYUN GELISTIRME - AGAC/ORMAN:
   # 10,000 cinar agaci
   tree_factory = TreeFactory()

   # İcsel: model, texture, mesh (ortak)
   pine_tree_type = tree_factory.get_tree_type("Pine", "pine_texture.png")

   # Dissel: x, y, z pozisyonu (her agac farkli)
   forest = []
   for i in range(10000):
       tree = Tree(pine_tree_type, x=random(), y=random(), z=random())
       forest.append(tree)

   # 10,000 nesne yerine 1 ortak TreeType + 10,000 pozisyon

3. STRING POOL (Java):
   # Java'da ayni string'ler ortak nesne kullanir
   str1 = "Hello"  # Yeni nesne
   str2 = "Hello"  # Ayni nesne (str1 == str2)
   str3 = "World"  # Yeni nesne

4. ICON/IMAGE CACHE:
   icon_factory = IconFactory()

   # İcsel: icon image data
   folder_icon = icon_factory.get_icon("folder.png")

   # Her klasor ayni icon'u kullanir (dissel: position, folder_name)
   desktop.draw_icon(folder_icon, "Documents", x=10, y=10)
   desktop.draw_icon(folder_icon, "Downloads", x=10, y=50)
   desktop.draw_icon(folder_icon, "Pictures", x=10, y=90)

5. PARTI KLE SISTEMLERI (Oyunlarda):
   # Binlerce partikul (alevler, duman, yildizlar)
   particle_factory = ParticleFactory()

   # İcsel: sprite, color, size
   spark_type = particle_factory.get_particle("spark")

   # Dissel: position, velocity, lifespan
   particles = []
   for i in range(10000):
       p = Particle(spark_type, pos=(x, y), vel=(vx, vy))
       particles.append(p)

6. VERITABANI BAGLANTI HAVUZU (Connection Pool):
   # Cok sayida baglanti yerine, sinirli baglanti havuzu
   pool = ConnectionPool(max_connections=10)

   # 100 istek geldiginde, 10 baglanti yeniden kullanilir
   for request in requests:
       connection = pool.get_connection()  # Ortak kullan
       connection.execute(request)
       pool.release(connection)  # Havuza geri don

7. WEB TARAYICI - CSS STYLES:
   # Ayni CSS sinifi binlerce HTML eleman inda kullanilabilir
   style_manager = StyleManager()

   # İcsel: CSS properties
   button_style = style_manager.get_style("button-primary")

   # Dissel: text, onClick handler
   button1 = Button(button_style, text="Submit")
   button2 = Button(button_style, text="Cancel")
   button3 = Button(button_style, text="OK")

ICSEL (Intrinsic) vs DISSEL (Extrinsic):
-----------------------------------------
- İcsel: Ortak, degismez, paylasilan veri (renk, font, texture)
- Dissel: Benzersiz, degisen, context'e bagli veri (pozisyon, id)

Asagidaki Ornekte:
------------------
Araba aileleri (CarFamilies) icin flyweight pattern ornegi gosterilmektedir.
Ayni car_family_id'ye sahip arabalar ayni nesneyi (flyweight) kullanir,
boylece bellek tasarrufu saglanir. set_car_info ile dissel veri ayarlanir.
"""

class ComplexCars(object):
    """Separate class for Complex Cars"""

    def __init__(self):
        pass

    def cars(self, car_name):
        return "ComplexPattern[% s]" % (car_name)


class CarFamilies(object):
    """dictionary to store ids of the car"""

    car_family = {}

    def __new__(cls, name, car_family_id):
        try:
            id = cls.car_family[car_family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.car_family[car_family_id] = id
        return id

    def set_car_info(self, car_info):

        """set the car information"""

        cg = ComplexCars()
        self.car_info = cg.cars(car_info)

    def get_car_info(self):

        """return the car information"""

        return (self.car_info)


if __name__ == '__main__':
    car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferrari'), ('b', 1, 'Audi'))
    car_family_objects = []
    for i in car_data:
        obj = CarFamilies(i[0], i[1])
        obj.set_car_info(i[2])
        car_family_objects.append(obj)

    """similar id's says that they are same objects """

    for i in car_family_objects:
        print("id = " + str(id(i)))
        print(i.get_car_info())
