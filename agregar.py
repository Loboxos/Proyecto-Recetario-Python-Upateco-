import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.filedialog import askopenfilename
import receta,ingrediente,agregarIngrediente
import listaDingred
from datetime import datetime

class AgregarReceta(ttk.Frame): 
 
    def __init__(self, parent):
        super().__init__(parent)
        self.nombreR=tk.StringVar()
        self.parent=parent
        self.ingredientesR=tk.StringVar()
        self.preparacionR=tk.StringVar()
        self.tiempoPrepR=tk.StringVar()
        self.tiempoCoccR=tk.StringVar()
        self.imagenR=tk.StringVar()
        self.etiquetasR=tk.StringVar()
        
        parent.title("Ingresar nueva Receta")
        parent.iconbitmap('img\chef.ico')
    
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        self.create_widgets()
        ttk.Button(self,text="cerrar",command=parent.destroy).grid(column=0,row=7)

    def create_widgets(self):
        # Ingresar comida
        nombreR_label = ttk.Label(self, text="Nombre de la receta:")
        nombreR_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    

        nombreR_entry = ttk.Entry(self,textvariable=self.nombreR)
        nombreR_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
      
        ingredR_label = ttk.Label(self, text="Ingredientes:")
        ingredR_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        ttk.Button(self,text="agregar ingredientes",command=self.tablaConEntrada).grid(column=1, row=1, sticky=tk.E)

               # preparacion
        preparaR_label = ttk.Label(self, text="preparacion:")
        preparaR_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)


        preparaR_entry = ttk.Entry(self,textvariable=self.preparacionR)
        preparaR_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

               # tiempo preparacion
        tiempoP_label = ttk.Label(self, text="tiempo de preparacion:")
        tiempoP_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        tiempoP_entry = ttk.Entry(self,textvariable=self.tiempoPrepR)
        tiempoP_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

               # tiempo coccion
        tiempoC_label = ttk.Label(self, text="tiempo de coccion:")
        tiempoC_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

        tiempoC_entry = ttk.Entry(self ,textvariable=self.tiempoCoccR)
        tiempoC_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

            #carga imagen 
        imagenR_label = ttk.Label(self, text="imagen de la receta")
        imagenR_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
       

        ttk.Button(self, text="Abrir un archivo",
                   command=self.on_btn_abrir_pressed).grid(column=1,row=5)
        
        etiquetasR_label=ttk.Label(self,text="etiquetas de la receta")
        etiquetasR_label.grid(column=0,row=6,sticky=tk.W,padx=5,pady=5)
        
        etiquetasR_entry=ttk.Entry(self,textvariable=self.etiquetasR)
        etiquetasR_entry.grid(column=1,row=6,sticky=tk.E,padx=5,pady=5)


        # login button
        guardar_button = ttk.Button(self, text="Agregar",command=lambda:[self.guardar_datos(),self.mensaje()])
        guardar_button.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)
    
    def tablaConEntrada(self):
        toplevel = tk.Toplevel(self.parent)
        agregarIngrediente.AgregarIngrediente(toplevel).pack()

        
    def on_btn_abrir_pressed(self):
        tipos = (('Archivos de imagen', '*.gif'),
                 ('Todos los archivos', '*.*'))
        ruta_archivo = askopenfilename(filetypes=tipos)
        self.imagenR=ruta_archivo


    def mensaje(self):
        messagebox.showinfo("Aviso","Se Agrego la receta correctamente")

    def guardar_datos(self):
        listaIngr=agregarIngrediente.listaDingredi
        for ingred in listaIngr:
            ing=ingrediente.Ingrediente(ingred[0],ingred[1],ingred[2])
        listaFinalxd=listaDingred.ListDingredientes(listaIngr)
        
        nombre=self.nombreR.get()        
        preparacion=self.preparacionR.get()
        tiempoC=self.tiempoCoccR.get()
        tiempoP=self.tiempoPrepR.get()
        imagen=self.imagenR


        etiquetas=self.etiquetasR.get()
        etiquetas=etiquetas.split(",")

        fecha = datetime.now()
        
        recetas=receta.Receta(nombre,preparacion,tiempoP,tiempoC,str(fecha),True,listaIngr,imagen,etiquetas)
        recetas.añadirUnaNuevaReceta()
