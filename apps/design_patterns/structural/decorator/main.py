"""
DECORATOR PATTERN (Dekorator/Suslayici Deseni)
===============================================

TANIM:
Decorator Pattern, bir nesneye dinamik olarak yeni sorumluluklar ekleyen yapisal
(structural) bir tasarim desenidir. Decorator'lar, alt sinif olusturmaya esnek bir
alternatif saglarlar ve islev genisletme icin kullanilir.

Ne Zaman Kullanilir:
--------------------
- Runtime'da nesnelere sorumluluk eklemek gerektiginde
- Miras almadan (inheritance) islev eklemek istedigimizde
- Alt sinif patlamas ini (subclass explosion) onlemek istedigimizde
- Nesneleri sararak (wrapping) yeni davranislar eklemek gerektiginde
- Sorumluluklar geri alinabilir olmalidir

Avantajlari:
------------
+ Open/Closed Principle - yeni decorator'lar kolayca eklenebilir
+ Single Responsibility - her decorator bir sorumluluk ekler
+ Runtime'da davranis degistirilebilir
+ Birden fazla decorator birlestirilebilir (chain)
+ Miras yerine composition kullanir

Dezavantajlari:
--------------
- Cok fazla kucuk nesne olusur
- Decorator siralamasi onemlidir
- Debug edilmesi zor olabilir (cok katman)
- Sarmalanan nesneye dogrudan erisim kaybolur

Gercek Hayattan Ornekler:
-------------------------
1. KAHVE SIPARISI:
   # Temel kahve
   coffee = SimpleCoffee()  # 10 TL

   # Suriye gore eklemeler
   coffee = MilkDecorator(coffee)     # +5 TL
   coffee = SugarDecorator(coffee)    # +2 TL
   coffee = WhippedCreamDecorator(coffee)  # +7 TL

   print(coffee.cost())  # 24 TL
   print(coffee.description())  # "Simple Coffee, Milk, Sugar, Whipped Cream"

2. INPUT/OUTPUT STREAM (Java):
   # Dosyadan okuma + Buffering + Compression
   file = FileInputStream("data.txt")
   buffered = BufferedInputStream(file)
   compressed = GzipInputStream(buffered)

   data = compressed.read()

3. GUI KOMPONENTLERI - SCROLL VE BORDER:
   # Text Area
   text_area = TextArea()

   # Kaydirma cubugu ekle
   with_scroll = ScrollDecorator(text_area)

   # Cerceve ekle
   with_border = BorderDecorator(with_scroll)

   # Golge ekle
   final_widget = ShadowDecorator(with_border)

   final_widget.render()

4. METIN FORMATLAMA:
   text = PlainText("Merhaba")

   # Farkli formatlari uygula
   bold_text = BoldDecorator(text)
   italic_text = ItalicDecorator(bold_text)
   underline_text = UnderlineDecorator(italic_text)

   print(underline_text.render())
   # "<u><i><b>Merhaba</b></i></u>"

5. BILDIRIM SISTEMI:
   # Temel bildirim
   notifier = EmailNotifier()

   # Ekstra kanallar ekle
   notifier = SMSDecorator(notifier)
   notifier = SlackDecorator(notifier)
   notifier = PushNotificationDecorator(notifier)

   notifier.send("Onemli bildirim!")
   # Email, SMS, Slack ve Push ile gonder

6. SIFRELEME VE SIKISTIRMA:
   # Veri kayit pipeline'i
   data_source = FileDataSource("data.txt")

   # Sifreleme katmani
   encrypted = EncryptionDecorator(data_source)

   # Sikistirma katmani
   compressed = CompressionDecorator(encrypted)

   compressed.write_data("Gizli veri")
   # Veri sifrelenir, sikistirilir ve kaydedilir

7. WEB ISTEKLERI - MIDDLEWARE:
   # HTTP request
   request = HTTPRequest()

   # Katmanlar ekle
   request = AuthenticationDecorator(request)
   request = LoggingDecorator(request)
   request = RateLimitDecorator(request)
   request = CacheDecorator(request)

   response = request.execute()

Decorator vs Inheritance:
-------------------------
- Decorator: Runtime'da dinamik, composition kullanir
- Inheritance: Compile-time'da statik, miras kullanir

Decorator vs Proxy:
-------------------
- Decorator: İslevsellik ekler
- Proxy: Erisim kontrol eder veya lazy loading yapar

Asagidaki Ornekte:
------------------
Metin formatlama icin decorator pattern ornegi gosterilmektedir.
WrittenText nesnesine UnderlineWrapper, ItalicWrapper ve BoldWrapper
decorator'lari eklenerek HTML tagleri ile sarmalanmistir.
"""

class WrittenText:
    """Represents a Written text """

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class UnderlineWrapper(WrittenText):
    """Wraps a tag in <u>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<u>{}</u>".format(self._wrapped.render())


class ItalicWrapper(WrittenText):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


class BoldWrapper(WrittenText):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


""" main method """

if __name__ == '__main__':
    before_gfg = WrittenText("GeeksforGeeks")
    after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

    print("before :", before_gfg.render())
    print("after :", after_gfg.render())
