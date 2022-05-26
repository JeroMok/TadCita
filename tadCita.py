
'''5) Una persona tiene una agenda donde guarda la información de sus citas. De cada cita se conoce:
Actividad por realizar, importancia, fecha y hora de inicio. Se deberá desarrollar una aplicación,
utilizando los TADs que crea necesarios. Se desea tener un menú con los siguientes puntos:
a) Agregar cita
b) Modificar cita
c) Eliminar cita
d) Listado de citas
e) Pasar todas las citas de un día determinado a otro dado
f) Eliminar las citas de un día dado
g) Generar una cola con todas las actividades e importancia de un día específico
'''
# tad simple cita
# El siguiente tad sirve para almacenar en una cita  la actividad (string), el orden e importancia (int)
# la fecha de inicio (datatime) y la hora de finalizacion(datatime)

#OPERACIONES QUE SOPORTA:
 
#def crearCita():
    #crea una instancia de la cita

#def cargarcita():
    #carga los datos de la cita

#def verActividad(cita):
    #retorna la actividad de la cita 
#def verImportancia(cita):
   # retorna la importancia en orden 
#def verHoraInicio (cita):
    #retorna la hora de inicio de la cita
#def verHoraFin(cita):
   #retorna la hora de finalizacion de la cita

#def modActividad(cita):
   #modifica la actividad de la cita
# def modImportancia(cita):
   #modifica la importancia de la cita
#def modHoraInicio(cita):
   #modifica la hora de inicio de la cita
#def modHoraFin(cita):
   #modifica la hora de finalizacion de la cita
#def cambiarCita(unaCita, otraCita):
   #copia los datos de la cita 1 a la cita 2
   #def eliminarCita(cita):
      #elimina la cita

# tadCita = [
   #       actividad: string,
      #    importancia: int,
         # horaInicio: datatime,
         # horaFin: datatime,

  # ]'''

  #representacion interna
# lista con los datos de la cita:
cita = ["",0,"",""]

#OPERACIONES

def crearCita():#crea una instancia de la cita
   cita = ["",0,"",""]
   return cita

def cargarcita(cita,act,imp,ini,fin):#carga los datos de la cita
   cita[1] = act
   cita[2] = imp
   cita[3] = ini
   cita[4] = fin

def verActividad(cita):#retorna la actividad de la cita
   return cita[1]
    
    
def verImportancia(cita): # retorna la importancia en orden 
   return cita[2]
  
def verHoraInicio (cita):#retorna la hora de inicio de la cita
   return cita[3]
    
def verHoraFin(cita): #retorna la hora de finalizacion de la cita
   return cita[4]
  
def modActividad(cita, otraAct): #modifica la actividad de la cita
   cita[1] = otraAct

  
def modImportancia(cita, otraImp): #modifica la importancia de la cita
    cita[2] = otraImp
  
def modHoraInicio(cita,otraHoraIni): #modifica la hora de inicio de la cita
   cita[3] = otraHoraIni
  
def modHoraFin(cita,otraHoraFin):#modifica la hora de finalizacion de la cita
   cita[4] = otraHoraFin
   
def cambiarCita(unaCita,otraCita):#copia los datos de la cita 1 a la cita 2
   unaCita[1] = otraCita[1]# se omite el orden de importancia ya que las citas se puede cambia
   unaCita[3] = otraCita[3]# por ser una mas imortante que la otra
   unaCita[4] = otraCita[4]

   