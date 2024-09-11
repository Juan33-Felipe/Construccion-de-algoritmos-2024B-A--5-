__autor__="Juan Felipe Zambrano"
__licence__="GPL"
__version__="1.0.0"
__email__="juan.zambranoparra@campusucc.edu.co"

class Fecha:
    # Aqui inicia mi clase

   """------------------------------------------------------
   # Atributo
   ------------------------------------------------------"""

   dia = 0
   mes = 0
   anio = 0
    
   """------------------------------------------------------
   # Metodos
   ------------------------------------------------------"""
   method='DarDia'
   params='Ninguno'
   returns='Dia de la clase'
   descriptions='Devuelve el dia de la clase'
   
   
   def DarDia(self):
      # Aqui inicia mi método
      return self.dia
    
   
   method='DarMes'
   params='Ninguno'
   returns='Mes de la clase'
   descriptions='Devuelve al mes de la clase'
   

   def DarMes(self):
      # Aqui inicia mi método
      return self.mes
    

   method='DarAnio'
   params='Ninguno'
   returns='Año de la clase'
   descriptions='Devuelve al año de la clase'
   

   def DarAnio(self):
      # Aqui inicia mi método
      return self.anio


   method='Cambiar fecha'
   params='Nueva Fecha'
   returns='Ninguno'
   descriptions='Este metodo permite cambiar la fecha por una nueva'


   def CambiarFecha(self, nuevaFecha):
      #aqui empieza mi metodo
      self.fecha = nuevaFecha 


   method='DarFecha'
   params='Ninguno'
   returns='Fecha Actual'
   descriptions='Dar la fecha cambiada'
   
   
   def DarFecha(self):
      # Aqui inicia mi método
      return self.dia+'/'+self.mes+'/'+self.anio
    

        