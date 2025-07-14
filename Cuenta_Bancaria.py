import os

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nNro de Cuenta: {self.numero_cuenta}\nBalance: {self.balance}"

    def depositar(self, cantidad):

        if cantidad > 0:
            self.balance += cantidad
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Has depositado ${cantidad}. Tu nuevo balance es: ${self.balance}")
        else:
            print("Error: No puedes depositar una cantidad negativa o cero.")


    def retirar(self, cantidad):

        if cantidad > 0:
            if cantidad <= self.balance:
                self.balance -= cantidad
                print(f"Has retirado ${cantidad}. Tu nuevo balance es: ${self.balance}")
            else:
                print("Fondos insuficientes. No puedes retirar más dinero del que tienes.")
        else:
            print("Error: No puedes retirar una cantidad negativa o cero.")

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pausa para volver al menú
def pausar():
    input("\nPresiona Enter para volver al menú...")

# Función para crear un cliente
def crear_cliente():
    limpiar_pantalla()
    nombre = input("Ingrese su(s) nombre(s): ")
    limpiar_pantalla()
    apellido = input("Ingrese su(s) apellido(s): ")
    limpiar_pantalla()
    numero_cuenta = input("Indique cuál es su nro de cuenta bancaria: ")
    balance = 5000

    cliente = Cliente(nombre,apellido,numero_cuenta,balance)

    return cliente

def inicio():

    # Primero crear el cliente
    mi_cliente = crear_cliente()

    # Loop principal del programa
    while True:
        # Limpiar pantalla
        limpiar_pantalla()

        print("\n" + str(mi_cliente))
        print("\n¿Qué operación quieres realizar?")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            cantidad = float(input("¿Cuánto dinero quieres depositar? "))
            mi_cliente.depositar(cantidad)
            pausar()

        elif opcion == "2":
            cantidad = float(input("¿Cuánto dinero quieres retirar? "))
            mi_cliente.retirar(cantidad)
            pausar()

        elif opcion == "3":
            print("¡Gracias por usar nuestro sistema bancario!")
            break

# Para ejecutar el programa
if __name__ == "__main__":
    inicio()
