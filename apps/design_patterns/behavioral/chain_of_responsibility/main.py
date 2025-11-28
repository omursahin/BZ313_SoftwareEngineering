"""
CHAIN OF RESPONSIBILITY PATTERN (Sorumluluk Zinciri Deseni)
=============================================================

TANIM:
Chain of Responsibility, bir istegin birden fazla nesne tarafindan islenme sansini
saglayan davranissal (behavioral) bir tasarim desenidir. Istek, zincirdeki bir handler
tarafindan isleneninceye kadar zincir boyunca iletilir.

Ne Zaman Kullanilir:
--------------------
- Birden fazla nesne bir istegi isleme sansina sahip olmalidir
- Istegi isleyecek nesne onceden bilinmiyorsa
- Handler'larin seti dinamik olarak belirlenmesi gerekiyorsa
- Gonderici ve alici arasinda gevşek baglanti istiyorsak
- Istekleri sirayla isleme ihtiyaci varsa

Avantajlari:
------------
+ Gonderici ve alici arasinda gevşek baglanti (decoupling)
+ Handler'larin siralamasi esnek sekilde degistirilebilir
+ Single Responsibility Principle - her handler bir sorumluluk alir
+ Open/Closed Principle - yeni handler'lar kolayca eklenebilir
+ İşlem sorumluluğunu dagitir

Dezavantajlari:
--------------
- Istegin islenmesi garanti degildir
- Hata ayiklama (debugging) zor olabilir
- Performans problemleri olusabilir (uzun zincir)
- Request handler iliski si her zaman net olmayabilir

Gercek Hayattan Ornekler:
-------------------------
1. DESTEK TALEP SISTEMI (TICKET SYSTEM):
   # Level 1 -> Level 2 -> Level 3 -> Manager
   ticket = SupportTicket("Sifre sifirlama")
   level1_support.handle(ticket)  # Basit ise Level1 halleder
   # Degilse Level2'ye iletir, o da halledemezse Level3'e...

2. ONAY SISTEMI (APPROVAL CHAIN):
   # Satın alma onay zinciri
   purchase = PurchaseRequest(amount=15000)
   team_lead.handle(purchase)      # 5000 TL'ye kadar onaylayabilir
   manager.handle(purchase)         # 10000 TL'ye kadar
   director.handle(purchase)        # 50000 TL'ye kadar
   ceo.handle(purchase)             # Limitsiz

3. ATM PARA CEKME:
   # 200, 100, 50, 20, 10 TL'lik banknotlar
   withdrawal = WithdrawRequest(370)
   handler_200.handle(withdrawal)   # 1 adet 200 TL
   handler_100.handle(withdrawal)   # 1 adet 100 TL
   handler_50.handle(withdrawal)    # 1 adet 50 TL
   handler_20.handle(withdrawal)    # 1 adet 20 TL

4. LOG KAYIT SISTEMI:
   # Debug -> Info -> Warning -> Error -> Critical
   log_message = LogMessage("Database baglanti hatasi", level="ERROR")
   debug_logger.handle(log_message)
   # Her logger kendi seviyesine uygunsa isler, yoksa iletirir

5. MIDDLEWARE/FILTER ZINCIRI (Web Uygulamalari):
   request = HttpRequest("/api/users")
   authentication_filter.handle(request)  # Kimlik dogrula
   authorization_filter.handle(request)   # Yetki kontrol
   rate_limiter.handle(request)           # Oran sinirla
   controller.handle(request)             # İşle

6. GUI OLAY ISLEME:
   # Button -> Panel -> Window -> Application
   click_event = MouseClick(x=100, y=200)
   button.handle(click_event)  # Button islemezse
   panel.handle(click_event)   # Panel'e iletir

Asagidaki Ornekte:
------------------
Alfabetik karakter isleyen bir zincir ornegi gosterilmektedir.
Farkli handler'lar farkli karakter araliklarini (a-e, e-l, l-z) isler.
Hicbiri isleyemezse DefaultHandler devreye girer.
"""

class AbstractHandler(object):
    """Parent class of all concrete handlers"""

    def __init__(self, nxt):
        """change or increase the local variable using nxt"""

        self._nxt = nxt

    def handle(self, request):
        """It calls the processRequest through given request"""

        handled = self.processRequest(request)

        """case when it is not handled"""

        if not handled:
            self._nxt.handle(request)

    def processRequest(self, request):
        """throws a NotImplementedError"""

        raise NotImplementedError('First implement it !')


class FirstConcreteHandler(AbstractHandler):
    """Concrete Handler # 1: Child class of AbstractHandler"""

    def processRequest(self, request):
        '''return True if request is handled '''

        if 'a' < request <= 'e':
            print("This is {} handling request '{}'".format(self.__class__.__name__, request))
            return True


class SecondConcreteHandler(AbstractHandler):
    """Concrete Handler # 2: Child class of AbstractHandler"""

    def processRequest(self, request):
        '''return True if the request is handled'''

        if 'e' < request <= 'l':
            print("This is {} handling request '{}'".format(self.__class__.__name__, request))
            return True


class ThirdConcreteHandler(AbstractHandler):
    """Concrete Handler # 3: Child class of AbstractHandler"""

    def processRequest(self, request):
        '''return True if the request is handled'''

        if 'l' < request <= 'z':
            print("This is {} handling request '{}'".format(self.__class__.__name__, request))
            return True


class DefaultHandler(AbstractHandler):
    """Default Handler: child class from AbstractHandler"""

    def processRequest(self, request):
        """Gives the message that the request is not handled and returns true"""

        print("This is {} telling you that request '{}' has no handler right now.".format(self.__class__.__name__,
                                                                                          request))
        return True


class User:
    """User Class"""

    def __init__(self):
        """Provides the sequence of handles for the users"""

        initial = None

        self.handler = FirstConcreteHandler(SecondConcreteHandler(ThirdConcreteHandler(DefaultHandler(initial))))

    def agent(self, user_request):
        """Iterates over each request and sends them to specific handles"""

        for request in user_request:
            self.handler.handle(request)


"""main method"""

if __name__ == "__main__":
    """Create a client object"""
    user = User()

    """Create requests to be processed"""

    string = "GeeksforGeeks"
    requests = list(string)

    """Send the requests one by one, to handlers as per the sequence of handlers defined in the Client class"""
    user.agent(requests)
