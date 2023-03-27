import json
import random

class Receta:
    def __init__(self,nombre,preparacion,tiempoPrep,tiempoCocc,fechaDeCreacion,esFavorita,listaIngred,imagen="",etiquetas=[]):
        self.nombre = nombre
        self.listaIngred = listaIngred
        self.preparacion = preparacion
        self.imagen = imagen
        self.tiempoPrep = tiempoPrep
        self.tiempoCocc = tiempoCocc
        self.fechaDeCreacion = fechaDeCreacion
        self.etiquetas = etiquetas
        self.esFavorita = esFavorita

    def añadirUnaNuevaReceta(self):
        r1={
        "nombre":self.nombre,
        "preparacion":self.preparacion,
        "listaDeIngredientes":self.listaIngred,
        "tiempoDePrep":self.tiempoPrep,
        "tiempoDeCocc":self.tiempoCocc,
        "fechaDeCreacion":self.fechaDeCreacion,
        "imagen":self.imagen,
        "etiquetas":self.etiquetas
        
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
        
    def mostrarUnaRecetaDiaria():
        with open("recetas.json")as fo:
            recetas=json.load(fo)
        recetAzar=random.choice(recetas)
        return recetAzar      

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
        
        if int(op)==2:
            for receta in recetas:
                listaDeEtiquetas=receta["etiquetas"]
                for etiquetas in listaDeEtiquetas:
                    if etiquetas==entry:
                       lisrecet.append(receta)
            
            return lisrecet 
        if int(op)==3:
            entry=entry.split("-")
            for receta in recetas:
                if receta["tiempoDePrep"] in range (int(entry[0]),int(entry[1])):
                   lisrecet.append(receta)
            return lisrecet
        
        if int(op)==4:
            ingredientes=entry.split(",")
            for receta in recetas:
                for ing in ingredientes:
                    if ing in receta["listaDeIngredientes"][0]:
                        if receta not in lisrecet:
                            lisrecet.append(receta)
            return lisrecet
              
    def __str__(self):
        return f"{self.nombre}\n{self.listaIngred}\n{self.preparacion}\n"