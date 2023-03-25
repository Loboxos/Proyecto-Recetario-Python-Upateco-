import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.filedialog import askopenfilename
import receta





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
        