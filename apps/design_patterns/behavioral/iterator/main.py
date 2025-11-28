"""
ITERATOR PATTERN (Yineleyici Deseni)
=====================================

TANIM:
Iterator Pattern, bir koleksiyonun (collection) elemanlarına, altta yatan temsili
ortaya cikar madan sirayla erisme yontemi saglayan davranissal (behavioral) bir
tasarim desenidir.

Ne Zaman Kullanilir:
--------------------
- Koleksiyonun ic yapisini gizleyerek elemanlara erismek istedigimizde
- Ayni koleksiyon uzerinde birden fazla gezinme desteklemek gerektiginde
- Farkli veri yapilarini ayni arayuzle dolasma ihtiyaci oldugunda
- Koleksiyonun karmasikligini gizlemek istedigimizde
- Lazy loading (tembel yukleme) uygulamak istedigimizde

Avantajlari:
------------
+ Single Responsibility - koleksiyon ve gezinme mantigi ayrilir
+ Open/Closed - yeni iterator turleri kolayca eklenebilir
+ Ayni koleksiyon uzerinde paralel gezinme mumkun
+ Koleksiyonun ic yapisini gizler
+ Kod tekrarini azaltir
+ Lazy iteration destegi

Dezavantajlari:
--------------
- Basit koleksiyonlar icin gereksiz olabilir
- Bazen dogrudan erisim daha verimli olabilir
- Ek siniflar gerektirir

Gercek Hayattan Ornekler:
-------------------------
1. DOSYA SISTEMINDE GEZINME:
   # Klasor icindeki dosyalari dolaş
   folder_iterator = FolderIterator("C:/Documents")
   for file in folder_iterator:
       print(file.name)

2. SOSYAL MEDYA - ARKADAS LISTESI:
   # Farkli gezinme sekilleri
   friends = user.get_friends()

   # Yakin arkadas iterator
   close_friends_iter = CloseFriendsIterator(friends)
   for friend in close_friends_iter:
       print(friend.name)

   # Alfabetik iterator
   alphabetic_iter = AlphabeticIterator(friends)
   for friend in alphabetic_iter:
       print(friend.name)

3. MUZIK CALAR - PLAYLIST:
   playlist = Playlist(["Song1.mp3", "Song2.mp3", "Song3.mp3"])

   # Sirali calisma
   sequential_iter = SequentialIterator(playlist)

   # Rastgele calisma
   shuffle_iter = ShuffleIterator(playlist)

   # Tekrar calisma
   repeat_iter = RepeatIterator(playlist)

4. E-TICARET - URUN KATALOG U:
   products = ProductCatalog()

   # Fiyata gore iterator
   price_iter = PriceIterator(products, min=100, max=1000)
   for product in price_iter:
       print(product.name, product.price)

   # Kategoriye gore iterator
   category_iter = CategoryIterator(products, category="Electronics")

5. VERITABANI SAYFALAMA (Pagination):
   # Buyuk veri seti icin lazy loading
   users_iterator = DatabaseIterator(
       query="SELECT * FROM users",
       page_size=100
   )

   for user in users_iterator:
       # Her iterasyonda sadece 100 kayit yuklenir
       process(user)

6. AGAC YAPISI GEZINME (Tree Traversal):
   tree = BinaryTree(root)

   # In-order traversal
   in_order = InOrderIterator(tree)

   # Pre-order traversal
   pre_order = PreOrderIterator(tree)

   # Post-order traversal
   post_order = PostOrderIterator(tree)

   # Breadth-first (genislik oncelikli)
   bfs = BreadthFirstIterator(tree)

7. PYTHON DAHILI ITERATOR:
   # Python'da tum koleksiyonlar iterable
   my_list = [1, 2, 3, 4, 5]
   for item in my_list:  # Iterator pattern kullanilir
       print(item)

   # Generator expression (lazy iterator)
   squares = (x**2 for x in range(1000000))
   # Sadece ihtiyac duyuldugunda hesaplanir

Asagidaki Ornekte:
------------------
Python'un dahili iterator mekanizmasi gosterilmektedir.
Alfabetik karakterler (A-Z ve a-z) iterator kullanilarak gezilir.
Python'da for dongusu otomatik olarak iterator pattern kullanir.
"""

"""utility function"""


def inBuilt_Iterator1():
    alphabets = [chr(i) for i in range(65, 91)]

    """using in-built iterator"""
    for alpha in alphabets:
        print(alpha, end=" ")
    print()


"""utility function"""


def inBuilt_Iterator2():
    alphabets = [chr(i) for i in range(97, 123)]

    """using in-built iterator"""
    for alpha in alphabets:
        print(alpha, end=" ")
    print()


"""main method"""
if __name__ == "__main__":
    """call the inbuiltIterators"""
    inBuilt_Iterator1()
    inBuilt_Iterator2()
