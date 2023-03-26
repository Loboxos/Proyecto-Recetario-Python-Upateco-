import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.filedialog import askopenfilename
import receta,ingrediente,agregarIngrediente
import listaDingred

class AgregarReceta(ttk.Frame): 
 
    def __init__(self, parent):
        super().__init__(parent)
        self.nombreR=tk.StringVar()
        self.parent=parent
        #self.ing=tk.Variable()
        self.ingredientesR=tk.StringVar()
        self.preparacionR=tk.StringVar()
        self.tiempoPrepR=tk.StringVar()
        self.tiempoCoccR=tk.StringVar()
        self.imagenR=tk.StringVar()
        
        parent.title("Ingresar nueva Receta")
        parent.iconbitmap('img\chef.ico')
        #parent.resizable(False, False)
        
        #parent.geometry("300x200")
        #parent.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        self.create_widgets()
        ttk.Button(self,text="cerrar",command=parent.destroy).grid(column=0,row=6)

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

        ttk.Button(self,text="agregar ingredientes",command=self.tablaConEntrada).grid(column=1, row=1, sticky=tk.E)

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

            #carga imagen 
        password_label = ttk.Label(self, text="imagen de la receta")
        password_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)


        ttk.Button(self, text="Abrir un archivo",
                   command=self.on_btn_abrir_pressed).grid(column=1,row=5)
       
        

        # login button
        login_button = ttk.Button(self, text="Agregar",command=self.guardar_datos)
        login_button.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)
    
    def tablaConEntrada(self):
        toplevel = tk.Toplevel(self.parent)
        # agregamos el frame (Secundaria) a la ventana (toplevel)
        agregarIngrediente.AgregarIngrediente(toplevel).pack()

        
    def on_btn_abrir_pressed(self):
        tipos = (('Archivos de texto', '*.txt'),
                 ('Todos los archivos', '*.*'))
        ruta_archivo = askopenfilename(filetypes=tipos)
        self.imagenR=ruta_archivo



    def guardar_datos(self):
        listaIngr=agregarIngrediente.listaDingredi
        for ingred in listaIngr:
            ing=ingrediente.Ingrediente(ingred[0],ingred[1],ingred[2])
        listaFinalxd=listaDingred.ListDingredientes(listaIngr)
        
        nombre=self.nombreR.get()        
        print("linea103")
        
        #print(ingredientes)
        
        #print(self.ingredientesR.get())

        #ingredientes=self.ingredientesR.get()
        #listaIngredientes=ingredientes.split(",")
        
        #listIngredientes=[]
        #nombre=listaIngredientes[0]
        #unidadDmedida=listaIngredientes[1]
        #cantidad=listaIngredientes[2]
        
        #ing=ingrediente.Ingrediente(nombre,unidadDmedida,cantidad)
        #listIngredientes.append(ing)
        
        preparacion=self.preparacionR.get()
        tiempoC=self.tiempoCoccR.get()
        tiempoP=self.tiempoPrepR.get()
        imagen=self.imagenR
        
        recetas=receta.Receta(nombre,preparacion,tiempoP,tiempoC,"10/05/2001",True,listaIngr,imagen,"rico,nutritivo")
        recetas.añadirUnaNuevaReceta()
