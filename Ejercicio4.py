class Cuenta_Bank():
    def __init__(self,id,titular,fecha,num_cuenta,saldo):
        self.id = id
        self.titular = titular
        self.fecha = fecha
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    def retirar_dinero(self, num_retirar):
        if self.saldo > num_retirar:
            self.saldo = self.saldo - num_retirar
    
    def ingresar_dinero(self, num_ingresar):
        self.saldo = self.saldo + num_ingresar
