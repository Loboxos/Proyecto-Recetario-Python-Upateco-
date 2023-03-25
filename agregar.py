import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.filedialog import askopenfilename
import receta,ingrediente


class AgregarReceta(ttk.Frame): 
 
    def __init__(self, parent):
        super().__init__(parent)
        self.nombreR=tk.StringVar()
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

        password_entry = ttk.Entry(self,textvariable=self.ingredientesR)
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)


        # ingredientes=self.ingredientesR.split(",")
        # nombre=ingredientes[0]
        # unidadDmedida=ingredientes[1]
        # cantidad=ingredientes[2]

        # ing=ingrediente.Ingrediente(nombre,unidadDmedida,cantidad)
        




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
     
    def on_btn_abrir_pressed(self):
        tipos = (('Archivos de texto', '*.txt'),
                 ('Todos los archivos', '*.*'))
        ruta_archivo = askopenfilename(filetypes=tipos)
        self.imagenR=ruta_archivo



    def guardar_datos(self):
        nombre=self.nombreR.get()
        print(self.ingredientesR.get())

        ingredientes=self.ingredientesR.get()
        listaIngredientes=ingredientes.split(",")
        
        #print(listaIngredientes)
        
        preparacion=self.preparacionR.get()
        tiempoC=self.tiempoCoccR.get()
        tiempoP=self.tiempoPrepR.get()
        imagen=self.imagenR
        
        recetas=receta.Receta(nombre,preparacion,tiempoC,tiempoP,"10/05/2001","rico,nutritivo",True,imagen,listaIngredientes)
        recetas.añadirUnaNuevaReceta()
