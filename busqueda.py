import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.filedialog import askopenfilename
import receta


class buscarReceta(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Buscar una Receta")
        parent.iconbitmap('img\chef.ico')
        #parent.geometry("1200x400")
        parent.resizable(0, 0)

        parent.configure(background="#CCEEFF")

        
        
        self.nombreRE=tk.StringVar()
        self.combo1_str = tk.StringVar()
        
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        
        self.create_widgets()
        ttk.Button(self,text="cerrar",command=parent.destroy).grid(column=0,row=5)

    def create_widgets(self):
        # Ingresar comida
       
        nombre_label = ttk.Label(self, text="Buscar nombre por:")
        nombre_label.grid(column=1 , row=0, sticky=tk.W, padx=5, pady=5)

        
        self.combo1 = ttk.Combobox(self, textvariable=self.combo1_str,
                                   width=40)
        self.combo1.grid(row=0, column=2, padx=5, pady=5)
        self.combo1["values"] = ("Nombre", "etiquetas","tiempo de preparacion 'min'-'min'","ingredientes")
        self.combo1["state"] = "readonly"
        self.combo1.bind('<<ComboboxSelected>>', self.on_combo_changed)

     
        self.cartel_str = tk.StringVar()

        self.cartel = ttk.Label(self, text="", textvariable=self.cartel_str,
                                width=40)
        self.cartel.grid(row=0, column=3, padx=5, pady=5)
      
        nombre_entry = ttk.Entry(self,textvariable=self.nombreRE)
        nombre_entry.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)
        
        ttk.Button(self, text="Buscar receta",command=self.tabla).grid(column=0,row=6)

    def on_combo_changed(self,evento):
        if self.combo1_str.get() == "Nombre":
            self.cartel_str.set(1)
           
        elif self.combo1_str.get() == "etiquetas":
            self.cartel_str.set(2)
        
        elif self.combo1_str.get() == "tiempo de preparacion 'min'-'min'":
            self.cartel_str.set(3)
        
        elif self.combo1_str.get() == "ingredientes":
            self.cartel_str.set(4)
            
    def tabla(self):
        
        nombre=self.nombreRE.get()
        print(nombre)
        opcion=self.cartel_str.get()
        print(opcion)

        frame5 = ttk.Frame(self, borderwidth=1, relief="groove")
        frame5.grid(row=4,column=1,columnspan=2, sticky=tk.NSEW)
        frame5.columnconfigure(0, weight=2)
        frame5.rowconfigure(0, weight=2)
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
 
        contacts = []
        lisrec=receta.Receta.buscarUnaReceta(opcion,nombre)
    
        for x in lisrec:

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
        