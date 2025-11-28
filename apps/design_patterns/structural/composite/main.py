"""
COMPOSITE PATTERN (Birlesik/Bilesik Deseni)
============================================

TANIM:
Composite Pattern, nesneleri agac yapilarina organize ederek "parca-butun" (part-whole)
hiyerarsilerini temsil etmeyi saglar. Istemcilerin tekil nesneler ve nesne bilesimlerini
ayni sekilde ele almasina olanak tanir. Yapisal (structural) bir tasarim desenidir.

Ne Zaman Kullanilir:
--------------------
- Nesnelerin agac yapisi seklinde hiyerarsisi varsa
- İstemciler tekil ve bilesik nesneleri ayni sekilde ele almalidir
- Parca-butun hiyerarsisi temsil edilmek istendiginde
- Recursive (oz yinelemeli) yapi gerektiren durumlarda
- Grup islemleri tekil islemler gibi calisilmalidir

Avantajlari:
------------
+ Open/Closed - yeni eleman turleri kolayca eklenebilir
+ Tekil ve bilesik nesneler ayni arayuzu kullanir
+ Agac yapilari kolay yonetilir
+ Kod basitligini arttirir (if-else gerekmez)
+ Recursive operasyonlar kolaydir

Dezavantajlari:
--------------
- Genel tasarim cok genelleyici olabilir
- Sadece belirli tipleri kisitlamak zor olabilir
- Uygun olmayan yerlerde kullanilirsa karmasiklasa bilir

Gercek Hayattan Ornekler:
-------------------------
1. DOSYA SISTEMI:
   # Klasorler ve dosyalar
   root = Folder("Root")
   documents = Folder("Documents")
   file1 = File("resume.pdf", 1024)
   file2 = File("photo.jpg", 2048)

   documents.add(file1)
   documents.add(file2)
   root.add(documents)

   # Butun agac icin boyut hesapla
   total_size = root.get_size()  # Recursive olarak hesaplanir

2. GRAFIK EDITOR - SEKILLER:
   # Sekilleri gruplayabilme
   group1 = Group()
   group1.add(Circle(x=10, y=20))
   group1.add(Rectangle(x=30, y=40))

   group2 = Group()
   group2.add(Line(x1=0, y1=0, x2=100, y2=100))
   group2.add(group1)  # Grup icinde grup!

   # Tum grubu tek seferde tasi/olcekle/dondur
   group2.move(dx=50, dy=50)
   group2.scale(2.0)

3. ORGANIZASYON YAPISI:
   # Sirket hiyerarsisi
   ceo = Employee("CEO", salary=200000)

   cto = Employee("CTO", salary=150000)
   engineering_manager = Employee("Eng Manager", salary=120000)
   developer1 = Employee("Developer 1", salary=80000)
   developer2 = Employee("Developer 2", salary=80000)

   engineering_manager.add(developer1)
   engineering_manager.add(developer2)
   cto.add(engineering_manager)
   ceo.add(cto)

   # Toplam maas hesapla (butun organizasyon)
   total_salary = ceo.get_total_salary()

4. GUI KOMPONENTLERI:
   # Panel icinde paneller ve widgetlar
   main_window = Window()
   sidebar = Panel()
   content_panel = Panel()

   sidebar.add(Button("Home"))
   sidebar.add(Button("Settings"))

   content_panel.add(TextArea())
   content_panel.add(ImageView())

   main_window.add(sidebar)
   main_window.add(content_panel)

   # Tum window'u render et
   main_window.render()  # Her cocuk kendi kendini render eder

5. MENU SISTEMI:
   # Menu ve alt menuler
   file_menu = Menu("File")
   file_menu.add(MenuItem("New"))
   file_menu.add(MenuItem("Open"))

   save_submenu = Menu("Save")
   save_submenu.add(MenuItem("Save"))
   save_submenu.add(MenuItem("Save As"))
   file_menu.add(save_submenu)

   menubar = MenuBar()
   menubar.add(file_menu)

   # Tum menu'yu goster
   menubar.display()

6. E-TICARET SEPETI:
   # Urunler ve urun gruplari
   electronics = ProductGroup("Electronics")
   electronics.add(Product("Laptop", 5000))
   electronics.add(Product("Mouse", 100))

   books = ProductGroup("Books")
   books.add(Product("Python Guide", 50))
   books.add(Product("Design Patterns", 60))

   cart = ShoppingCart()
   cart.add(electronics)
   cart.add(books)

   # Toplam fiyat
   total_price = cart.get_total_price()

7. MATEMATIKSEL IFADELER:
   # (2 + 3) * (4 - 1)
   add = Add(Number(2), Number(3))
   sub = Subtract(Number(4), Number(1))
   multiply = Multiply(add, sub)

   result = multiply.evaluate()  # 15

Composite vs Decorator:
-----------------------
- Composite: Birden fazla cocuk nesne icerir (agac yapisi)
- Decorator: Tek bir nesneyi sarar (zincir yapisi)

Asagidaki Ornekte:
------------------
Organizasyon hiyerarsisi ornegi gosterilmektedir.
GeneralManager (Composite), Manager'lari (Composite) icerir.
Manager'lar Developer'lari (Leaf) icerir. showDetails() metodu
recursive olarak tum hiyerarsiyi gosterir.
"""

"""Here we attempt to make an organizational hierarchy with sub-organization,
which may have subsequent sub-organizations, such as:
GeneralManager								 [Composite]
	Manager1								 [Composite]
			Developer11					 [Leaf]
			Developer12					 [Leaf]
	Manager2								 [Composite]
			Developer21					 [Leaf]
			Developer22					 [Leaf]"""


class LeafElement:
    '''Class representing objects at the bottom or Leaf of the hierarchy tree.'''

    def __init__(self, *args):
        ''''Takes the first positional argument and assigns to member variable "position".'''
        self.position = args[0]

    def showDetails(self):
        '''Prints the position of the child element.'''
        print("\t", end="")
        print(self.position)


class CompositeElement:
    '''Class representing objects at any level of the hierarchy
    tree except for the bottom or leaf level. Maintains the child
    objects by adding and removing them from the tree structure.'''

    def __init__(self, *args):
        '''Takes the first positional argument and assigns to member
        variable "position". Initializes a list of children elements.'''
        self.position = args[0]
        self.children = []

    def add(self, child):
        '''Adds the supplied child element to the list of children
        elements "children".'''
        self.children.append(child)

    def remove(self, child):
        '''Removes the supplied child element from the list of
        children elements "children".'''
        self.children.remove(child)

    def showDetails(self):
        '''Prints the details of the component element first. Then,
        iterates over each of its children, prints their details by
        calling their showDetails() method.'''
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()


"""main method"""

if __name__ == "__main__":
    topLevelMenu = CompositeElement("GeneralManager")
    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")
    subMenuItem11 = LeafElement("Developer11")
    subMenuItem12 = LeafElement("Developer12")
    subMenuItem21 = LeafElement("Developer21")
    subMenuItem22 = LeafElement("Developer22")
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem22)

    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()
