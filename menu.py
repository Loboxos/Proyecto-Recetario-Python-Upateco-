import tkinter as tk
from tkinter import ttk
import busqueda,agregar,modificar,eliminar


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        parent.title("Mas opciones")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.iconbitmap('img\chef.ico')
        parent.resizable(False, False)

        ttk.Button(self, text="Buscar Receta",command=self.abrir_ventana1,width=100).grid() 
        ttk.Button(self, text="Agregar Receta",command=self.abrir_ventana2,width=100).grid()
        ttk.Button(self, text="Eliminar receta",command=self.abrir_ventana3,width=100).grid() 
        ttk.Button(self, text="modificar receta",command=self.abrir_ventana4,width=100).grid()
        ttk.Button(self, text="Cerrar",width=100, command=parent.destroy).grid()
    
    def abrir_ventana1(self):
        toplevel = tk.Toplevel(self.parent)
        busqueda.buscarReceta(toplevel).grid()

    def abrir_ventana4(self):
        toplevel = tk.Toplevel(self.parent)
        modificar.ModificarReceta(toplevel).grid()

    def abrir_ventana3(self):
        toplevel = tk.Toplevel(self.parent)
        eliminar.EliminarReceta(toplevel).grid()

    def abrir_ventana2(self):
        toplevel = tk.Toplevel(self.parent)
        agregar.AgregarReceta(toplevel).grid()
        