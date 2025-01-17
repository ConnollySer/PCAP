class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, valor):
        self.list.append(valor) 

    def dequeue(self):
        if len(self.list) > 0:
            primero = self.list[0]  
            del self.list[0]
            return primero
        else:
            return None

cola = Queue()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
print(cola.dequeue())  
print(cola.dequeue())  
print(cola.dequeue())  
print(cola.dequeue())  