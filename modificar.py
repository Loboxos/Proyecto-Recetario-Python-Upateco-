import tkinter as tk
from tkinter import ttk,messagebox
import receta,agregarIngrediente,ingrediente,listaDingred

class ModificarReceta(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.nombreRE=tk.StringVar()
        self.nombreNuevo=tk.StringVar()
        self.ingredienteNuevo=tk.StringVar()
        self.preparacionNuevo=tk.StringVar()
        self.tiempoPropRNuevo=tk.StringVar()
        self.tiempoCoccRnuevo=tk.StringVar()
        self.parent=parent
        

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
        nombreR_label = ttk.Label(self, text="Ingrese nombre de la receta a modificar:")
        nombreR_label.grid(column=0 , row=0, sticky=tk.W, padx=5, pady=5)

        nombreR_entry = ttk.Entry(self,textvariable=self.nombreRE)
        nombreR_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
        buscar_button = ttk.Button(self, text="Buscar",command=self.mostrar_datos)
        #messagebox.showinfo(title="Actualizacion",message="se elimino la receta correctamente")
        buscar_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
      
    def mostrar_datos(self):
        nombre=self.nombreRE.get()
        recet=receta.Receta.mostrarReceta(nombre)
        print(recet)
    
        frame2 = ttk.Frame(self, borderwidth=2, relief="groove")
        frame2.grid(row=2, column=1, sticky=tk.NSEW)
        ttk.Label(frame2, text="RECETA",background="green",width="50",anchor="center").grid()
        ttk.Label(frame2, text=recet['nombre'],background="lightgreen",anchor="nw").grid()
        
        nombreNuevo_label = ttk.Label(frame2, text="Nuevo nombre de Receta")
        nombreNuevo_label.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        nombreNuevo_entry = ttk.Entry(frame2,textvariable=self.nombreNuevo)
        nombreNuevo_entry.grid(column=2, row=1, sticky=tk.E, padx=5, pady=5)

        ingrNuevos_label = ttk.Label(frame2, text="Ingredientes nuevos")
        ingrNuevos_label.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        ttk.Button(frame2, text="agregar",command=self.tablaConEntrada).grid(column=2, row=2, sticky=tk.W)

        preparNuevo_label = ttk.Label(frame2, text="preparacion")
        preparNuevo_label.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

        preparNuevo_entry = ttk.Entry(frame2,textvariable=self.preparacionNuevo)
        preparNuevo_entry.grid(column=2, row=5, sticky=tk.E, padx=5, pady=5)
        
        ttk.Label(frame2, text="ingredientes:").grid()
        for ingrediente in recet['listaDeIngredientes']:
            ttk.Label(frame2, text=f"{ingrediente}, ").grid()

        ttk.Label(frame2, text=f"preparacion: {recet['preparacion']}" ).grid()
        guardar_button = ttk.Button(self, text="Modificar",command=lambda:[self.guardar_datos(),self.mensaje()])

        guardar_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
        
    def mensaje(self):
        messagebox.showinfo("Aviso","Se modifico la receta correctamente")

    def tablaConEntrada(self):
        toplevel = tk.Toplevel(self.parent)
        agregarIngrediente.AgregarIngrediente(toplevel).pack()

    def guardar_datos(self):
        nombreRe=self.nombreRE.get()
        nombreNuevo=self.nombreNuevo.get()

        listaIngr=agregarIngrediente.listaDingredi
        for ingred in listaIngr:
            ing=ingrediente.Ingrediente(ingred[0],ingred[1],ingred[2])

        #listaFinal=listaDingred.ListDingredientes(listaIngr)
        
        preparacion=self.preparacionNuevo.get()
        nombreRe=nombreRe.lower()

        receta.Receta.modificarUnaReceta(nombreRe,nombreNuevo,listaIngr,preparacion)
