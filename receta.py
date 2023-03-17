import json
import random

class Receta:
    def __init__(self,nombre,preparacion,tiempoPrep,tiempoCocc,fechaDeCreacion,etiquetas,esFavorita,imagen=None,ListaIngred=[]):
        self.nombre = nombre
        self.ListaIngred = ListaIngred
        self.preparacion = preparacion
        self.imagen =imagen
        self.tiempoPrep = tiempoPrep
        self.tiempoCocc = tiempoCocc
        self.fechaDeCreacion = fechaDeCreacion
        self.etiquetas = etiquetas
        self.esFavorita = esFavorita
    
    def añadirUnaNuevaReceta(self):
        r1={
        "nombre":self.nombre,
        "preparacion":self.preparacion,
        "listaIngred":self.ListaIngred,
        "tiempoPrep":self.tiempoPrep,
        "tiempoCocc":self.tiempoCocc,
        "fechaDeCreacion":self.fechaDeCreacion
         }
        
        with open("recetas.json",'r') as fo:
            recetas = json.load(fo)
            #print(recetas)
        recetas.append(r1)
        with open("recetas.json", "w") as fo:
            json.dump(recetas, fo)
            
    def modificarUnaReceta(self):
        pass

    def eliminarUnaReceta(self):
        pass

    def mostrarUnaRecetaDiaria():
        with open("recetas.json")as fo:
            recetas=json.load(fo)
        recetAzar=random.choice(recetas)
        return recetAzar
        #return recetas[random.choice(recetas)]

    def buscarUnaReceta(self):
        pass
    
    def __str__(self):
        return f"{self.nombre}\n{self.ListaIngred}\n{self.preparacion}\n"