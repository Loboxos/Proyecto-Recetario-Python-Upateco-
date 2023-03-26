import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.filedialog import askopenfilename
import receta,secundaria
#import ventanasecundaria

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent,padding=10,borderwidth=1,relief="groove")
        self.parent=parent
        
        

        parent.title("Recetario")
        
        
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        #self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
        
        frame1 = ttk.Frame(self, borderwidth=2, relief="groove")    # crea el frame
        frame1.grid(row=1, column=1,columnspan=2, sticky=tk.NSEW)    # inserta el frame al frame principal
        # inserta el frame al frame principal
       
        frame1.columnconfigure(0, weight=1) # configura columna 0 (default)
        frame1.rowconfigure(0, weight=1) # configura fila 0 (default)
        ttk.Label(frame1, text="Recetario",background="lightgreen",width="200",anchor="center").grid(padx=5, pady=5, sticky=tk.N)  # crea label y la inserta
        
        recetaPrinc=receta.Receta.mostrarUnaRecetaDiaria()
        print(recetaPrinc)

        frame2 = ttk.Frame(self, borderwidth=2, relief="groove")
        frame2.grid(row=2, column=1, sticky=tk.NSEW)
        ttk.Label(frame2, text="RECETA DEL DIA",background="green",width="50",anchor="center").grid()
        ttk.Label(frame2, text=recetaPrinc['nombre'],background="lightgreen",anchor="nw").grid()
        ttk.Label(frame2, text="ingredientes:").grid()
        for ingrediente in recetaPrinc['listaDeIngredientes']:
            ttk.Label(frame2, text=f"{ingrediente}, ").grid()
        
        ttk.Label(frame2, text=f"preparacion: {recetaPrinc['preparacion']}" ).grid()
        
      

       


        frame4 = ttk.Frame(self, borderwidth=1, relief="groove")
        frame4.grid(row=2, column=2, sticky=tk.NSEW)
        frame4.columnconfigure(0, weight=0)
        frame4.rowconfigure(0, weight=0)

        
        comida=recetaPrinc['nombre']
        comida=comida.replace(" ","")
        rutaImg=recetaPrinc['imagen']
        self.imagen = tk.PhotoImage(file=rutaImg)
        ttk.Label(frame4, image=self.imagen,background="lightgreen").grid()
        
       
        frame5 = ttk.Frame(self, borderwidth=1, relief="groove")
        frame5.grid(row=4,column=1,columnspan=2, sticky=tk.NSEW)
        frame5.columnconfigure(0, weight=2)
        frame5.rowconfigure(0, weight=2)
        ttk.Label(frame5, text="*****MAS RECETAS******",background="green",width="100",anchor="center").grid(row=3,column=1,columnspan=2,sticky=tk.S)


        # definimos 2 columnas 1: tabla, 2: barra de desplazamiento
       
       
       #no cambia si lo borramos
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
        
        
   
        
        frame5.tabla = ttk.Treeview(self, columns=columnas,show='headings',selectmode="browse") # sin multi-seleccion
        frame5.tabla.grid(row=5, column=1,columnspan=2, sticky=(tk.NSEW))
        

        # definimos los encabezados que se muestran
        frame5.tabla.heading('Receta', text='Receta')
        frame5.tabla.heading('ingredientes', text='ingredientes')
        frame5.tabla.heading('etiquetas', text='etiquetas')
        frame5.tabla.heading('Tpreparacion', text='Tpreparacion')
        frame5.tabla.heading('Tcoccion', text='Tcoccion')
 
        #self.frame5=frame5
        
        # generar los datos artificiales
        contacts = []
        cantRecetas=len(receta.Receta.listaDeRecetas())
        for x in receta.Receta.listaDeRecetas():
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

        tk.Button(self, text="*****ACTUALIZAR******",bg='CadetBlue',command=self.actualizarTabla).grid(row=7,column=1,sticky=tk.S)
        tk.Button(self, text="*****MAS OPCIONES******",bg='CadetBlue',command=self.abrir_ventana).grid(row=7,column=2,sticky=tk.S)
    
    
    def actualizarTabla(self):
        frame5=self.frame5 = ttk.Frame(self, borderwidth=1, relief="groove")
        frame5.grid(row=4,column=1,columnspan=2, sticky=tk.NSEW)
        frame5.columnconfigure(0, weight=2)
        frame5.rowconfigure(0, weight=2)
        ttk.Label(frame5, text="*****MAS RECETAS******",background="green",width="100",anchor="center").grid(row=3,column=1,columnspan=2,sticky=tk.S)


        # definimos 2 columnas 1: tabla, 2: barra de desplazamiento
       
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
 
        #self.frame5=frame5
        
        # generar los datos artificiales
        contacts = []
        cantRecetas=len(receta.Receta.listaDeRecetas())
        
        for x in receta.Receta.listaDeRecetas():
            nombre=x['nombre']
            ingredientes=x['listaDeIngredientes']
            etiquetas=x['etiquetas']
            tiempoPrep=x['tiempoDePrep']
            tiempoCocc=x['tiempoDeCocc']
            contacts.append((f'{nombre}', f'{ingredientes} ',f'{etiquetas}', f'{tiempoPrep}MIN', f'{tiempoCocc}MIN'))

        # agregar datos al treeview
        for contact in contacts:
            frame5.tabla.insert('', tk.END, values=contact)

    
 

    def abrir_ventana(self):
        toplevel = tk.Toplevel(self.parent)
        # agregamos el frame (Secundaria) a la ventana (toplevel)
        secundaria.Secundaria(toplevel).pack()



root=tk.Tk()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.iconbitmap('img\chef.ico')
#root.geometry('1400x900')



#root.config(bg="red")
App(root).grid(sticky=tk.NSEW)
#root.resizable(False, False)#para que no se pueda redimensionar la ventana


root.mainloop()