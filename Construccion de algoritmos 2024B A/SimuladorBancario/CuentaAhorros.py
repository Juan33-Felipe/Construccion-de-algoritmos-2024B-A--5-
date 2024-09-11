__autor__="Juan Felipe Zambrano"
__licence__="GPL"
__version__="1.0.0"
__email__="juan.zambranoparra@campusucc.edu.co"

class CuentaAhorros:
    # Aqui inicia mi clase

    #------------------------------------------------------
    # Atributo
    #------------------------------------------------------

    saldo = 0
    interes = 0

    #------------------------------------------------------
    # Metodos
    #------------------------------------------------------

    __method__= "ConsignarValor"
    __params__= "Monto"
    __returns__ = "Nada"
    __descriptions__ = "Este método me permite consignar un monto a la cuenta."
    
    def ConsignarValor(self, monto):
        self._saldo = self._saldo+monto
        

    __method__="DarSaldo"
    __params__="Ninguno"
    __returns__="Saldo"
    __descriptions__="Este metodo retorna el saldo"   
    
    def DarSaldo (self):
        return self.__saldo
    

    __method__="RetirarValor"
    __params__="Monto"
    __returns__="Nada"
    __descriptions__="Este metodo retira un monto de la cuenta"   
    
    def RetirarValor (self, monto):
        self.__saldo = self.__saldo-monto


    __method__="RetirarAhorro"
    __params__="Monto"
    __returns__="Nada"
    __descriptions__="Este metodo retira un monto del ahorro de la cuenta"   
    
    def RetirarAhorro (self, monto):
        self.__ahorro = self.__ahorro-monto


    __method__="RetirarTodo"
    __params__="Total"
    __returns__="Nada"
    __descriptions__="Este metodo permite retirar todo el saldo de la cuenta de ahorros"   
    
    def RetirarTodo (self, total):
      self.__saldo = self.__saldo-total

    
    