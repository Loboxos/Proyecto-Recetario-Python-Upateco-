import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.filedialog import askopenfilename
import receta






class ModificarReceta(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.nombreRE=tk.StringVar()
        self.nombreNuevo=tk.StringVar()
        self.ingredienteNuevo=tk.StringVar()
        self.preparacionNuevo=tk.StringVar()
        self.tiempoPropRNuevo=tk.StringVar()
        self.tiempoCoccRnuevo=tk.StringVar()
        # self.ingredientesR=tk.StringVar()
        # self.preparacionR=tk.StringVar()
        # self.tiempoPrepR=tk.StringVar()
        # self.tiempoCoccR=tk.StringVar()
        

        parent.title("Modificar una Receta")
        parent.iconbitmap('img\chef.ico')
        #parent.resizable(False, False)
        
        parent.geometry("1200x400")
        parent.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        self.create_widgets()
        ttk.Button(self,text="cerrar",command=parent.destroy).grid(column=0,row=5)
    
    def create_widgets(self):
        # Ingresar comida
        username_label = ttk.Label(self, text="Ingrese nombre de la receta a modificar:")
        username_label.grid(column=0 , row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(self,textvariable=self.nombreRE)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
        
        # login button
        login_button = ttk.Button(self, text="Buscar",command=self.mostrar_datos)
        #messagebox.showinfo(title="Actualizacion",message="se elimino la receta correctamente")
        login_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
      
    def mostrar_datos(self):
        nombre=self.nombreRE.get()
        recet=receta.Receta.mostrarReceta(nombre)
        print(recet)
    
        frame2 = ttk.Frame(self, borderwidth=2, relief="groove")
        frame2.grid(row=2, column=1, sticky=tk.NSEW)
        ttk.Label(frame2, text="RECETA",background="green",width="50",anchor="center").grid()
        ttk.Label(frame2, text=recet['nombre'],background="lightgreen",anchor="nw").grid()
        
        username_label = ttk.Label(frame2, text="Nuevo nombre de Receta")
        username_label.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(frame2,textvariable=self.nombreNuevo)
        username_entry.grid(column=2, row=1, sticky=tk.E, padx=5, pady=5)

        username_label = ttk.Label(frame2, text="Ingredientes nuevos")
        username_label.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(frame2,textvariable=self.ingredienteNuevo)
        username_entry.grid(column=2, row=2, sticky=tk.E, padx=5, pady=5)

        username_label = ttk.Label(frame2, text="preparacion")
        username_label.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(frame2,textvariable=self.preparacionNuevo)
        username_entry.grid(column=2, row=5, sticky=tk.E, padx=5, pady=5)
        
        ttk.Label(frame2, text="ingredientes:").grid()
        for ingrediente in recet['listaDeIngredientes']:
            ttk.Label(frame2, text=f"{ingrediente}, ").grid()

        ttk.Label(frame2, text=f"preparacion: {recet['preparacion']}" ).grid()
 # login button
        login_button = ttk.Button(self, text="Modificar",command=self.guardar_datos)
        #messagebox.showinfo(title="Actualizacion",message="se elimino la receta correctamente")
        login_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)


    def guardar_datos(self):
        nombreRe=self.nombreRE.get()
        nombreNuevo=self.nombreNuevo.get()
        ingredientes=self.ingredienteNuevo.get()
        listaIngredientes=ingredientes.split(",")
        preparacion=self.preparacionNuevo.get()
        nombreRe=nombreRe.lower()        
        receta.Receta.modificarUnaReceta(nombreRe,nombreNuevo,listaIngredientes,preparacion)
