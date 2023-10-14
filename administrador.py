from os import system;system("cls")
import control_usuario
import control_clientes
import control_reservas
import control_arbitros
import control_promocion
import control_reportes
import reservasclientes
import time
import inicio
#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'

user = "didier"
password = "2023"

def validar_admin():
    print("BIENVENIDO  ADMINISTRADOR"); print("")
    while True:
        userv = input("Ingrese el nombre de usuario --> ")
        passv = input("Ingrese la contraseña --> ")
        if userv == user:
            if password == passv:
                print("")
                print("Accediendo..")
                time.sleep(2)
                system('cls')                
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
            print(RED,"")
            print("UPS! DEBES INGRESAR UN ENTERO POSITIVO :)...")
            print(WHITE,"")
            input("Presione Enter.. --> ")
            system("cls")
            continue    
        
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            reservasclientes.menudias('0') 
        elif opcion == 4:
            system('cls')
            control_arbitros.arbitros()
        elif opcion == 5:
            control_promocion.menu_promociones()
        elif opcion == 6:
            pass
        elif opcion == 7:
            system('cls')
            print("Regresando al Menu Principal..")
            time.sleep(2)
            system('cls')
            inicio.programa()
        else:
            print("\nIngrese una opción valida")
    

