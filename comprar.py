import os
from tkinter import messagebox
class tienda:
    
    def __init__(self):
        self.continuar = True
        self.monto = 55030
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
                    messagebox.showinfo("Compra ", "objeto comprado")
                    break
            elif opcion == 2:
                vender = input("¿Que deseas vender?: ")
                if(vender):
                    usuario = input("¿A quién lo deseas vender?: ")
                    if(usuario):
                        precio = input("Precio de la venta: ")
                        if(precio):
                            messagebox.showinfo(f"venta exitosa", "Objeto vendido")
                            break
            elif opcion == 3:
                import index
                break
app = tienda()