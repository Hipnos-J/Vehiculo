from vehiculoapp.models import Chofer, Vehiculo, RegistroContabilidad

def crear_vehiculo(patente, marca, modelo, year, activo): 
    vehiculo = Vehiculo(patente=patente, marca=marca, modelo=modelo, year=year, activo=activo) 
    vehiculo.save() 
    return vehiculo

def crear_chofer(rut, nombre, apellido, activo): 
    chofer = Chofer(rut=rut, nombre=nombre, apellido=apellido, activo=activo) 
    chofer.save() 
    return chofer

def crear_registro_contable(fecha_compra, valor, vehiculo):
    registro = RegistroContabilidad(fecha_compra=fecha_compra, valor=valor, vehiculo=vehiculo)
    registro.save()
    return registro

def deshabilitar_chofer(chofer):
    chofer.active = False
    chofer.save()
    return chofer

def deshabilitar_vehiculo(vehiculo):
    vehiculo.active = False
    vehiculo.save()
    return vehiculo

def habilitar_chofer(chofer):
    chofer.active = True
    chofer.save()
    return chofer

def habilitar_vehiculo(vehiculo):
    vehiculo.active = True
    vehiculo.save()
    return vehiculo

def obtener_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    return vehiculo

def obtener_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    return chofer

def asignar_chofer_a_vehiculo(chofer,vehiculo):
    vehiculo.chofer = chofer
    vehiculo.save()
    chofer.save()

def imprimir_datos_vehiculos(): 
    vehiculos = Vehiculo.objects.all() 
    for v in vehiculos: 
        print(f"Vehiculo:{v.patente}/{v.marca}/{v.modelo}/" + 
              f"{v.year}/activo:{v.activo}") 
        if hasattr(v, "chofer"): 
            print(f"\tChofer[{v.chofer.rut}]:{v.chofer.nombre} " + 
                  f"{v.chofer.apellido}/activo:{v.chofer.activo}") 
        if hasattr(v, "contabilidad"): 
            print(f"\tContabilidad:[{v.contabilidad.id}]:fecha_compra:" + 
                  f"{v.contabilidad.fecha_compra}/valor:{v.contabilidad.valor}")
            
            
