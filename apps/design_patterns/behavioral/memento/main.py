"""
MEMENTO PATTERN (Ani/Hatira Deseni)
====================================

TANIM:
Memento Pattern, bir nesnenin onceki durumunu kapsulleme (encapsulation) ilkesini
bozmadan kaydedip geri yuklenmesini saglayan davranissal (behavioral) bir tasarim
desenidir. "Snapshot" veya "Undo" mekanizmasi implementasyonu icin kullanilir.

Ne Zaman Kullanilir:
--------------------
- Nesnenin onceki durumunu kaydetmek gerektiginde
- Undo/Redo (geri al/yeniden yap) ozelligi eklemek istedigimizde
- Snapshot olusturma ihtiyaci oldugunda
- Dogrudan erisimin kapsullemeyi bozacagi durumlarda
- Transaction rollback gerektiginde

Avantajlari:
------------
+ Kapsullemeyi bozmaz
+ Nesnenin ic durumunu korur
+ Basit undo/redo mekanizmasi
+ Snapshot mekanizmasi kolay
+ Single Responsibility Principle

Dezavantajlari:
--------------
- Cok fazla memento bellek sorunlarina yol acabebilir
- Memento olusturma maliyeti yuksek olabilir
- Caretaker'in yasam dongusu karmasik olabilir
- Dikkatli yonetilmezse bellek sizintisi riski

Gercek Hayattan Ornekler:
-------------------------
1. METIN EDITORU UNDO/REDO:
   editor = TextEditor()
   history = EditorHistory()

   # Metin yaz
   editor.write("Merhaba ")
   history.save(editor)  # Durumu kaydet

   editor.write("Dunya")
   history.save(editor)

   editor.write("!!!")

   # Geri al
   history.undo(editor)  # "Merhaba Dunya"
   history.undo(editor)  # "Merhaba "

2. OYUN KAYIT SISTEMI (Save/Load):
   game = Game()

   # Oyun ilerliyor
   game.player.position = (100, 200)
   game.player.health = 75
   game.level = 5

   # Kayit noktasi
   save_manager = SaveManager()
   save_manager.save(game)  # Checkpoint

   # Oyun devam ediyor
   game.player.health = 0  # Oldu

   # Kaydi yukle
   save_manager.load(game)  # Checkpoint'e don

3. VERITABANI TRANSACTION:
   transaction = DatabaseTransaction()

   # Islemler
   transaction.execute("INSERT INTO users ...")
   transaction.save_point("sp1")

   transaction.execute("UPDATE accounts ...")
   transaction.save_point("sp2")

   transaction.execute("DELETE FROM logs ...")

   # Hata olustu, rollback
   transaction.rollback_to("sp2")  # Son UPDATE'e don

4. FORM DURUM YONETIMI:
   form = ComplexForm()
   form_history = FormHistory()

   # Kullanici formu dolduruyor
   form.set_field("name", "Ahmet")
   form_history.save(form)

   form.set_field("email", "ahmet@example.com")
   form_history.save(form)

   form.set_field("phone", "invalid")  # Yanlis

   # Onceki hale don
   form_history.undo(form)

5. GRAFIK EDITORU:
   canvas = Canvas()
   canvas_history = CanvasHistory()

   # Cizim islemleri
   canvas.draw_circle(x=10, y=20, r=5)
   canvas_history.save(canvas)

   canvas.draw_rectangle(x=50, y=60, w=100, h=50)
   canvas_history.save(canvas)

   canvas.draw_line(...)

   # Ctrl+Z (undo)
   canvas_history.undo(canvas)

6. KONFIGURASYON YONETIMI:
   config = AppConfig()
   config_backup = ConfigBackup()

   # Mevcut konfigurasyonu kaydet
   config_backup.backup(config)

   # Deneysel degisiklikler
   config.set("api_endpoint", "https://test.api.com")
   config.set("timeout", 5000)

   # İşe yaramadi, eski haline don
   config_backup.restore(config)

Asagidaki Ornekte:
------------------
Dosya yazma islemleri icin memento pattern ornegi gosterilmektedir.
FileWriterUtility ile yapilan degisiklikler Memento'larda saklanir
ve CareTaker vasitasiyla geri alinabilir (undo).
"""

"""Memento class for saving the data"""


class Memento:
    """Constructor function"""

    def __init__(self, file, content):
        """put all your file content here"""

        self.file = file
        self.content = content


"""It's a File Writing Utility"""


class FileWriterUtility:
    """Constructor Function"""

    def __init__(self, file):
        """store the input file data"""
        self.file = file
        self.content = ""

    """Write the data into the file"""

    def write(self, string):
        self.content += string

    """save the data into the Memento"""

    def save(self):
        return Memento(self.file, self.content)

    """UNDO feature provided"""

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


"""CareTaker for FileWriter"""


class FileWriterCaretaker:
    """saves the data"""

    def save(self, writer):
        self.obj = writer.save()

    """undo the content"""

    def undo(self, writer):
        writer.undo(self.obj)


if __name__ == '__main__':
    """create the caretaker object"""
    caretaker = FileWriterCaretaker()

    """create the writer object"""
    writer = FileWriterUtility("GFG.txt")

    """write data into file using writer object"""
    writer.write("First vision of GeeksforGeeks\n")
    print(writer.content + "\n\n")

    """save the file"""
    caretaker.save(writer)

    """again write using the writer """
    writer.write("Second vision of GeeksforGeeks\n")

    print(writer.content + "\n\n")

    """undo the file"""
    caretaker.undo(writer)

    print(writer.content + "\n\n")
