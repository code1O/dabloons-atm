import os

class tienda:
    
    def __init__(self):
        self.continuar = True
        self.monto = 0
        self.menu()

    def menu(self):
        opcion = 0
        while True:

            print("""
            Tienda
            
            1- Comprar
            2- Vender
            3-  Volver atras
            """)
            opcion = int(input("Elige una opción: "))
            
            if opcion == 1:
                comprar = input("¿Qué desea comprar?: ")
                if(comprar):
                    precio = float(input("Precio: "))
                    print("Objeto comprado: ", comprar)
                    break
            elif opcion == 2:
                vender = input("¿Que deseas vender?: ")
                if(vender):
                    usuario = input("¿A quién lo deseas vender?: ")
                    if(usuario):
                        precio = input("Precio de la venta: ")
                        if(precio):
                            print(f"venta exitosa de {vender} a {usuario} por {precio} Dabloons")
                            break
            elif opcion == 3:
                import index
                break
app = tienda()