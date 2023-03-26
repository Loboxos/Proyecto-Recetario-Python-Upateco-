class Ingrediente:
    def __init__(self,nombre,unidadDmedida,cantidad):
        self.nombre = nombre
        self.unidadDmedida = unidadDmedida
        self.cantidad = cantidad
        
    def __str__(self):
        return f"nombre:{self.nombre}/nUnidadDmedida:{self.unidadDmedida}/nCantidad:{self.cantidad}"
        
    