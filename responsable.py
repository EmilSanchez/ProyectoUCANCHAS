from os import system;system("cls")
from datetime import datetime

#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'

user=0
password=0
def validar_respon():
    print(F"BIENVENIDO  RESPONSABLE")
    while True:
        userv = input("Ingrese el nombre de usuario --> ")
        passv = input("Ingrese la contraseña --> ")
        if userv == user:
            if password == passv:
                menu_responsable()
            else:
                print(RED,"La contraseña es incorrecta...")
                print(WHITE,"")
                input("Presione Enter para intentarlo nuevamente.. --> ")
                system("cls")
                continue                
        else:
            print(RED,"El nombre de usuario es incorrecto...")
            print(WHITE,"")
            input("Presione Enter para intentarlo nuevamente.. --> ")
            system("cls")
            continue

def menu_responsable():
    while True: 
        system("cls")
        print("=" * 44)
        print("|    RESPONSABLE DE CANCHAS DEPORTIVAS SAS |")
        print("=" * 44)
        print("|    1.  --   GESTION DE CLIENTES          |")
        print("|    2.  --   GESTION DE RESERVAS          |")
        print("|    3.  --   GESTION DE ARBITROS          |")
        print("|    4.  --   SALIR                        |")
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
            pass

        elif opcion == 4:
            break        
