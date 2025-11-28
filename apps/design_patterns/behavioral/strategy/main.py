"""
STRATEGY PATTERN (Strateji Deseni)
===================================

TANIM:
Strategy Pattern, bir algoritma ailesini tanimlar, her birini ayri bir sinifa koyar
ve birbirlerinin yerine kullanilabilir hale getirir. Strateji, algoritmay i kullanan
istemciden bagimsiz olarak degistirilebilir hale getirir. Davranissal (behavioral)
bir tasarim desenidir.

Ne Zaman Kullanilir:
--------------------
- Ayni islemi farkli yontemlerle yapmak gerektiginde
- Cok fazla if-else veya switch-case varsa
- Runtime'da algoritma degistirmek istendiginde
- Algoritmalarin kapsullenmesi gerektiginde
- Benzer siniflar sadece davranislarinda farklilik gosterdiginde

Avantajlari:
------------
+ Open/Closed Principle - yeni strateji eklemek kolay
+ if-else/switch-case karmasikligini ortadan kaldirir
+ Runtime'da strateji degistirilebilir
+ Algoritmayi kullanan koddan izole eder
+ Test edilebilirlik artar

Dezavantajlari:
--------------
- Strateji sayisi artinca sinif sayisi artar
- İstemci farkli stratejileri bilmeli
- Basit durumlar icin gereksiz olabilir

Gercek Hayattan Ornekler:
-------------------------
1. ODEME STRATEJILERI:
   shopping_cart = ShoppingCart()

   # Kredi karti ile ode
   credit_card = CreditCardPayment("1234-5678-9012-3456")
   shopping_cart.set_payment_strategy(credit_card)
   shopping_cart.checkout(1000)

   # PayPal ile ode
   paypal = PayPalPayment("user@example.com")
   shopping_cart.set_payment_strategy(paypal)
   shopping_cart.checkout(500)

   # Kripto para ile ode
   crypto = CryptoPayment("wallet_address_123")
   shopping_cart.set_payment_strategy(crypto)
   shopping_cart.checkout(2000)

2. SIRALAMA STRATEJILERI:
   products = [...]

   sorter = ProductSorter()

   # Fiyata gore sirala
   sorter.set_strategy(PriceSortStrategy())
   sorter.sort(products)

   # Popülerlige gore sirala
   sorter.set_strategy(PopularitySortStrategy())
   sorter.sort(products)

   # Alfabetik sirala
   sorter.set_strategy(AlphabeticalSortStrategy())
   sorter.sort(products)

3. SIKISTIRMA STRATEJILERI:
   file_compressor = FileCompressor()

   # ZIP sikistirma
   file_compressor.set_strategy(ZipCompression())
   file_compressor.compress("file.txt")

   # RAR sikistirma
   file_compressor.set_strategy(RarCompression())
   file_compressor.compress("file.txt")

   # 7Z sikistirma
   file_compressor.set_strategy(SevenZipCompression())
   file_compressor.compress("file.txt")

4. NAVIGASYON STRATEJILERI:
   navigator = Navigator()

   # Araba ile rota
   navigator.set_strategy(CarRouteStrategy())
   navigator.build_route("Ankara", "Istanbul")  # Otoyol

   # Yuruyerek rota
   navigator.set_strategy(WalkingRouteStrategy())
   navigator.build_route("Ankara", "Istanbul")  # Park ve yuruyus yollari

   # Toplu tasima
   navigator.set_strategy(PublicTransportStrategy())
   navigator.build_route("Ankara", "Istanbul")  # Otobus/tren

5. VALIDASYON STRATEJILERI:
   validator = Validator()

   # Email validasyonu
   validator.set_strategy(EmailValidationStrategy())
   validator.validate("user@example.com")

   # Telefon validasyonu
   validator.set_strategy(PhoneValidationStrategy())
   validator.validate("+905551234567")

   # TC Kimlik validasyonu
   validator.set_strategy(TCKNValidationStrategy())
   validator.validate("12345678901")

6. INDIRIM STRATEJILERI:
   # Black Friday indirimi
   black_friday = BlackFridayDiscount()  # %50 indirim

   # Ogrenci indirimi
   student_discount = StudentDiscount()  # %20 indirim

   # Sadakat indirimi
   loyalty_discount = LoyaltyDiscount()  # %10 indirim

   # Kupon indirimi
   coupon = CouponDiscount("SAVE30")  # 30 TL indirim

   product = Product(price=1000)
   product.set_discount_strategy(black_friday)
   final_price = product.calculate_price()

Asagidaki Ornekte:
------------------
Urun fiyati icin farkli indirim stratejileri gosterilmektedir.
Item sinifi, runtime'da farkli discount_strategy'ler alabilir
ve buna gore fiyat hesaplanir.
"""

"""A separate class for Item"""


class Item:
    """Constructor function with price and discount"""

    def __init__(self, price, discount_strategy=None):

        """take price and discount strategy"""

        self.price = price
        self.discount_strategy = discount_strategy

    """A separate function for price after discount"""

    def price_after_discount(self):

        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount

    def __repr__(self):

        statement = "Price: {}, price after discount: {}"
        return statement.format(self.price, self.price_after_discount())


"""function dedicated to On Sale Discount"""


def on_sale_discount(order):
    return order.price * 0.25 + 20


"""function dedicated to 20 % discount"""


def twenty_percent_discount(order):
    return order.price * 0.20


"""main function"""
if __name__ == "__main__":
    print(Item(20000))

    """with discount strategy as 20 % discount"""
    print(Item(20000, discount_strategy=twenty_percent_discount))

    """with discount strategy as On Sale Discount"""
    print(Item(20000, discount_strategy=on_sale_discount))
