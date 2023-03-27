from json import JSONDecodeError
import tkinter as tk
from tkinter import ttk,messagebox
import receta,menu


class App(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent,padding=10,borderwidth=1,relief="groove")
        self.parent=parent
        self.parent.title("Recetario") #titulo de la ventana
        
        frame1 = ttk.Frame(self, borderwidth=2, relief="groove")    # crea el frame titulo
        frame1.grid(row=1, column=1,columnspan=2, sticky=tk.NSEW)    # inserta el frame al frame principal
        
        ttk.Label(frame1, text="Recetario",background="lightgreen",width="200",anchor="center").grid(padx=5, pady=5, sticky=tk.N)  # crea label y la inserta
       
        
       #try:
        recetaPrinc=receta.Receta.mostrarUnaRecetaDiaria()
        print(recetaPrinc)
 
        frame2 = ttk.Frame(self, borderwidth=2, relief="groove")   #frame receta principal
        frame2.grid(row=2, column=1, sticky=tk.NSEW)

        #labels de la receta principal
        ttk.Label(frame2, text="RECETA DEL DIA",background="green",width="50",anchor="center").grid()
        ttk.Label(frame2, text=recetaPrinc['nombre'],background="lightgreen",anchor="nw").grid()
        ttk.Label(frame2, text="ingredientes:").grid()
        for ingrediente in recetaPrinc['listaDeIngredientes']:
            ttk.Label(frame2, text=f"{ingrediente}, ").grid()
        ttk.Label(frame2, text=f"preparacion: {recetaPrinc['preparacion']}" ).grid()
        
                                                                  
        frame4 = ttk.Frame(self, borderwidth=1, relief="groove")   #frame imagen de la receta principal
        frame4.grid(row=2, column=2, sticky=tk.NSEW)
        frame4.columnconfigure(0, weight=0)
        frame4.rowconfigure(0, weight=0)

        
        comida=recetaPrinc['nombre']
        comida=comida.replace(" ","")

        rutaImg=recetaPrinc['imagen']
        self.imagen = tk.PhotoImage(file=rutaImg)
        ttk.Label(frame4, image=self.imagen,background="lightgreen").grid() #inserta imagen
        
    
        frame5 = ttk.Frame(self, borderwidth=1, relief="groove")  #frame tabla con otras recetas 

        frame5.grid(row=4,column=1,columnspan=2, sticky=tk.NSEW)
        
        frame5.columnconfigure(1, weight=1)
        frame5.rowconfigure(1, weight=1)

        ttk.Label(frame5, text="*****MAS RECETAS******",background="green",width="100",anchor="center").grid(row=3,column=1,columnspan=2,sticky=tk.S)


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

       
        lis = []
        for rec in receta.Receta.listaDeRecetas():
            nombre=rec['nombre']
            ingredientes=rec['listaDeIngredientes']
            etiquetas=rec['etiquetas']
            tiempoPrep=rec['tiempoDePrep']
            tiempoCocc=rec['tiempoDeCocc']
            lis.append((f'{nombre}', f'{ingredientes} ',f'{etiquetas}', f'{tiempoPrep}MIN', f'{tiempoCocc}MIN'))

        # agregar datos al treeview
        for li in lis:
            frame5.tabla.insert('', tk.END, values=li)
    
        self.frame5=frame5
       
        
     
    #except JSONDecodeError:
        tk.Button(self, text="*****ACTUALIZAR******",bg='CadetBlue',command=lambda:[self.mensaje(),self.actualizarTabla()]).grid(row=7,column=1,sticky=tk.S)
        tk.Button(self, text="*****MAS OPCIONES******",bg='CadetBlue',command=self.abrir_ventana).grid(row=7,column=2,sticky=tk.S)
   
    def mensaje(self):
        messagebox.showinfo("Aviso","Tabla Actualizada")
    
    def actualizarTabla(self):
        frame5=self.frame5 = ttk.Frame(self, borderwidth=1, relief="groove")
        frame5.grid(row=4,column=1,columnspan=2, sticky=tk.NSEW)
        
        frame5.columnconfigure(1, weight=1)
        frame5.rowconfigure(1, weight=1)
        
        ttk.Label(frame5, text="*****MAS RECETAS******",background="green",width="100",anchor="center").grid(row=3,column=1,columnspan=2,sticky=tk.S)
         
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
        lis = []
        
        for rec in receta.Receta.listaDeRecetas():
            nombre=rec['nombre']
            ingredientes=rec['listaDeIngredientes']
            etiquetas=rec['etiquetas']
            tiempoPrep=rec['tiempoDePrep']
            tiempoCocc=rec['tiempoDeCocc']
            lis.append((f'{nombre}', f'{ingredientes} ',f'{etiquetas}', f'{tiempoPrep}MIN', f'{tiempoCocc}MIN'))

        # agregar datos al treeview
        for li in lis:
            frame5.tabla.insert('', tk.END, values=li)
        
    def abrir_ventana(self):
        toplevel = tk.Toplevel(self.parent)
        # agregamos el frame (Menu) a la ventana (toplevel)
        menu.Menu(toplevel).pack()


root=tk.Tk()
root.iconbitmap('img\chef.ico')
App(root).grid(sticky=tk.NSEW)
root.resizable(False, False)#para que no se pueda redimensionar la ventana
root.mainloop()