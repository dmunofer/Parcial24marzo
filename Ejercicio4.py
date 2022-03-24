class Cuenta_Bank():
    def __init__(self,id=int,titular=str,fecha=int,num_cuenta=float,saldo=float):
        self.id = id
        self.titular = titular
        self.fecha = fecha
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    def retirar_dinero(self, num_retirar):
        if self.saldo > num_retirar:
            self.saldo = self.saldo - num_retirar
        else:
            raise Exception("No tienes suficiente saldo")

    def ingresar_dinero(self, num_ingresar):
        self.saldo = self.saldo + num_ingresar

    def transferir_dinero(self, cuenta2, cantidad):
        try:
            self.retirar_dinero(cantidad)
            cuenta2.ingresar_dinero(cantidad)
        except:
            raise Exception("No tienes suficiente saldo")



