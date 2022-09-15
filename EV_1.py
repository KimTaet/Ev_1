
import datetime

Reservacion={1234:["Ricardo","Cursos",'17/09/2022', "Matutino", "Blanca"]}
Cliente={1:"Ricardo"}
Sala={1:["Blanca",20],2:["Negra",30],3:["Roja",45],4:["Azul",35]}

while True:
    print("")
    print("Menu Principal")
    print("")
    print("1. Registrar la reservación de una sala")
    print("2. Editar el nombre del evento de una reservación ya hecha.")
    print("3. Consultar las reservaciones existentes para una fecha específica.")
    print("4. Registrar a un nuevo cliente ")
    print("5. Registrar una sala ")
    print("6. Salir")
    print("")
    opcion_menu=int(input("¿Que opcion del menu deseas? "))

    if opcion_menu == 1 :
        while True:
            folio=int(input("Ingrese el folio : "))
            if folio in Reservacion.keys():
                print("Ya existe el folio, favor de volver a ingresar")
            else:
                nombre_cliente=input("Ingrese el nombre del cliente : ")
                if (not nombre_cliente in Cliente.values()):
                    print("No esta registrado, favor de registrarse")
                    break
                else:
                    nombre_evento=input("Ingresar el nombre del evento : ")
                    if nombre_evento == "":
                        print("No se puede dejar vacio")
                    else:
                        Fecha_actual=datetime.date.today()
                        fecha_reservacion=input("Ingrese fecha que deseas reservar : ")
                        Fecha=datetime.datetime.strptime(fecha_reservacion, "%d/%m/%Y" ).date()
                        dias_aprox=Fecha.day - Fecha_actual.day
                        if dias_aprox <= 2:
                            print("La reservacion se tiene que hacer con 2 dias de anticipacion")
                        else:
                            turno=input("Ingrese el turno que desea reservar, Matutino | Vespertino | Nocturno: ")
                            print(list(Sala.items()))
                            sala=input("Ingresa que sala desea reservar (El nombre de la sala, ej.Rosa): ")
                            if [fecha_reservacion,turno,sala] in Reservacion.values():
                                print("Fecha ocupada")
                            else:
                                Reservacion.update({folio:[nombre_cliente,nombre_evento,fecha_reservacion,turno,sala]})
                                print(Reservacion.items())
                                print("Empleado agregado")
                                break

    if opcion_menu == 2:
        while True:
            folio=int(input("Ingrese su numero de folio : "))
            cambio=Reservacion.get(folio)
            if cambio== None:
                print("Folio no encontrado")
            else:
                print(f"Datos actuales", {cambio[1]})
                nombre_evento=input("Nuevo nombre del evento reservado : ")
                Reservacion.update({folio:[nombre_evento]})
                print("Nombre del evento modificado")
            break

    if opcion_menu == 3:
        while True:
            fecha_buscar=input("Ingresa la fecha que deseas buscar : ")
            Fecha=datetime.datetime.strptime(fecha_buscar, "%d/%m/%Y" ).date()
            for Fecha in Reservacion.keys():
                for valor in Reservacion.values():
                    print("*" * 73)
                    print("*" * 15, f"Reporte de Reservaciones dia {fecha_buscar}", "*" * 15)
                    print("*" * 73)
                    print ("{:<15} {:<15} {:<15} {:<15}".format('Sala','Cliente','Evento','Turno'))
                    print("*" * 73)
                    print(f"{valor[4]}"," "* 8,f"{valor[0]}"," "*8,f"{valor[1]}"," "*8,f"{valor[3]}")
                    print("*" * 30,"Fin Reporte","*" * 30)
            break

    if opcion_menu == 4:
        while True:
            nombre_cliente=input("Ingrese el nombre del cliente, Dejar vacio para terminar : ")
            if nombre_cliente == "":
                break
            else:
                if Cliente.keys():
                    nueva_llave=(max(list(Cliente.keys()))+1)
                else:
                    nueva_llave = 1
                Cliente[nueva_llave] = (nombre_cliente)
        for clave, dato in list(Cliente.items()):
            print(f"{clave}\t{dato[0]}")

    if opcion_menu == 5:
        while True:
            nombre_sala=input("Ingrese el nombre de la sala, Dejar vacio para terminar : ")
            if nombre_sala == "":
                break
            else:
                cupo_sala=int(input("Ingresar el cupo de la sala : "))
                if Sala.keys():
                    nueva_llave=(max(list(Sala.keys()))+1)
                else:
                    nueva_llave = 1
                Sala[nueva_llave]= (nombre_sala, cupo_sala)
        for clave, datos in list(Sala.items()):
            print(f"{clave}\t{datos[0]}\t{datos[1]}")

    if opcion_menu == 6 :
        print("Gracias, Vuelva pronto")
        break