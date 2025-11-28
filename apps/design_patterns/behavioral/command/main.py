"""
COMMAND PATTERN (Komut Deseni)
===============================

TANIM:
Command Pattern, bir istegi nesne olarak kapsuller (encapsulate), boylece kullanicilari
farkli istekler, kuyruklar veya log istekleri ile parametrize edebilir ve geri alinamaz
islemleri destekleyebilirsiniz. Bu davranissal (behavioral) bir tasarim desenidir.

Ne Zaman Kullanilir:
--------------------
- İşlemleri nesneler olarak temsil etmek istedigimizde
- İşlemleri kuyruga almak, zamanlamak veya uzaktan calistirmak gerektiginde
- Geri alma (undo) / yeniden yapma (redo) islemleri desteklemek istedigimizde
- İşlem gecmisini kaydetmek (logging) gerektiginde
- Callback islevselligine ihtiyac duyuldugunda
- Makro islemler (birden fazla komutu birlestirme) olusturmak istedigimizde

Avantajlari:
------------
+ Single Responsibility - komutlari cagiran ve calistiran kodlari ayirir
+ Open/Closed - yeni komutlar kolayca eklenebilir
+ Geri alma/yeniden yapma (undo/redo) implementasyonu kolay
+ Karmasik komutlar basit komutlardan olusturulabilir
+ Ertelenm is islem (deferred execution) destegi
+ İşlem gecmisi tutulabilir (logging)

Dezavantajlari:
--------------
- Kod karmasikligi artar (her islem icin yeni sinif)
- Basit islemler icin gereksiz olabilir
- Cok fazla kucuk sinif olusturulabilir

Gercek Hayattan Ornekler:
-------------------------
1. METIN EDITORU UNDO/REDO:
   editor = TextEditor()

   # Her islem bir komut
   copy_command = CopyCommand(editor, text="Merhaba")
   paste_command = PasteCommand(editor)
   delete_command = DeleteCommand(editor, start=0, end=5)

   # Komutlari calistir
   copy_command.execute()
   paste_command.execute()

   # Geri al
   paste_command.undo()

2. RESTAURANT SIPARIS SISTEMI:
   # Musteriden gelen siparisler Command olarak temsil edilir
   order1 = OrderCommand(table=5, items=["Pizza", "Kola"])
   order2 = OrderCommand(table=3, items=["Burger", "Patates"])

   # Siparisler kuyruga alinir
   kitchen_queue.add(order1)
   kitchen_queue.add(order2)

   # Mutfak siparisleri isler
   kitchen_queue.execute_next()

3. AKILLI EV SISTEMLERI:
   # Cesitli cihaz komutlari
   light_on = LightOnCommand(living_room_light)
   tv_on = TVOnCommand(tv)
   ac_set = SetTemperatureCommand(ac, temperature=22)

   # Makro komut - "Eve geldim"
   arriving_home = MacroCommand([light_on, tv_on, ac_set])

   # Tek tusla tum komutlari calistir
   remote_control.set_command(1, arriving_home)
   remote_control.press_button(1)

4. OYUN KONTROLLERI:
   # Her tus basimi bir komut
   jump_command = JumpCommand(player)
   attack_command = AttackCommand(player)
   move_command = MoveCommand(player, direction="forward")

   # Tus basimlarini kaydet (replay icin)
   game_recorder.record(jump_command)
   game_recorder.record(attack_command)

   # Replay
   game_recorder.replay()

5. VERITABANI ISLEMLERI (Transaction):
   transaction = DatabaseTransaction()
   transaction.add(InsertCommand("users", data))
   transaction.add(UpdateCommand("profile", new_data))
   transaction.add(DeleteCommand("cache", key))

   transaction.execute()  # Tum komutlari calistir
   # Hata olursa
   transaction.rollback()  # Tum komutlari geri al

6. GUI BUTON ISLEMLERI:
   save_btn.set_command(SaveCommand(document))
   print_btn.set_command(PrintCommand(document))
   close_btn.set_command(CloseCommand(document))

Asagidaki Ornekte:
------------------
Basit bir Command pattern implementasyonu gosterilmektedir.
Command nesnesi Receiver'a iletilen islemi kapsuller.
Invoker, komutu tetikler ve Receiver islemi gerceklestirir.
"""

"""Use built-in abc to implement Abstract classes and methods"""
from abc import ABC, abstractmethod

"""Class Dedicated to Command"""


class Command(ABC):
    """constructor method"""

    def __init__(self, receiver):
        self.receiver = receiver

    """process method"""

    def process(self):
        pass


"""Class dedicated to Command Implementation"""


class CommandImplementation(Command):
    """constructor method"""

    def __init__(self, receiver):
        self.receiver = receiver

    """process method"""

    def process(self):
        self.receiver.perform_action()


"""Class dedicated to Receiver"""


class Receiver:
    """perform-action method"""

    def perform_action(self):
        print('Action performed in receiver.')


"""Class dedicated to Invoker"""


class Invoker:
    """command method"""

    def command(self, cmd):
        self.cmd = cmd

    """execute method"""

    def execute(self):
        self.cmd.process()


"""main method"""
if __name__ == "__main__":
    """create Receiver object"""
    receiver = Receiver()
    cmd = CommandImplementation(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
