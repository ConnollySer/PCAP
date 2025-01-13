class Book:
    #constructor
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
     #encapsulacion : private attibutes
        self.__price = price
        self.__discount = None
        
    #setter method
    def set_discount(self,discount):
        self.__discount = discount
        
    #getter method
    def get_price(self):
        if self.__discount:
            return self.__price* (1-self.__discount)
        return self.__price
    
    #Return a printable representation of the object
    def __repr__(self):
        return f"Titulo: \'{self.title}\', Cantidad: {self.quantity}, Author: {self.author}, Precio: {round(self.get_price(),3)}€"

book1 = Book("Luffy y sus aventurillas traviesas", 30, "Naruto", 55)    
book2 = Book("las increibles aventuras de nadie", 50, "yo", 5)
book3 = Book("No hay mas historia que contar", 45, " Sergio el mejhor", 44)

print(book1)
print(book2)
print(book3)

print(book1.title)
print(book2.__price)
print(book1.quantity)
print(book1.author)
print(book1.__discount)
        