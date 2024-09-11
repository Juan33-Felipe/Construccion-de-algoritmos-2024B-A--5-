__autor__="Juan Felipe Zambrano"
__licence__="GPL"
__version__="1.0.0"
__email__="juan.zambranoparra@campusucc.edu.co"

"""------------------------------------------------------
# Importaciones
------------------------------------------------------"""
from CuentaAhorros import CuentaAhorros 
from CuentaCorriente import CuentaCorriente
from CDT import CDT 

class Simulador_Bancario:
    # Aqui inicia mi clase

    #------------------------------------------------------
    # Atributo
    #-------------------------------------------------------

    __cedula = ""
    __nombre = ""


    #-----------------------------------------------------------
    # Asociaciones
    #------------------------------------------------------------

    __cuentaCorriente = CuentaCorriente()
    __cuentaAhorros =  CuentaAhorros()
    __CDT = CDT()

    __mesActual = 0

    #------------------------------------------------------
    # Metodos
    #------------------------------------------------------

    __method__="ConsignarCuentaCorriente"
    __params__="Monto"
    __returns__="Ninguno"
    __descriptions__="Este metodo permite consignar un monto a la cuenta"  

    def consignarCuentaCorriente (self, monto):
        #Aqui inicia el metodo
        #self.__cuentaCorriente.saldo = self.__cuentaCorriente.saldo+monto # modo no recomendable
        self.__cuentaCorriente.consignarValor(monto)

    __method__="CalcularSaldoTotal"
    __params__="Ninguno"
    __returns__="Saldo Total"
    __descriptions__="Este metodo suma el saldo de todas las cuentas"   
    
    def CalcularSaldoTotal(self):
        #Aqui inicia el metodo
        #forma 1
        total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        return total
    
    __method__="PasarAhorrosACorriente"
    __params__="Ninguno"
    __returns__="Ninguno"
    __descriptions__="Este metodo transfiere el saldo de ahorros a corriente"   
    
    def PasarAhorrosACorriente(self):
        saldoTemporal = self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarValor(saldoTemporal)
        self.__cuentaCorriente.consignarValor(saldoTemporal)

    __method__="Ahorrar"
    __params__="Monto"
    __returns__="Ninguno"
    __descriptions__="Este metodo permite pasar un monto de la cuenta corriente a la cuenta de ahorros"  

    def Ahorrar (self, monto):
        self.__cuentaCorriente.RetirarValor(monto)
        self.__cuentaAhorros.consignarValor(monto)

    __method__="RetirarTodo"
    __params__="Ninguno"
    __returns__="cantidad retirada"
    __descriptions__="Este metodo permite retirar todo el saldo de la cuenta corriente"   
    
    def RetirarTodo (self, total):
        total = self.__cuentaCorriente.DarSaldo() + self.__cuentaAhorros.Darsaldo()
        self.__cuentaAhorros.RetirarValor(self.__cuentaAhorros.Darsaldo())
        self.cuentaCorriente.RetirarValor(self.__cuentaCorriente.DarSaldo())
        return"Usted acaba de retirar"+total
    
    __method__='DuplicarAhorro'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__='Duplica la cantidad de dinero que hay en la cuenta de ahorros'

    def DuplicarAhorro(self):
      #Aqui inicia el metodo
      self.__cuentaAhorros.ConsignarValor(self.__cuentaAhorros.DarSaldo())

    
    