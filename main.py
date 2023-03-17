import receta
import recetario

print("----------Recetario--------")
op=int(input("que desea hacer?\n1 Crear receta: \n2 Editar receta \n3 Eliminar receta \n4 Mostrar Recetario\n"))
if op==1:
    # nombreR=input("ingrese nombre de la receta")
    # preparacion=input("escriba su preparacion")
    # listaIngred=[]
    # seguir="si"
    # while seguir=="si":
    #     listaIngred.append(input("ingrese un ingrediente"))
    #     seguir=input("desea seguir ingresando ingredientes? si o no ")
    # tiempoPrep=input("ingrese tiempo de preparacion")
    # tiempoCocc=input("ingrese tiempo de coccion")
    # fechaDeCreacion=input("ingrese la fecha de creacion")
    # etiqueta=input("ingrese una etiqueta")
    # fav=input("marcar como favorita? si o no")
    # if fav=="si":
    #     esFavorita=True
    # else:
    #     esFavorita=False
    # imagen=input("ingrese url de imagen")
   
    sandwich=receta.Receta("sandwich","primrtar el pan segundo ponerle el queso",30,5,"10/05/2001","rico y saludable",True,"imagen",["zapallo","milanesa"])
    recetas=receta.Receta("pizza","ponerle el queso",30,5,"10/05/2001","rico",True,"imagen",["zapallo","milanesa"])
    recetas.añadirUnaNuevaReceta()
    recetas.mostrarUnaRecetaDiaria()
    #print(sandwich)
    #recetario1=recetario.Recetario([sandwich])
    
    #recetario1.crearUnaNuevaRecetas(pizza)
    #recetario1.mostrar()