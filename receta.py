import json
import random

class Receta:
    def __init__(self,nombre,preparacion,tiempoPrep,tiempoCocc,fechaDeCreacion,esFavorita,imagen=None,etiquetas=[],ListaIngred=[]):
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
        "listaDeIngredientes":self.ListaIngred,
        "tiempoDePrep":self.tiempoPrep,
        "tiempoDeCocc":self.tiempoCocc,
        "fechaDeCreacion":self.fechaDeCreacion,
        "imagen":self.imagen
         }
        
        with open("recetas.json",'r') as fo:
            recetas = json.load(fo)
            #print(recetas)
        recetas.append(r1)
        with open("recetas.json", "w") as fo:
            json.dump(recetas, fo)
            
    def modificarUnaReceta(nombreReceta,nuevoNombre,ingr,preparacion):
        with open("recetas.json",'r') as fo:
            recetas = json.load(fo)
            for rec in recetas:
               if rec["nombre"]==nombreReceta:
                  rec["nombre"]=nuevoNombre
                  rec["listaDeIngredientes"]=ingr
                  rec["preparacion"]=preparacion
               else:
                print("receta no encontrada")
        with open("recetas.json", "w") as fo:
            json.dump(recetas, fo)
    def eliminarUnaReceta(nombreReceta):
        with open("recetas.json",'r') as fo:
            recetas = json.load(fo)
            #print(recetas)
            print("linea 40")
            for rec in recetas:
               if rec["nombre"]==nombreReceta:
                recetas.remove(rec)
                print("receta eliminada")
                
                #print(recetas)
               else:
                print("receta no encontrada")
            
        with open("recetas.json", "w") as fo:
            json.dump(recetas, fo)
            #nombreReceta="pizza"
            #if recetas['nombre']==nombreReceta:
             #   print(recetas['nombre'])
        
    def listaDeRecetas():
        with open("recetas.json")as fo:
            recetas=json.load(fo)
        return recetas
    
    def mostrarReceta(nombre):
        with open("recetas.json")as fo:
            recetas=json.load(fo)
        for receta in recetas:
            if receta["nombre"]==nombre:
                recetaD=receta
        return recetaD
        #return recetas[random.choice(recetas)]

    def mostrarUnaRecetaDiaria():
        with open("recetas.json")as fo:
            recetas=json.load(fo)
        recetAzar=random.choice(recetas)
        return recetAzar
        #return recetas[random.choice(recetas)]

    def buscarUnaReceta(op,entry):
        with open("recetas.json")as fo:
            recetas=json.load(fo)
        lisrecet=[]
        print("holaaaaaad")
        if int(op)==1:
            print("opcion 1")
            for receta in recetas:
                    if receta["nombre"]==entry:
                        recetaD=receta
                        print(recetaD)
                        lisrecet.append(recetaD)
                    else:
                        print("que buscas pa")
        return lisrecet
        #     #return recetaD
        # if op==2:
        #       for receta in recetas:
        #         if receta["etiquetas"]==entry:
        #           recetaD=receta
        #       #return recetaD

        # if op==3:
        #     for receta in recetas:
        #        if receta["tiempoDePrep"]==entry:
        #         recetaD=receta
        #     #return recetaD
        
        # if op==4:
        #     for receta in recetas:
        #        if receta["listaDeIngredientes"]==entry:
        #         recetaD=receta
            #return recetaD
        
    def __str__(self):
        return f"{self.nombre}\n{self.ListaIngred}\n{self.preparacion}\n"