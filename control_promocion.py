from os import system;system("cls")
import time
#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'
                    
promociones=[]

def menu_promociones():
    while True:
        print("=" * 44)
        print("|          CONTROL DE PROMOCIONES          |")
        print("=" * 44)
        print("|    1.  --   CREAR DESCUENTO %            |")
        print("|    2.  --   ACTIVAR DESCUENTO %          |")
        print("|    3.  --   SALIR                        |")

        print("=" * 44);print("")
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
            crear_promocion()
            break
        elif opcion==2:
            activar_promocion()
        else:
            print(RED,"Esa opción no existe, ingrese una valida")
            print(WHITE,"")
            input("Presione Enter para intentarlo nuevamente --> ")
            system("cls")

def crear_promocion():

    #creando promocion
    while True:
        dia=input("Ingrese el día de la promoción --> ")
        while True:
            try:
                numero_porcentaje=int(input(f"Ingrese el el numero de decuento % para el día {dia} --> "))
                break
            except:
                print(RED,"")
                print("UPS! DEBE INGRESAR UN ENTERO :)...")
                print(WHITE,"")
                input("Presione Enter .. --> ")
                system("cls")
                print(f"Dia de promoción: {dia}")
                continue

        promociones.append(dia)
        porcentaje=numero_porcentaje/100
        promociones.append(porcentaje)

        for i in range(2):
            system("cls")
            print("Creando promoción...")
            time.sleep(1)
            
        print("Promoción creada")
        break
        #Tiempo de crear

def activar_promocion():
    pass
    
menu_promociones()