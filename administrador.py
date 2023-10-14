from os import system;system("cls")
import control_usuario
import control_clientes
import control_reservas
import control_arbitros
import control_promocion
import control_reportes
import Excepciones_time

#para la promocion activa
#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'

user = "Didier"
password= "2023"

def validar_admin():
    
    print("\nBIENVENIDO  ADMINISTRADOR"); print("")
    while True:
        userv = input("Ingrese el nombre de usuario --> ")
        passv = input("Ingrese la contraseña --> ")
        if userv == user:
            if password == passv:
                menu_administrador()
                break
            else:
                print(RED,"")
                print("La contraseña es incorrecta...")
                print(WHITE,"")
                input("Presione Enter para intentarlo nuevamente.. --> ")
                system("cls")
                continue                
        else:
            print(RED,"")
            print("El nombre de usuario es incorrecto...")
            print(WHITE,"")
            input("Presione Enter para intentarlo nuevamente.. --> ")
            system("cls")
            continue

def menu_administrador():
    while True: 
        print("=" * 44)
        print("| ADMINISTRACION DE CANCHAS DEPORTIVAS SAS |")
        print("=" * 44)
        print("|    1.  --   CONTROL DE USUARIOS          |")
        print("|    2.  --   CONTROL DE CLIENTES          |")
        print("|    3.  --   CONTROL DE RESERVAS          |")
        print("|    4.  --   CONTROL DE ARBITROS          |")
        print("|    5.  --   CONTROL DE PROMOCIONES       |")
        print("|    6.  --   CONTROL DE REPORTES          |")
        print("|    7.  --   SALIR                        |")
        print("=" * 44); print("")
            
        try:
            opcion = int(input("Ingrese la opcion a ejecutar --> "))         
        except:
            Excepciones_time.excepciones()
            continue    
        
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass 
        elif opcion == 4:
            control_arbitros()
        elif opcion == 5:
            control_promocion.menu_promociones()
        elif opcion == 6:
            pass
        elif opcion == 7:
            print("\nGracias por visitarnos!")
            return 
        else:
            print("\nIngrese una opción valida")
    

validar_admin()