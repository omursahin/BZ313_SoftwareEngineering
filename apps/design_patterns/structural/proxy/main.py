"""
PROXY PATTERN (Vekil Deseni)
============================

TANIM:
Proxy Pattern, baska bir nesneye erisimi kontrol etmek icin o nesnenin yerine gecen
(vekil) bir nesne saglayan yapisal (structural) bir tasarim desenidir. Proxy, asil
nesneyle ayni arayuzu kullanir ve ekstra islevsellik ekleyebilir.

Ne Zaman Kullanilir:
--------------------
- Nesneye erisimi kontrol etmek istedigimizde
- Lazy initialization (tembel yukleme) gerektiginde
- Agir nesneleri optimize etmek istedigimizde
- Uzak nesnelere erisim saglamak gerektiginde (Remote Proxy)
- Erisim haklari kontrol etmek istedigimizde (Protection Proxy)
- Cache mekanizmasi eklemek istedigimizde (Caching Proxy)

Proxy Turleri:
--------------
1. VIRTUAL PROXY: Agir nesneler icin lazy loading
2. PROTECTION PROXY: Erisim kontrol (authentication, authorization)
3. REMOTE PROXY: Uzak sunucudaki nesneyi temsil eder
4. CACHING PROXY: Sonuclari onbellekte saklar
5. SMART REFERENCE: Referans sayimi, log tutma

Avantajlari:
------------
+ Erisim kontrol saglar
+ Lazy initialization ile performans artisi
+ Gercek nesne hazir olmadan calisabilir
+ Ekstra islevsellik (log, cache) eklenebilir
+ Open/Closed Principle destekler

Dezavantajlari:
--------------
- Yanit suresi artabilir
- Kod karmasikligi artar
- Gereksiz indirection olusabilir

Gercek Hayattan Ornekler:
-------------------------
1. VIRTUAL PROXY - RESIM YUKLEME:
   # Buyuk resim lazy loading ile yuklenir
   image = ImageProxy("large_image_10MB.jpg")

   # Henuz yuklenmedi
   image.display()  # İlk erisimde yuklenir

   # Artik yuklendi, cache'ten gelir
   image.display()  # Hizli

2. PROTECTION PROXY - YETKI KONTROLU:
   # Sadece admin silebilir
   document = DocumentProxy(real_document, user)

   document.view()    # Herkes gorebilir
   document.edit()    # Sadece yazar duzenleyebilir
   document.delete()  # Sadece admin silebilir

   class DocumentProxy:
       def delete(self):
           if self.user.role != "admin":
               raise PermissionError("Admin olmalisiniz!")
           self.real_document.delete()

3. CACHING PROXY - VERITABANI:
   # Sik kullanilan sorgular cache'lenir
   db_proxy = CachedDatabaseProxy(real_db)

   # İlk cagri - veritabanindan gelir
   users = db_proxy.get_all_users()  # 100ms

   # İkinci cagri - cache'ten gelir
   users = db_proxy.get_all_users()  # 1ms

4. REMOTE PROXY - WEB SERVIS:
   # Uzaktaki servisi yerel gibi kullan
   payment_service = PaymentServiceProxy()

   # Arka planda HTTP request yapilir
   payment_service.process_payment(100)

   # Gercekte:
   # - HTTP baglantisi ac
   # - JSON serialize et
   # - POST request gonder
   # - Yaniti parse et
   # - Hatayi handle et

5. SMART REFERENCE - DOSYA ERISIM LOGLAMA:
   file_proxy = LoggingFileProxy("sensitive_data.txt")

   # Her erisim loglaniyor
   file_proxy.read()   # Log: "User X read file at 14:30"
   file_proxy.write()  # Log: "User X wrote file at 14:31"

6. LAZY LOADING - ORM (Object-Relational Mapping):
   # İliskili nesneler lazy yuklenir
   user = User.get(id=1)

   # Posts henuz yuklenmedi
   posts = user.posts  # İlk erisimde database'den yukle

   # Artik yuklendi
   for post in user.posts:  # Cache'ten gelir
       print(post.title)

7. INTERNET PROXY - GUVENLIK DUVARI:
   internet_proxy = InternetProxy()

   # Belirli sitelere erisim engellendi
   internet_proxy.connect("geeksforgeeks.com")  # OK
   internet_proxy.connect("banned-site.com")    # BLOCKED!

8. BAGLANTI HAVUZU (Connection Pool):
   # Gercek baglanti maliyetli, proxy yonetir
   conn_proxy = ConnectionPoolProxy()

   # Havuzdan baglanti al
   conn = conn_proxy.get_connection()
   conn.query("SELECT...")

   # Baglantiyi kapat degil, havuza geri ver
   conn_proxy.release(connection)

Proxy vs Decorator:
-------------------
- Proxy: Erisim kontrol eder, lazy loading yapar
- Decorator: İslevsellik ekler

Proxy vs Adapter:
-----------------
- Proxy: Ayni arayuz kullanir
- Adapter: Farkli arayuzleri uyumlu hale getirir

Proxy vs Facade:
----------------
- Proxy: Tek nesneyi temsil eder
- Facade: Alt sistem grubunu basitlestirir

Asagidaki Ornekte:
------------------
Universite sistemi icin protection proxy ornegi gosterilmektedir.
CollegeProxy, ogrencinin ucret bakiyesini kontrol eder. Bakiye
500'den fazlaysa College nesnesine erisime izin vermez.
"""

class College:
    '''Resource-intensive object'''

    def studyingInCollege(self):
        print("Studying In College....")


class CollegeProxy:
    '''Relatively less resource-intensive proxy acting as middleman.
    Instantiates a College object only if there is no fee due.'''

    def __init__(self):

        self.feeBalance = 1000
        self.college = None

    def studyingInCollege(self):

        print("Proxy in action. Checking to see if the balance of student is clear or not...")
        if self.feeBalance <= 500:
            # If the balance is less than 500, let him study.
            self.college = College()
            self.college.studyingInCollege()
        else:

            # Otherwise, don't instantiate the college object.
            print("Your fee balance is greater than 500, first pay the fee")


"""main method"""

if __name__ == "__main__":
    # Instantiate the Proxy
    collegeProxy = CollegeProxy()

    # Client attempting to study in the college at the default balance of 1000.
    # Logically, since he / she cannot study with such balance,
    # there is no need to make the college object.
    collegeProxy.studyingInCollege()

    # Altering the balance of the student
    collegeProxy.feeBalance = 100

    # Client attempting to study in college at the balance of 100. Should succeed.
    collegeProxy.studyingInCollege()
