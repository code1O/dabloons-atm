import os

class cajero:

    def __init__(self):
        self.continuar = True
        self.monto = 0
        self.menu()

    def contraseña(self):
        contador = 1
        while contador <= 3:
            x = int(input("Ingrese su contraseña: "))
            if x == 5467:
                print("contraseña correcta")
                break
            else:
                print(f"Contraseña incorrecta, le quedan {3 - contador} intentos")
                if contador == 3:
                    print("No puede realizar operaciones")
                    self.continuar = False
    def menu(self):
        os.system('cls')
        self.contraseña()
        os.system('cls')
        opcion = 0
        while True:
            print(""" 

        Bienvenido al cajero automatico de dabloons

            ******Menu******

            1- Depositar 
            2- Retirar
            3- Ver saldo
            4- Salir
            """)
            opcion = int(input("Elige una opción: "))
            if self.continuar:
                if opcion == 1:
                    self.depositar()
                    import comprar
                    break
                elif opcion == 2:
                    self.retiro()
                elif opcion == 3:
                    self.ver()
                elif opcion == 4:
                    break
    def depositar(self):
        dep = int(input("Ingrese el monto a depositar: "))
        print(f"Su nuevo saldo es {self.monto + dep}")
        self.monto+=dep
    def retiro(self):
        retirar = int(input("¿Cuánto desea retirar?: "))
        print("Su monto actual es", self.monto)
        self.monto-=retirar
    def ver(self):
            print("Su saldo es: ", self.monto)
            
app = cajero()
