"""
VISITOR PATTERN (Ziyaretci Deseni)
===================================

TANIM:
Visitor Pattern, bir nesne yapisindaki elemanlar uzerinde yapilacak yeni operasyonlari,
bu elemanlarin siniflarini degistirmeden tanimlamaniza olanak tanir. Davranissal
(behavioral) bir tasarim desenidir. Double Dispatch mekanizmasi kullanir.

Ne Zaman Kullanilir:
--------------------
- Nesne yapisi karmasik ve nadiren degisiyorsa
- Benzer operasyonlari nesne yapisi uzerinde uygulamak gerektiginde
- Nesne yapisina yeni operasyon eklemek s ik yapiliyorsa
- Algoritmayi veri yapisindan ayirmak istedigimizde
- Open/Closed Principle uygulamak istedigimizde (operasyonlar icin)

Avantajlari:
------------
+ Open/Closed - yeni operasyon eklemek kolay
+ Single Responsibility - ilgili operasyonlar bir arada
+ Birden fazla nesne turunde ayni operasyonu uygulayabilir
+ Visitor state toplayabilir (accumulator pattern)
+ Karmasik operasyonlar nesne disinda tutulur

Dezavantajlari:
--------------
- Yeni eleman turu eklemek zor
- Kapsullemeyi bozabilir (private erisim gerekebilir)
- Circular dependency riski
- Karmasik ve anlasilmasi zor olabilir

Gercek Hayattan Ornekler:
-------------------------
1. DOSYA SISTEMI OPERASYONLARI:
   # Dosya yapisi
   folder = Folder("Documents")
   folder.add(File("report.pdf"))
   folder.add(File("image.jpg"))
   folder.add(Folder("SubFolder"))

   # Farkli ziyaretciler
   size_calculator = SizeCalculatorVisitor()
   folder.accept(size_calculator)
   print(f"Total size: {size_calculator.total_size}")

   virus_scanner = VirusScannerVisitor()
   folder.accept(virus_scanner)

   permission_checker = PermissionCheckerVisitor()
   folder.accept(permission_checker)

2. E-TICARET SEPET HESAPLAMA:
   cart = ShoppingCart()
   cart.add(Book("Python Guide", price=50))
   cart.add(Electronic("Mouse", price=100))
   cart.add(Food("Apple", price=5))

   # Vergi hesapla (her urun farkli vergi orani)
   tax_calculator = TaxCalculatorVisitor()
   cart.accept(tax_calculator)
   print(f"Tax: {tax_calculator.total_tax}")

   # İndirim hesapla
   discount_calculator = DiscountCalculatorVisitor()
   cart.accept(discount_calculator)

   # Kargo hesapla
   shipping_calculator = ShippingCalculatorVisitor()
   cart.accept(shipping_calculator)

3. GRAFIK EDITORU - SEKIL OPERASYONLARI:
   canvas = Canvas()
   canvas.add(Circle(radius=10))
   canvas.add(Rectangle(width=20, height=30))
   canvas.add(Triangle(base=15, height=20))

   # Cesitli operasyonlar
   area_calculator = AreaCalculatorVisitor()
   canvas.accept(area_calculator)

   xml_exporter = XMLExporterVisitor()
   canvas.accept(xml_exporter)

   svg_renderer = SVGRendererVisitor()
   canvas.accept(svg_renderer)

4. COMPILER/AST (Abstract Syntax Tree):
   # Kod agaci
   expression = Add(
       Multiply(Number(2), Number(3)),
       Number(5)
   )

   # Farkli ziyaretciler
   evaluator = EvaluatorVisitor()
   result = expression.accept(evaluator)  # 2*3+5 = 11

   code_generator = CodeGeneratorVisitor()
   code = expression.accept(code_generator)  # "((2 * 3) + 5)"

   optimizer = OptimizerVisitor()
   optimized = expression.accept(optimizer)

5. ORGANIZASYON YAPISI:
   company = Company()
   company.add(Department("IT"))
   company.add(Department("HR"))
   company.add(Employee("John", salary=5000))
   company.add(Employee("Jane", salary=6000))

   # Operasyonlar
   salary_calculator = SalaryCalculatorVisitor()
   company.accept(salary_calculator)
   print(f"Total salary: {salary_calculator.total}")

   report_generator = ReportGeneratorVisitor()
   company.accept(report_generator)

   budget_analyzer = BudgetAnalyzerVisitor()
   company.accept(budget_analyzer)

6. OYUN NESNELERI:
   game_world = GameWorld()
   game_world.add(Enemy("Goblin", health=100))
   game_world.add(Item("Health Potion"))
   game_world.add(NPC("Merchant"))

   # Ziyaretciler
   damage_dealer = DamageDealerVisitor(damage=50)
   game_world.accept(damage_dealer)  # Sadece dusmanlara hasar verir

   collector = ItemCollectorVisitor()
   game_world.accept(collector)  # Itemlari toplar

   dialogue_starter = DialogueVisitor()
   game_world.accept(dialogue_starter)  # NPC'lerle konusur

DIKKAT:
-------
Visitor pattern kullanmadan once, nesne yapisinizin ne kadar sik degisecegini
dusunun. Eger yeni nesne turleri sik ekleniyor ama operasyonlar sabitse,
Visitor pattern UYGUN DEGILDIR. Tersi durumda (yeni operasyonlar sik, yeni
nesne turleri nadir) Visitor pattern idealdir.

Asagidaki Ornekte:
------------------
Kurs sistemi icin visitor pattern ornegi gosterilmektedir.
Instructor ve Student visitor'lari, farkli kurs turlerini (DSA, STL, SDE)
ziyaret eder ve her biri icin farkli islemler yapar.
"""

""" The Courses hierarchy cannot be changed to add new
functionality dynamically. Abstract Crop class for
Concrete Courses_At_GFG classes: methods defined in this class
will be inherited by all Concrete Courses_At_GFG classes."""


class Courses_At_GFG:

    def accept(self, visitor):
        visitor.visit(self)

    def teaching(self, visitor):
        print(self, "Taught by ", visitor)

    def studying(self, visitor):
        print(self, "studied by ", visitor)

    def __str__(self):
        return self.__class__.__name__


"""Concrete Courses_At_GFG class: Classes being visited."""


class SDE(Courses_At_GFG): pass


class STL(Courses_At_GFG): pass


class DSA(Courses_At_GFG): pass


""" Abstract Visitor class for Concrete Visitor classes:
method defined in this class will be inherited by all
Concrete Visitor classes."""


class Visitor:

    def __str__(self):
        return self.__class__.__name__


""" Concrete Visitors: Classes visiting Concrete Course objects.
These classes have a visit() method which is called by the
accept() method of the Concrete Course_At_GFG classes."""


class Instructor(Visitor):
    def visit(self, crop):
        crop.teaching(self)


class Student(Visitor):
    def visit(self, crop):
        crop.studying(self)


"""creating objects for concrete classes"""
sde = SDE()
stl = STL()
dsa = DSA()

"""Creating Visitors"""
instructor = Instructor()
student = Student()

"""Visitors visiting courses"""
sde.accept(instructor)
sde.accept(student)

stl.accept(instructor)
stl.accept(student)

dsa.accept(instructor)
dsa.accept(student)
