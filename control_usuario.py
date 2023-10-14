from os import system;system("cls")
import time
#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'
#AGREGAR,ELIMINAR,ACTUALIZAR,ACTIVAR Y DESACTIVAR UN RESPONSABLE

users_responsables=[["10565862642","Daniel Ortiz","22"]]

def iniciocont_usuario():
    while True: 
        system("cls")
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
            print(RED,"")
            print("UPS! DEBES INGRESAR UN ENTERO POSITIVO :)...")
            print(WHITE,"")
            input("Presione Enter.. --> ")
            system("cls")
            continue    

        if opcion==1:
            agregarrespon()
        elif opcion==2:
            eliminarrespon()
        elif opcion==3:
            actualizarrespon()
        elif opcion==4:
            pass
        elif opcion==5:
            pass
        elif opcion==6:
            break

def agregarrespon():

    nuevo_repon=[]

    print("\n            AGREGAR RESPONSABLE           ")
    nombre=input("\nIngrese el nombre y apellido del responsable a agregar --> ").capitalize()
    cc=input("Ingrese la cédula del responsable --> ")
    password=input(f"Ingrese la contraseña de para el registro de cuenta del responsable -->")
    nuevo_repon.append(cc)
    nuevo_repon.append(nombre)
    nuevo_repon.append(password)
    users_responsables.append(nuevo_repon)

    for i in range(2):
        system("cls")
        print("Agregando responsable...")
        time.sleep(1)
    
    system("cls")
    print("Responsable registrado")
    input("Presione Enter .. --> ")

def eliminarrespon():
    while True:
        contador=1
        print("\n            ELIMINAR RESPONSABLE           ")
        for i in users_responsables:
            print(f"{contador}. --   {i[1]}          ")
            contador+=1
        
        try:
            respon = int(input("Ingrese la opcion de responsable --> "))
            if respon<=len(users_responsables) and respon>=0:
                eliminado=users_responsables.pop(respon-1)
                for i in range(2):
                    system("cls")
                    print("Eliminando responsable...")
                    time.sleep(1)
                
                system("cls")
                print(f"Responsable {eliminado[1]} eliminado")
                input("Presione Enter .. --> ")
                break
            else:
                print(RED,"")
                print("DEBES INGRESAR UNA OPCION VALIDA ...")
                print(WHITE,"")
                input("Presione Enter.. --> ")
                system("cls")
                            
        except:
            print(RED,"")
            print("UPS! DEBES INGRESAR UN ENTERO POSITIVO :)...")
            print(WHITE,"")
            input("Presione Enter.. --> ")
            system("cls")
            
def actualizarrespon():
    contador=1
    print("\n            ACTUALIZAR RESPONSABLE           ")
    for i in users_responsables:
        print(f"{contador}. --   {i[1]}          ")
        contador+=1
        try:
            respon = int(input("Ingrese la opcion de responsable --> "))
            if respon<=len(users_responsables) and respon>=0:
                pass
            else:
                print(RED,"")
                print("DEBES INGRESAR UNA OPCION VALIDA ...")
                print(WHITE,"")
                input("Presione Enter.. --> ")
                system("cls")
                            
        except:
            print(RED,"")
            print("UPS! DEBES INGRESAR UN ENTERO POSITIVO :)...")
            print(WHITE,"")
            input("Presione Enter.. --> ")
            system("cls")

iniciocont_usuario()