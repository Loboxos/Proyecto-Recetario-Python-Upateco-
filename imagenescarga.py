from tkinter import filedialog as FileDialog

def test():
    fichero = FileDialog.askopenfilename(filetypes=(("Ficheros de imagen .gif", "*.gif"),("Todos los ficheros","*.*")))
    ruta = FileDialog.asksaveasfile(initialdir="img",defaultextension=".gif")
    print(fichero)
test()