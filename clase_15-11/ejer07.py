class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Depositados {cantidad}. Nuevo saldo: {self.__saldo}")

    def __mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")

# Crear instancia y usar métodos
mi_cuenta = CuentaBancaria("Ana", 1000)
mi_cuenta.depositar(500)
# mi_cuenta.__mostrar_saldo()  # Esto daría un error porque es un método privado
print(mi_cuenta.titular)