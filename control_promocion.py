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
        elif opcion==2:
            activar_promocion()
        elif opcion==3:
            break
        else:
            print(RED,"Esa opción no existe, ingrese una valida")
            print(WHITE,"")
            input("Presione Enter para intentarlo nuevamente --> ")
            system("cls")

def crear_promocion():
    #creando promocion
    while True:
        promo=[]
        dia=input("Ingrese el día de la promoción --> ")
        while True:
            try:
                print(f"Dia de promoción: {dia}")
                numero_porcentaje=int(input(f"Ingrese el el numero de decuento % para el día {dia} --> "))
                if numero_porcentaje>0:
                    break
                else:
                    print(RED,"")
                    print("UPS! DEBE INGRESAR UN ENTERO :)...")
                    print(WHITE,"")
                    input("Presione Enter .. --> ")                    
            except:
                print(RED,"")
                print("UPS! DEBE INGRESAR UN ENTERO :)...")
                print(WHITE,"")
                input("Presione Enter .. --> ")
                system("cls")

                continue

        promo.append(dia)
        promo.append(numero_porcentaje)
        promociones.append(promo)

        for i in range(2):
            system("cls")
            print("Creando promoción...")
            time.sleep(1)
            
        system("cls")
        print("Promoción creada")
        input("Presione Enter .. --> ")        
        break

        #Tiempo de crear

def activar_promocion():

    while True:
        if len(promociones)==0:
            print("No hay ninguna promoción ")
        else:
            contador=1
            for i in promociones:
                print(f"{contador}. ---  Día {i[0]} descuento de {i[1]} % ")
                contador+=1
            try:
                opcion = int(input("Ingrese el descuento a activar --> "))   
            except:
                print(RED,"")
                print("UPS! DEBES INGRESAR UN ENTERO POSITIVO :)...")
                print(WHITE,"")
                input("Presione Enter.. --> ")
                system("cls")

            if opcion<=len(promociones) and opcion>=0:
                promo_activa=promociones[opcion-1]
                print(promo_activa)
            else:
                print(RED,"")
                print("UPS! DEBES INGRESAR UN ENTERO POSITIVO :)...")
                print(WHITE,"")
                input("Presione Enter.. --> ")
                system("cls")

