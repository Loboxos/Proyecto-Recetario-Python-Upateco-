import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.filedialog import askopenfilename
import receta

class EliminarReceta(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.nombreR=tk.StringVar()
        parent.title("Eliminar una Receta")
        parent.iconbitmap('img\chef.ico')
        parent.geometry("300x200")
        parent.resizable(0, 0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        self.create_widgets()
        ttk.Button(self,text="cerrar",command=parent.destroy).grid(column=0,row=5)
    
    def create_widgets(self):
        
        nombreR_label = ttk.Label(self, text="Ingrese nombre de la receta:")
        nombreR_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        nombreR_entry = ttk.Entry(self,textvariable=self.nombreR)
        nombreR_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
       
        guardar_button = ttk.Button(self, text="Eliminar",command=lambda:[self.guardar_datos(),self.mensaje()])
        guardar_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
    
    def mensaje(self):
        messagebox.showinfo("Aviso","Se elimino la receta correctamente")
    
    def guardar_datos(self):
        nombre=self.nombreR.get()
        nombre=nombre.lower()        
        receta.Receta.eliminarUnaReceta(nombre)
        