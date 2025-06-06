class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __eq__(self,other):
        return self.price == other.price
    
P1 = Product("Pen",20)
P2 = Product("Pencil",20)
P3 = Product("Book",50)

print(P1 == P2)
print(P1 == P3)