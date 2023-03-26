class ListDingredientes:
    ingredientes=[]
    def __init__(self,ingredientes=[]):
        self.ingredientes=ingredientes
        
    def agregar(self,i):
        self.ingredientes.append(i)
    
    def mostrar(self):
        print("hola linea 10")
        for i in self.ingredientes:
            return i
    