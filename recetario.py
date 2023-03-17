class Recetario:
    recetas = []

    def __init__(self,recetas=[]):
        self.recetas = recetas

    def crearUnaNuevaRecetas(self,receta):
        self.recetas.append(receta)
    
    def mostrar(self):
        for p in self.recetas:
            print(p) 