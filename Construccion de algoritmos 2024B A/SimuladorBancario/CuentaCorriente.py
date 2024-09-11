__autor__="Juan Felipe Zambrano"
__licence__="GPL"
__version__="1.0.0"
__email__="juan.zambranoparra@campusucc.edu.co"

class CuentaCorriente:
    # Aqui inicia mi clase

    #------------------------------------------------------
    # Atributo
    #-------------------------------------------------------

    __saldo = 0

    #------------------------------------------------------
    # Metodos
    #------------------------------------------------------
    __method__="ConsignarValor"
    __params__="Monto"
    __returns__="Ninguno"
    __descriptions__="Este metodo permite consignar un monto a la cuenta"  

    def consignarValor (self, monto):
         self.__saldo = self.__saldo+monto
    
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

    __method__="Ahorrar"
    __params__="Monto"
    __returns__="Ninguno"
    __descriptions__="Este metodo permite pasar el ahorro de la cuenta corriente a la cuenta de ahorros"  
  
    
    def DarSaldoCorriente (self):
        return self.__saldo
