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
