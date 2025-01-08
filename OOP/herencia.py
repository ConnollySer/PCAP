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
print(book1.quantity)
print(book1.author)

        
class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch
        
    def __repr__(self):
        return f"Titulo: \ '{self.title}\', Genero: {self.branch},\ Cantidad: {self.quantity}, Author: {self.author}, Precio: {round(self.get_price(),3)} €"
    

novela1 = Novel("Don Quixote Don Flamingo", 45, " Luffy", 4, 500)
novela1.set_discount(0.50)
ensayo1 = Academic("La dura verdad", 5, "Yo", 4545, "accion")

print(novela1)
print(ensayo1)

        