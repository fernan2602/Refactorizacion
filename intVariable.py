class solicitud:
    def __init__(self,tipo,cantidad,precio):
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio = precio
    
    def invVariable(self):
        comparacion = self.tipo == 2 and self.cantidad > 10 and self.precio < 100
        if comparacion:
            print("Descuento 0.5M")

prueba = solicitud(2,50,90)
prueba.invVariable()














"""class solicitud:

    def __init__(self,tipo,cantidad,precio):
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio = precio

    def invVariable(self):
        if(self.tipo == 2 and self.cantidad > 10 and self.precio < 100):
            print("Desceunto = 0.5M")

prueba = solicitud(2,50,90)
prueba.invVariable()"""



            





















