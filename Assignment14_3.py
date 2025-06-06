class Book:
    def __init__(self,price):
        self.__price = price 

    def get_price(self):
        return self.__price
    
    def set_price(self,price):
        self.__price = price

book = Book(250)

print("Book Price:", book.get_price())
book.set_price(350)

print("New Price:", book.get_price())