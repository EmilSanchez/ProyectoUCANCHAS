from os import system;system("cls")
import Excepciones_time

WHITE = '\033[37m'
#AGREGAR,ELIMINAR,ACTUALIZAR,ACTIVAR Y DESACTIVAR UN RESPONSABLE

users_responsables=[["10565862642","Daniel Ortiz","22"]]
users_activos=[]
users_inactivos=[["10565862642","Daniel Ortiz","22"]]
def iniciocont_usuario():
    while True: 
        print("=" * 49)
        print("|   CONTROL DE USUARIO DE CANCHAS DEPORTIVAS SAS |")
        print("=" * 49)
        print("|    1.  --   AGREGAR RESPONSABLE               |")
        print("|    2.  --   ELIMINAR RESPONSABLE              |")
        print("|    3.  --   ACTUALIZAR RESPONSABLE            |")
        print("|    4.  --   DESACTIVAR RESPONSABLE            |")
        print("|    5.  --   ACTIVAR RESPONSABLE               |")
        print("|    6.  --   SALIR                             |")
        print("=" * 49); print("")
            
        try:
            opcion = int(input("Ingrese la opcion a ejecutar --> "))         
        except:
            Excepciones_time.errores()
            continue    

        if opcion==1:
            agregarrespon()
        elif opcion==2:
            eliminarrespon()
        elif opcion==3:
            actualizarrespon()
        elif opcion==4:
            desactivarrespon()
        elif opcion==5:
            activarrespon()
        elif opcion==6:
            break
        else:
            Excepciones_time.errores()

def agregarrespon():
    nuevo_repon=[]
    print("\n            AGREGAR RESPONSABLE           ")
    nombre=input("\nIngrese el nombre y apellido del responsable a agregar --> ").title()
    cc=input("Ingrese la cédula del responsable --> ")
    password=input(f"Ingrese la contraseña de para el registro de cuenta del responsable -->")
    nuevo_repon.append(cc)
    nuevo_repon.append(nombre)
    nuevo_repon.append(password)
    users_responsables.append(nuevo_repon)
    #Tiempo
    Excepciones_time.tiempo("Registrando responsable...","Responsable registrado")
    users_inactivos.append(nuevo_repon)

def eliminarrespon():
    while True:
        contador=1
        print("\n            ELIMINAR RESPONSABLE           ")
        for i in users_responsables:
            print(f"{contador}. --   {i[1]}          ")
            contador+=1

        try:
            respon_elim = int(input("Ingrese la opcion de responsable --> ")) 
            #respon menor o igual a la cantidad de elementos 
            if respon_elim<=len(users_responsables) and respon_elim>0:
                users_responsables.pop(respon_elim-1)
                Excepciones_time.tiempo("Eliminando responsable ...","Responsable Eliminado")
                break
            else:
                Excepciones_time.errores()
                            
        except:
            Excepciones_time.excepciones()
            
def actualizarrespon():
    while True:
        #Mostrar responsables
        contador=1
        print("\n            ACTUALIZAR RESPONSABLE           ")
        for i in users_responsables:
            print(f"{contador}. --   {i[1]}          ")
            contador+=1

        try:
            #La lista del responsable
            respon = int(input("Ingrese la opcion de responsable --> "))
            #validar la opcion 
            if respon<=len(users_responsables) and respon>0:
                while True:
                    print("1.Identificacion")
                    print("2.Nombre")
                    print("3.Telefono")
                    try:
                        opc=int(input("Ingrese La opcion a actualizar --> "))
                        if opc==1:
                            nueva_cc=input("Ingrese la nueva identificación --> ")

                            #elimina el nuevo elemento
                            users_responsables[respon-1].pop(opc-1)

                            #Agrega nuevo elemento
                            users_responsables[respon-1].insert(opc-1,nueva_cc)
                            Excepciones_time.tiempo("Actualizando ...","Identificación actualizada")
                            break

                        elif opc==2:
                            new_name=input("Ingrese el nombre y apellido nuevo  --> ")
                            users_responsables[respon-1].pop(opc-1)
                            users_responsables[respon-1].insert(opc-1,new_name) 
                            Excepciones_time.tiempo("Actualizando ...","Nombre actualizado")
                            break
                        elif opc==3:
                            nuevo_tel=input("Ingrese el nuevo número de teléfono --> ")
                            users_responsables[respon-1].pop(opc-1)
                            users_responsables[respon-1].insert(opc-1,nuevo_tel)
                            Excepciones_time.tiempo("Actualizando ...","Teléfono actualizado")
                            break
                        else:
                            Excepciones_time.errores()     
                    except:
                        Excepciones_time.excepciones()
            else:
                Excepciones_time.errores()
        except:
            Excepciones_time.excepciones()
            continue
        else:
            break
                                
def activarrespon():
    if len(users_inactivos)<=0:
        print("TODOS LOS RESPONSABLES ESTÁN ACTIVOS")
        input("Presione Enter.. --> ")
    else:
        while True:
            contador=1
            print("\n            ACTIVAR RESPONSABLE           ")
            for i in users_inactivos:
                print(f"{contador}. --   {i[1]}          ")
                contador+=1
            try:
                respon=int(input("Ingrese la opción del responsable a activar --> "))
                if respon<=len(users_inactivos) and respon>0:
                    break
                else:
                    Excepciones_time.errores()
            except:
                Excepciones_time.excepciones()
                continue

        respon_activar=users_inactivos.pop(respon-1)
        users_activos.append(respon_activar)
        Excepciones_time.tiempo("Activando responsable ...","Responsable activado")

def desactivarrespon():
    if len(users_activos)<=0:
        print("TODOS LOS RESPONSABLES ESTÁN INACTIVOS")
        input("Presione Enter.. --> ")
    else:
        while True:
            contador=1
            print("\n           DESACTIVAR RESPONSABLE           ")
            for i in users_activos:
                print(f"{contador}. --   {i[1]}          ")
                contador+=1
            try:
                respon=int(input("Ingrese la opción del responsable a desactivar --> "))
                if respon<=len(users_activos) and respon>0:
                    break
                else:
                    Excepciones_time.errores()
            except:
                Excepciones_time.excepciones()

        #eliminar el respon de activos
        respon_desactivar=users_activos.pop(respon-1)
        #Agragaer el respon a inactivos
        users_activos.append(respon_desactivar)
        Excepciones_time.tiempo("Activando responsable ...","Responsable activado")

