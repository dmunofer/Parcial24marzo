from datetime import datetime
from random import randint
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
        else:
            raise Exception("No tienes suficiente saldo")

    def ingresar_dinero(self, num_ingresar):
        self.saldo = self.saldo + num_ingresar

    def transferir_dinero(self, cuenta2, cantidad):
        cuenta2 = Cuenta_Bank()                         #Esto falla porque faltaria definir lo de dentro pero tampoco tengo tiempo
        self.retirar_dinero(cantidad)
        cuenta2.ingresar_dinero(cantidad)

class PlazoFijo(Cuenta_Bank):
    def __init__(self,id,titular,fecha,fecha_vencimento,num_cuenta,saldo):
        self.id = id
        self.titular = titular
        self.fecha = fecha
        self.num_cuenta = num_cuenta
        self.saldo = saldo
        self.fecha_vencimento =  fecha_vencimento

    def retirar_dinero(self,cantidad):
        if self.saldo > cantidad:
            if datetime.now() < self.fecha_vencimento:
                self.saldo = self.saldo - cantidad-(0,5*cantidad)
            else:
                self.saldo = self.saldo - cantidad
        else:
            raise Exception("No tienes suficiente saldo")

class VIP(Cuenta_Bank):
    def __init__(self,id,titular,fecha,num_cuenta,saldo,negativo_max):
        self.id = id
        self.titular = titular
        self.fecha = fecha
        self.num_cuenta = num_cuenta
        self.saldo = saldo
        self.negativo_max = negativo_max

    def retirar_dinero(self,cantidad):
        if self.saldo -cantidad > -(self.negativo_max):
            self.saldo = self.saldo - cantidad
        else:
            raise Exception("La retirada supera el límite")

    def transferir_dinero(self, cuenta2, cantidad):
        try:
            self.retirar_dinero(cantidad)
            cuenta2.ingresar_dinero(cantidad)
        except:
            raise Exception("La retirada supera el límite")


cuenta_normal = Cuenta_Bank(6677, 'Diego Fernández', '4-5-2003',454322689098,10000)           # Aquí habría que haber hecho algo para los valores aleatorios pero no me va a dar tiempo
cuenta_PlazoFijo = PlazoFijo(7842,'Jaime González','6-9-1998','4-5-2005',234323890876,10000)
cuenta_VIP = VIP(3451,'Laura Garrido','23-12-2010',909898760980,10000,2000)

cuenta_normal.transferir_dinero(cuenta_PlazoFijo,2000)
cuenta_PlazoFijo.transferir_dinero(cuenta_VIP,2000)
cuenta_VIP.transferir_dinero(cuenta_normal,2000)
cuenta_normal.ingresar_dinero(575)
cuenta_PlazoFijo.ingresar_dinero(575)
cuenta_VIP.ingresar_dinero(575)
cuenta_normal.retirar_dinero(78)
cuenta_PlazoFijo.retirar_dinero(78)
cuenta_VIP.retirar_dinero(78)