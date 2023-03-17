import tkinter as tk
from tkinter import ttk
import receta

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
        self.imagen = tk.PhotoImage(file="img/pizza.gif")
        ttk.Label(frame4, image=self.imagen,background="lightgreen").pack(anchor="center")
        
        frame5 = ttk.Frame(self, borderwidth=1, relief="groove")
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
        
        # generar los datos artificiales
        contacts = []
        for n in range(1, 30):
            contacts.append((f'MILANESA', f'[SALSA,QUESO,PAN RALLADO] ',f'[rico,facil]', f'{n}MIN',f'{n}MINCocc'))

        # agregar datos al treeview
        for contact in contacts:
            frame5.tabla.insert('', tk.END, values=contact)

        ttk.Button(self, text="*****MAS OPCIONES******",command=self.abrir_ventana).grid(row=7,column=1,columnspan=2,sticky=tk.S)
    
    def abrir_ventana(self):
        # creamos la ventana secundaria
        # como padre indicamos la ventana principal
        toplevel = tk.Toplevel(self.parent)
        # agregamos el frame (Secundaria) a la ventana (toplevel)
        Secundaria(toplevel).grid()


class Secundaria(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Mas opciones")
        #parent.geometry("450x200+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.iconbitmap('img\chef.ico')
        parent.resizable(False, False)
        ttk.Button(self, text="Cerrar",width=100, command=parent.destroy).grid()
        ttk.Button(self, text="Buscar Receta",width=100).grid() 
        ttk.Button(self, text="Agregar Receta",width=100).grid()
        ttk.Button(self, text="Eliminar receta",width=100).grid() 
        ttk.Button(self, text="modificar receta",width=100).grid()




#print(recetaPrinc)
# Finalmente bucle de la aplicación

root=tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.iconbitmap('img\chef.ico')
root.geometry('1000x600')
#root.config(bg="red")
App(root).grid(sticky=tk.NSEW)
root.resizable(False, False)#para que no se pueda redimensionar la ventana
root.mainloop()