"""
STATE PATTERN (Durum Deseni)
============================

TANIM:
State Pattern, bir nesnenin ic durumu degistiginde davranisini degistirmesine izin veren
davranissal (behavioral) bir tasarim desenidir. Nesne, sinifini degistirmis gibi gorunur.

Ne Zaman Kullanilir:
--------------------
- Nesne davranisi durumuna bagli oldugunda
- Cok fazla if-else veya switch-case durumu varsa
- Durum gecisleri karmasik oldugunda
- Durum-spesifik davranislar iyi tanimlanmissa
- Runtime'da durum degisimleri gerektiginde

Avantajlari:
------------
+ Single Responsibility - her durum ayri sinifta
+ Open/Closed - yeni durum eklemek kolay
+ Kod okunabilirligi artar
+ Karmasik if-else'leri ortadan kaldirir
+ Durum gecisleri acik ve net

Dezavantajlari:
--------------
- Cok fazla kucuk sinif olusur
- Basit durum makineleri icin gereksiz olabilir
- Durum sayisi azsa asiri muhendislik olabilir

Gercek Hayattan Ornekler:
-------------------------
1. SIPARIS DURUMLARI (E-Commerce):
   order = Order()

   # Durum gecisleri
   order.setState(PendingState())    # Beklemede
   order.process()

   order.setState(ProcessingState()) # İşleniyor
   order.process()

   order.setState(ShippedState())    # Kargoda
   order.process()

   order.setState(DeliveredState())  # Teslim edildi
   order.process()

   # Her durumda farkli davranis
   # Pending: iptal edilebilir
   # Processing: iptal edilemez
   # Shipped: takip edilebilir
   # Delivered: iade edilebilir

2. MUZIK CALAR DURUMLARI:
   player = MusicPlayer()

   # Durumlari ayarla
   player.playing_state = PlayingState(player)
   player.paused_state = PausedState(player)
   player.stopped_state = StoppedState(player)

   player.set_state(player.stopped_state)

   player.play()   # Calmayi baslat
   player.pause()  # Duraklat
   player.play()   # Devam et
   player.stop()   # Durdur

3. ATM MAKINESI:
   atm = ATM()

   # Farkli durumlar
   idle_state = IdleState()         # Bosta
   card_inserted = CardInsertedState()  # Kart takildi
   pin_entered = PinEnteredState()     # PIN girildi
   transaction = TransactionState()    # İşlem yapiliyor

   # Her durumda farkli islemler mumkun
   # Idle: sadece kart kabul eder
   # Card: PIN ister
   # PIN: islem seceneklerini gosterir
   # Transaction: para cekim/yatirma yapar

4. BELGE DURUMU (Document Workflow):
   document = Document()

   draft = DraftState()        # Taslak
   moderation = ModerationState()  # İncelemede
   published = PublishedState()    # Yayinda
   archived = ArchivedState()      # Arsivde

   document.set_state(draft)
   document.edit("Icerik")  # Taslakta duzenleme yapilabilir

   document.publish()  # Moderation'a gider
   document.approve()  # Yayinlanir

5. TRAFIK ISIGI:
   traffic_light = TrafficLight()

   red = RedState(traffic_light)
   yellow = YellowState(traffic_light)
   green = GreenState(traffic_light)

   traffic_light.set_state(red)
   # Kirmizi: arabalar dur
   # Sari: hazirlan
   # Yesil: gec

   traffic_light.change()  # Red -> Green
   traffic_light.change()  # Green -> Yellow
   traffic_light.change()  # Yellow -> Red

6. OYUN KARAKTERI DURUMLARI:
   player = Player()

   idle = IdleState()
   running = RunningState()
   jumping = JumpingState()
   attacking = AttackingState()
   dead = DeadState()

   # Her durumda farkli animasyon ve davranis
   player.set_state(running)
   player.handle_input("space")  # Jumping state'e gec

Asagidaki Ornekte:
------------------
Radyo (Radio) icin state pattern ornegi gosterilmektedir.
Radyo AM ve FM durumlari arasinda gecis yapabilir.
Her durumun kendi istasyon listesi ve davranisi vardir.
"""

"""State class: Base State class"""


class State:
    """Base state. This is to share functionality"""

    def scan(self):
        """Scan the dial to the next station"""
        self.pos += 1

        """check for the last station"""
        if self.pos == len(self.stations):
            self.pos = 0
        print("Visiting... Station is {} {}".format(self.stations[self.pos], self.name))


"""Separate Class for AM state of the radio"""


class AmState(State):
    """constructor for AM state class"""

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    """method for toggling the state"""

    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate


"""Separate class for FM state"""


class FmState(State):
    """Constriuctor for FM state"""

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    """method for toggling the state"""

    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate


"""Dedicated class Radio"""


class Radio:
    """A radio. It has a scan button, and an AM / FM toggle switch."""

    def __init__(self):
        """We have an AM state and an FM state"""
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    """method to toggle the switch"""

    def toggle_amfm(self):
        self.state.toggle_amfm()

    """method to scan """

    def scan(self):
        self.state.scan()


""" main method """
if __name__ == "__main__":

    """ create radio object"""
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    for action in actions:
        action()
