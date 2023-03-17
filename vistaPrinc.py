import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Recetario')#titulo
root.iconbitmap('chef.ico') 
root.geometry('600x400+50+50')#geometria
etiqueta=tk.Label(root, text="RECETA DEL DIA",bg= "salmon")#label
etiqueta.pack(fill=tk.X)#posicio

img=tk.PhotoImage(file="pizza2.png")
lbl_img=tk.Label(root,image=img)



lbl_img.pack()
root.mainloop()