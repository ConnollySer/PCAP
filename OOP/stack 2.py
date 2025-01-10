import sys 

class Stack:
    def __init__(self):
        self.size = 0;
        self.__stack_list = []
 
        
    def push(self, value):
        self.__stack_list.append(value)
    
    def pop(self):
        value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return value
    
    def __repr__(self):
       print(f"Pila = {self.__stack_list}")
        
stack_object = Stack()
try:
    print(len(stack_object.__stack_list))
except: 
    print("Error. El atributo es privado")
    sys.exit(1)
    
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        
    def get_sum (self):
        return self.__sum
    
    def push(self, value):
        self.__sum += value
        Stack.push(self, value)
        
    def pop(self):
        self.__sum -= value
        return value
    
    
        