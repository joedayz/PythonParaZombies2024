class CuentaBancaria:
          def __init__(self, numero_cuenta, titular, saldo=0.0):
                    self.numero_cuenta = numero_cuenta
                    self.titular = titular
                    self.saldo = saldo
          
          def depositar(self, monto):
                    if(monto>0):
                              self.saldo += monto
                              print(f"Depósito de {monto} realizado. Saldo actual: {self.saldo}")
                    else:
                              print("Monto inválido. El monto debe ser mayor a 0.")

          def retirar(self, monto):
                    if(monto>0 and monto<=self.saldo):
                              self.saldo -= monto
                              print(f"Retiro de {monto} realizado. Saldo actual: {self.saldo}")
                    else:
                              print("Fondos insuficientes o monto no válido.")                              
                              
          def __str__(self) -> str:
                    return f"Cuenta: {self.numero_cuenta}\nTitular: {self.titular}\nSaldo: {self.saldo}"
          
class CuentaAhorros(CuentaBancaria):
          def __init__(self, numero_cuenta, titular, saldo=0.0, tasa_interes=0.0):
                    super().__init__(numero_cuenta, titular, saldo)
                    self.tasa_interes = tasa_interes
                      
          def aplicar_interes(self):
                    interes = self.saldo * self.tasa_interes
                    print(f"Interés generado: {interes}")
                    self.depositar(interes)

class CuentaCorriente(CuentaBancaria):
          def __init__(self, numero_cuenta, titular, saldo=0.0, sobregiro=0.0):
                    super().__init__(numero_cuenta, titular, saldo)
                    self.sobregiro = sobregiro
          
          def retirar(self, monto):
                    if(monto>(self.saldo+self.sobregiro)):
                              print("Fondos insuficientes o monto no válido.")
                              return           
                    self.saldo -= monto
                    print(f"Retiro de {monto} realizado. Saldo actual: {self.saldo}")
                              
                    
                              
                              
cuenta1 = CuentaAhorros("123456","Carlos", 1000, 0.05)
print(cuenta1)

cuenta1.depositar(500)
cuenta1.aplicar_interes()

cuenta2 = CuentaCorriente("654321","Jose", 1000, 500)
print(cuenta2)
cuenta2.depositar(500)
cuenta2.retirar(2000)
print(cuenta2)
