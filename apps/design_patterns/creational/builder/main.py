"""
BUILDER PATTERN (Insaatci/Kurucu Deseni)
=========================================

TANIM:
Builder Pattern, karmasik nesnelerin asamali olarak insa edilmesini saglayan yaratici
(creational) bir tasarim desenidir. Ayni insaat surecini kullanarak farkli temsiller
olusturmaniza olanak tanir.

Ne Zaman Kullanilir:
--------------------
- Nesne olusturma sureci karmasik ve cok adimli oldugunda
- Ayni insaat sureciyle farkli nesne temsilleri olusturulmasi gerektiginde
- Constructor'da cok fazla parametre oldugunda (Telescoping Constructor problemi)
- Nesnenin olusturulma asamalarini kontrol etmek istedigimizde

Avantajlari:
------------
+ Karmasik nesneleri adim adim olusturabilirsiniz
+ Ayni insaat kodunu farkli temsiller icin kullanabilirsiniz
+ Nesne insaasi ile temsili birbirinden ayirir (Single Responsibility)
+ Nesnenin yarim kalmis halinin kullanilmasini onler

Dezavantajlari:
--------------
- Kod karmasikligi artar (birden fazla yeni sinif gerekir)
- Basit nesneler icin gereksiz olabilir

Gercek Hayattan Ornekler:
-------------------------
1. YEM EK SIPARISI (FAST FOOD):
   Burger burger = new BurgerBuilder()
       .addBun("Susam")
       .addPatty("Dana")
       .addCheese()
       .addLettuce()
       .addTomato()
       .build();

2. SQL SORGU OLUSTURUCU:
   Query query = new QueryBuilder()
       .select("name", "email")
       .from("users")
       .where("age > 18")
       .orderBy("name")
       .limit(10)
       .build();

3. DOKUMAN OLUSTURUCU:
   Document doc = new DocumentBuilder()
       .setTitle("Rapor")
       .setAuthor("Ahmet")
       .addParagraph("Giris")
       .addImage("grafik.png")
       .addTable(data)
       .build();

4. BILGISAYAR KONFIGURASYONU:
   Computer pc = new ComputerBuilder()
       .setCPU("Intel i7")
       .setRAM("16GB")
       .setStorage("512GB SSD")
       .setGPU("NVIDIA RTX 3060")
       .build();

Asagidaki Ornekte:
------------------
GeeksforGeeks kurs sistemi icin builder pattern ornegi gosterilmektedir.
Farkli kurs turleri (DSA, SDE, STL) ve karmasik kurslar adim adim olusturulmaktadir.
"""

# Abstract course
class Course:

    def __init__(self):
        self.Fee()
        self.available_batches()

    def Fee(self):
        raise NotImplementedError

    def available_batches(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)


# concrete course
class DSA(Course):
    """Class for Data Structures and Algorithms"""

    def Fee(self):
        self.fee = 8000

    def available_batches(self):
        self.batches = 5

    def __str__(self):
        return "DSA"


# concrete course
class SDE(Course):
    """Class for Software Development Engineer"""

    def Fee(self):
        self.fee = 10000

    def available_batches(self):
        self.batches = 4

    def __str__(self):
        return "SDE"


# concrete course
class STL(Course):
    """Class for Standard Template Library"""

    def Fee(self):
        self.fee = 5000

    def available_batches(self):
        self.batches = 7

    def __str__(self):
        return "STL"


# Complex Course
class ComplexCourse:

    def __repr__(self):
        return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)


# Complex course
class Complexcourse(ComplexCourse):

    def Fee(self):
        self.fee = 7000

    def available_batches(self):
        self.batches = 6


# construct course
def construct_course(cls):
    course = cls()
    course.Fee()
    course.available_batches()

    return course  # return the course object


# main method
if __name__ == "__main__":
    dsa = DSA()  # object for DSA course
    sde = SDE()  # object for SDE course
    stl = STL()  # object for STL course

    complex_course = construct_course(Complexcourse)
    print(complex_course)