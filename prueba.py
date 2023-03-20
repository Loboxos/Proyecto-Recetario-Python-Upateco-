import tkinter as tk
from tkinter import ttk,messagebox
import receta
import time,random

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent,padding=10,borderwidth=1,relief="groove")
        self.parent=parent
        
        

        parent.title("Recetario")
        
        
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        #self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
        
        frame1 = ttk.Frame(self, borderwidth=2, relief="groove")    # crea el frame
        frame1.grid(row=1, column=1,columnspan=2, sticky=tk.NSEW)    # inserta el frame al frame principal
        # inserta el frame al frame principal
       
        frame1.columnconfigure(0, weight=1) # configura columna 0 (default)
        frame1.rowconfigure(0, weight=1) # configura fila 0 (default)
        ttk.Label(frame1, text="Recetario",background="lightgreen",width="200",anchor="center").grid(padx=5, pady=5, sticky=tk.N)  # crea label y la inserta
        
        recetaPrinc=receta.Receta.mostrarUnaRecetaDiaria()
        print(recetaPrinc)

        frame2 = ttk.Frame(self, borderwidth=2, relief="groove")
        frame2.grid(row=2, column=1, sticky=tk.NSEW)
        ttk.Label(frame2, text="RECETA DEL DIA",background="green",width="50",anchor="center").grid()
        ttk.Label(frame2, text=recetaPrinc['nombre'],background="lightgreen",anchor="nw").grid()
        ttk.Label(frame2, text="ingredientes:").grid()
        for ingrediente in recetaPrinc['listaDeIngredientes']:
            ttk.Label(frame2, text=f"{ingrediente}, ").grid()

        ttk.Label(frame2, text=f"preparacion: {recetaPrinc['preparacion']}" ).grid()
        
      

       


        frame4 = ttk.Frame(self, borderwidth=1, relief="groove")
        frame4.grid(row=2, column=2, sticky=tk.NSEW)
        frame4.columnconfigure(0, weight=0)
        frame4.rowconfigure(0, weight=0)
        self.imagen = tk.PhotoImage(file="img/pizza.gif")
        ttk.Label(frame4, image=self.imagen,background="lightgreen").pack(anchor="center")
        
       
        frame5 = ttk.Frame(self, borderwidth=1, relief="groove")
        frame5.grid(row=4,column=1,columnspan=2, sticky=tk.NSEW)
        frame5.columnconfigure(0, weight=2)
        frame5.rowconfigure(0, weight=2)
        ttk.Label(frame5, text="*****MAS RECETAS******",background="green",width="100",anchor="center").grid(row=3,column=1,columnspan=2,sticky=tk.S)


        # definimos 2 columnas 1: tabla, 2: barra de desplazamiento
       
        frame5.columnconfigure(1, weight=1)
        frame5.columnconfigure(2, weight=1) # wight=0 no cambia de tamaño nunca
        frame5.rowconfigure(1, weight=1)
        frame5.rowconfigure(2, weight=1)
        frame5.rowconfigure(3, weight=1)
        frame5.columnconfigure(3, weight=1) # wight=0 no cambia de tamaño nunca
        frame5.rowconfigure(4, weight=1)
        frame5.columnconfigure(4, weight=1) # wight=0 no cambia de tamaño nunca


        # definimos las columnas de la tabla
        columnas = ('Receta', 'ingredientes', 'etiquetas','Tpreparacion','Tcoccion')
        
        
   
        
        frame5.tabla = ttk.Treeview(self, columns=columnas,
                                  show='headings',
                                  selectmode="browse") # sin multi-seleccion
        frame5.tabla.grid(row=5, column=1,columnspan=2, sticky=(tk.NSEW))
        

        # definimos los encabezados que se muestran
        frame5.tabla.heading('Receta', text='Receta')
        frame5.tabla.heading('ingredientes', text='ingredientes')
        frame5.tabla.heading('etiquetas', text='etiquetas')
        frame5.tabla.heading('Tpreparacion', text='Tpreparacion')
        frame5.tabla.heading('Tcoccion', text='Tcoccion')
 
        #self.frame5=frame5
        
        # generar los datos artificiales
        contacts = []
        cantRecetas=len(receta.Receta.listaDeRecetas())
        for x in receta.Receta.listaDeRecetas():
            nombre=x['nombre']
            ingredientes=x['listaDeIngredientes']
            etiquetas=x['etiquetas']
            tiempoPrep=x['tiempoDePrep']
            tiempoCocc=x['tiempoDeCocc']
            contacts.append((f'{nombre}', f'{ingredientes} ',f'{etiquetas}', f'{tiempoPrep}MIN', f'{tiempoCocc}MIN'))

        # agregar datos al treeview
        for contact in contacts:
            frame5.tabla.insert('', tk.END, values=contact)
    
        self.frame5=frame5
        self.label = tk.Label(self, text='EPL Predictions')

        tk.Button(self, text="*****ACTUALIZAR******",bg='CadetBlue').grid(row=7,column=1,sticky=tk.S)
        tk.Button(self, text="*****MAS OPCIONES******",bg='CadetBlue',command=self.abrir_ventana).grid(row=7,column=2,sticky=tk.S)
   
    
   # def update(self):
    #   self.config(text=str(random.random()))
     #  root.after(1000, self.update)

    def abrir_ventana(self):
        # creamos la ventana secundaria
        # como padre indicamos la ventana principal
        toplevel = tk.Toplevel(self.parent)
        # agregamos el frame (Secundaria) a la ventana (toplevel)
        Secundaria(toplevel).grid()


class Secundaria(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        parent.title("Mas opciones")
        #parent.geometry("450x200+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.iconbitmap('img\chef.ico')
        parent.resizable(False, False)

        ttk.Button(self, text="Buscar Receta",width=100).grid() 
        ttk.Button(self, text="Agregar Receta",command=self.abrir_ventana2,width=100).grid()
        ttk.Button(self, text="Eliminar receta",command=self.abrir_ventana3,width=100).grid() 
        ttk.Button(self, text="modificar receta",width=100).grid()
        ttk.Button(self, text="Cerrar",width=100, command=parent.destroy).grid()
    def abrir_ventana3(self):
        toplevel = tk.Toplevel(self.parent)
        EliminarReceta(toplevel).grid()

    def abrir_ventana2(self):
        # creamos la ventana secundaria
        # como padre indicamos la ventana principal
        toplevel = tk.Toplevel(self.parent)
        # agregamos el frame (Secundaria) a la ventana (toplevel)
        AgregarReceta(toplevel).grid()


class EliminarReceta(ttk.Frame):
    import receta
    def __init__(self, parent):
        super().__init__(parent)
        #import prueba
        #frame5=prueba.App.frame5
        #print(frame5)
        self.nombreR=tk.StringVar()
       
        # self.ingredientesR=tk.StringVar()
        # self.preparacionR=tk.StringVar()
        # self.tiempoPrepR=tk.StringVar()
        # self.tiempoCoccR=tk.StringVar()
        

        parent.title("Eliminar una Receta")
        parent.iconbitmap('img\chef.ico')
        #parent.resizable(False, False)
        
        parent.geometry("300x200")
        parent.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        self.create_widgets()
        ttk.Button(self,text="cerrar",command=parent.destroy).grid(column=0,row=5)
    
    def create_widgets(self):
        # Ingresar comida
        username_label = ttk.Label(self, text="Ingrese nombre de la receta:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(self,textvariable=self.nombreR)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
        # login button
        login_button = ttk.Button(self, text="Eliminar",command=self.guardar_datos)
        #messagebox.showinfo(title="Actualizacion",message="se elimino la receta correctamente")
        login_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
    
    def guardar_datos(self):
        nombre=self.nombreR.get()
        nombre=nombre.lower()        
        receta.Receta.eliminarUnaReceta(nombre)
        
       
        
        



        

class AgregarReceta(ttk.Frame):
    import receta
    def __init__(self, parent):
        super().__init__(parent)
        self.nombreR=tk.StringVar()
        self.ingredientesR=tk.StringVar()
        self.preparacionR=tk.StringVar()
        self.tiempoPrepR=tk.StringVar()
        self.tiempoCoccR=tk.StringVar()

        
        parent.title("Ingresar nueva Receta")
        parent.iconbitmap('img\chef.ico')
        #parent.resizable(False, False)
        
        parent.geometry("300x200")
        parent.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        self.create_widgets()
        ttk.Button(self,text="cerrar",command=parent.destroy).grid(column=0,row=5)
    def create_widgets(self):
        # Ingresar comida
        username_label = ttk.Label(self, text="Nombre de la receta:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    
        
        

        username_entry = ttk.Entry(self,textvariable=self.nombreR)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        #print(self.nombreR)
        # ingredientes
        password_label = ttk.Label(self, text="Ingredientes:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,textvariable=self.ingredientesR)
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

               # preparacion
        password_label = ttk.Label(self, text="preparacion:")
        password_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)


        password_entry = ttk.Entry(self,textvariable=self.preparacionR)
        password_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

               # tiempo preparacion
        password_label = ttk.Label(self, text="tiempo de preparacion:")
        password_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,textvariable=self.tiempoPrepR)
        password_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

               # tiempo coccion
        password_label = ttk.Label(self, text="tiempo de coccion:")
        password_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self ,textvariable=self.tiempoCoccR)
        password_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Agregar",command=self.guardar_datos)
        login_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)


    def guardar_datos(self):
        nombre=self.nombreR.get()
        print(self.ingredientesR.get())
        ingredientes=self.ingredientesR.get()
        listaIngredientes=ingredientes.split(",")
        print(listaIngredientes)
        preparacion=self.preparacionR.get()
        tiempoC=self.tiempoCoccR.get()
        tiempoP=self.tiempoPrepR.get()
        recetas=receta.Receta(nombre,preparacion,tiempoC,tiempoP,"10/05/2001","rico,nutritivo",True,"imagen",listaIngredientes)
        recetas.añadirUnaNuevaReceta()
        

    def create_widgets(self):
        # Ingresar comida
        username_label = ttk.Label(self, text="Nombre de la receta:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    
        
        

        username_entry = ttk.Entry(self,textvariable=self.nombreR)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        #print(self.nombreR)
        # ingredientes
        password_label = ttk.Label(self, text="Ingredientes:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,textvariable=self.ingredientesR)
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

               # preparacion
        password_label = ttk.Label(self, text="preparacion:")
        password_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)


        password_entry = ttk.Entry(self,textvariable=self.preparacionR)
        password_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

               # tiempo preparacion
        password_label = ttk.Label(self, text="tiempo de preparacion:")
        password_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,textvariable=self.tiempoPrepR)
        password_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

               # tiempo coccion
        password_label = ttk.Label(self, text="tiempo de coccion:")
        password_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self ,textvariable=self.tiempoCoccR)
        password_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Agregar",command=self.guardar_datos)
        login_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
        

        
   
        


#print(recetaPrinc)
# Finalmente bucle de la aplicación

root=tk.Tk()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.iconbitmap('img\chef.ico')
root.geometry('1000x600')


#root.config(bg="red")
App(root).grid(sticky=tk.NSEW)
root.resizable(False, False)#para que no se pueda redimensionar la ventana


root.mainloop()