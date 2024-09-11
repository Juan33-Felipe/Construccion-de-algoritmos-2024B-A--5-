__autor__="Juan Felipe Zambrano"
__licence__="GPL"
__version__="1.0.0"
__email__="juan.zambranoparra@campusucc.edu.co"

class CDT:
    # Aqui inicia mi clase

    """------------------------------------------------------
    # Atributo
    ------------------------------------------------------"""

    interes = 0
    inversion = 0
    fecha = 0

    """------------------------------------------------------------
    # Metodos
    ------------------------------------------------------------"""   
    
    __method__="CambiarInteres"
    __params__="nuevoInteres"
    __returns__="Nada"
    __descriptions__="Este metodo establece el valor de el interes"
    
    def CambiarInteres(self, nuevoInteres):
        # Aqui inicia mi metodo 
      self.interes = nuevoInteres  
    
    __method__="DarInteres"
    __params__="Ninguno"
    __returns__="Nuevo Interes"
    __descriptions__="Refleja el interes en la cuenta del usuario"  

    def DarInteres(self):
        #Aqui inicia mi metodo
        return self.interes