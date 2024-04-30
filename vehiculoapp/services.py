from vehiculoapp.models import Chofer, Vehiculo, RegistroContabilidad

def crear_vehiculo(patente, marca, modelo, year): 
    vehiculo = Vehiculo(patente=patente, marca=marca, modelo=modelo, year=year) 
    vehiculo.save() 
    return vehiculo

def crear_chofer()