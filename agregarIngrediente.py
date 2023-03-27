import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename



class AgregarIngrediente(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Agregar ingredientes")
        parent.iconbitmap('img\chef.ico')
        # parent.resizable(False, False)
        parent.geometry("500x500")
        
        self.parent = parent
        self.nombre=tk.StringVar()
        self.unidadDmedida=tk.StringVar()
        self.cantidad=tk.StringVar()
        
        set = ttk.Treeview(parent)
        set.pack()
        self.set=set
        datos=[]
        self.datos=datos
        
        
        set['columns'] = ('nombre', 'unidadDmedida', 'cantidad')
        set.column("#0", width=0,  stretch="NO")
        set.column("nombre", anchor="center", width=80)
        set.column("unidadDmedida", anchor="center", width=80)
        set.column("cantidad", anchor="center", width=80)

        set.heading("#0", text="", anchor="center")
        set.heading("nombre", text="nombre", anchor="center")
        set.heading("unidadDmedida", text="unidadDmedida", anchor="center")
        set.heading("cantidad", text="cantidad", anchor="center")
        # data
        
       
        
        global count
        count = 0


        nombre = ttk.Label(self, text="nombre")
        nombre.grid(row=0, column=0)

        unidadDmedida = ttk.Label(self, text="unidadDmedida")
        unidadDmedida.grid(row=0, column=1)

        cantidad = ttk.Label(self, text="cantidad")
        cantidad.grid(row=0, column=2)

        nombre_entry =ttk.Entry(self,textvariable=self.nombre)
        nombre_entry.grid(row=1, column=0)

        unidadDmedida_entry = ttk.Entry(self,textvariable=self.unidadDmedida)
        unidadDmedida_entry.grid(row=1, column=1)

        cantidad_entry = ttk.Entry(self,textvariable=self.cantidad)
        cantidad_entry.grid(row=1, column=2)
        
        self.nombre_entry=nombre_entry
        self.unidadDmedida_entry=unidadDmedida_entry
        self.cantidad_entry=cantidad_entry
        ttk.Button(self, text="cargar",command=self.input_record).grid(column=1,row=5)
        ttk.Button(self,text="cerrar",command=parent.destroy).grid(column=1,row=7)
        ttk.Button(self,text="guardar",command=lambda:[self.guardar(),self.mensaje()]).grid(column=1,row=6)
        
    global listaDingredi
    
    def mensaje(self):
        messagebox.showinfo("Aviso","Ingredientes agregados")
    
    def guardar(self):
        global listaDingredi
        
        listaDingredi=[]
        
        for x in self.set.get_children():
            datos=self.set.item(x)["values"]
            listaDingredi.append(datos)

    def input_record(self):
        global count
        self.set.insert(parent='',index='end',iid = count,text='',values=(self.nombre.get(),self.unidadDmedida.get(),self.cantidad.get()))
    
        count += 1
        self.nombre_entry.delete(0,"end")
        self.unidadDmedida_entry.delete(0,"end")
        self.cantidad_entry.delete(0,"end")
        
        
