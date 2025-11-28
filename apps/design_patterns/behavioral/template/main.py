"""
TEMPLATE METHOD PATTERN (Sablon Metod Deseni)
==============================================

TANIM:
Template Method, bir algoritmanin iskeletini (skeleton) tanimlar ve bazi adimlari
alt siniflara birakir. Alt siniflar, algoritmanin yapisini degistirmeden belirli
adimlari yeniden tanimlayabilir. Davranissal (behavioral) bir tasarim desenidir.

Ne Zaman Kullanilir:
--------------------
- Algoritmanin genel yapisi sabitse ama detaylar degisiyorsa
- Benzer algoritmalarda kod tekrarini onlemek istedigimizde
- Alt siniflarin sadece belirli adimlari degistirmesi gerektiginde
- Hook (kanca) metodlari saglamak istedigimizde
- Inversion of Control (Hollywood Principle: "Don't call us, we'll call you")

Avantajlari:
------------
+ Kod tekrarini azaltir
+ Algoritma akisi kontrol altinda
+ Sadece degisen kisimlar override edilir
+ Framework gelistirmede cok kullanislidir
+ Open/Closed Principle destekler

Dezavantajlari:
--------------
- Alt siniflar ust sinifa sikica bagimli
- Template method cok fazla adim icerirse karmasiklas ir
- Liskov Substitution Principle ihlaline neden olabilir
- Debugging zor olabilir

Gercek Hayattan Ornekler:
-------------------------
1. SICAK ICECEK HAZIRLAMA:
   class BeverageTemplate:
       def prepare(self):
           self.boil_water()
           self.brew()           # Alt sinifta tanimlanir
           self.pour_in_cup()
           self.add_condiments()  # Alt sinifta tanimlanir

   class Tea(BeverageTemplate):
       def brew(self):
           print("Cay demirleniyor")

       def add_condiments(self):
           print("Limon ekleniyor")

   class Coffee(BeverageTemplate):
       def brew(self):
           print("Kahve demleniyor")

       def add_condiments(self):
           print("Sut ve seker ekleniyor")

   tea = Tea()
   tea.prepare()  # Template metod akisi takip eder

2. VERI MADENCILIGI (Data Mining):
   class DataMiner:
       def mine(self, path):
           data = self.open_file(path)
           raw_data = self.extract_data(data)  # Alt sinif implement eder
           analysis = self.analyze(raw_data)    # Alt sinif implement eder
           self.send_report(analysis)

   class PDFDataMiner(DataMiner):
       def extract_data(self, file):
           # PDF'den veri cek

   class CSVDataMiner(DataMiner):
       def extract_data(self, file):
           # CSV'den veri cek

3. OYUN SEVIYE YUKLEME:
   class GameLevel:
       def load_level(self):
           self.load_background()
           self.load_characters()   # Alt sinif ozellestirir
           self.load_obstacles()    # Alt sinif ozellestirir
           self.load_music()
           self.start_level()

   class Level1(GameLevel):
       def load_characters(self):
           # Seviye 1 karakterleri

   class Level2(GameLevel):
       def load_characters(self):
           # Seviye 2 karakterleri

4. WEB SCRAPING:
   class WebScraper:
       def scrape(self, url):
           html = self.download_page(url)
           parsed = self.parse_html(html)     # Alt sinif implement eder
           data = self.extract_data(parsed)   # Alt sinif implement eder
           self.save_data(data)

   class AmazonScraper(WebScraper):
       def parse_html(self, html):
           # Amazon'a ozel parsing

   class EbayScraper(WebScraper):
       def parse_html(self, html):
           # eBay'e ozel parsing

5. UNIT TEST FRAMEWORK:
   class TestCase:
       def run_test(self):
           self.setup()           # Hook metod (opsiyonel)
           self.test()            # Alt sinif implement eder
           self.tear_down()       # Hook metod (opsiyonel)

   class DatabaseTest(TestCase):
       def setup(self):
           self.db = connect_to_test_db()

       def test(self):
           # Test kodlari

       def tear_down(self):
           self.db.close()

6. DOSYA DISA AKTARMA:
   class DataExporter:
       def export(self, data):
           formatted_data = self.format_data(data)  # Alt sinif yapar
           self.write_header()                      # Hook metod
           self.write_data(formatted_data)
           self.write_footer()                      # Hook metod

   class PDFExporter(DataExporter):
       def format_data(self, data):
           # PDF formatina cevir

   class ExcelExporter(DataExporter):
       def format_data(self, data):
           # Excel formatina cevir

Asagidaki Ornekte:
------------------
Dosya isleme icin template method pattern ornegi gosterilmektedir.
template_function genel akisi belirler, getter ve converter
parametreler olarak gecirilir (strategy pattern benzeri).
"""

""" method to get the text of file"""


def get_text():
    return "plain_text"


""" method to get the xml version of file"""


def get_xml():
    return "xml"


""" method to get the pdf version of file"""


def get_pdf():
    return "pdf"


"""method to get the csv version of file"""


def get_csv():
    return "csv"


"""method used to convert the data into text format"""


def convert_to_text(data):
    print("[CONVERT]")
    return "{} as text".format(data)


"""method used to save the data"""


def saver():
    print("[SAVE]")


"""helper function named as template_function"""


def template_function(getter, converter=False, to_save=False):
    """input data from getter"""
    data = getter()
    print("Got `{}`".format(data))

    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skip conversion")

    """saves the data only if user want to save it"""
    if to_save:
        saver()

    print("`{}` was processed".format(data))


"""main method"""
if __name__ == "__main__":
    template_function(get_text, to_save=True)

    template_function(get_pdf, converter=convert_to_text)

    template_function(get_csv, to_save=True)

    template_function(get_xml, to_save=True)
