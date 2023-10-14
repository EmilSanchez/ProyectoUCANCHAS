from os import system;system("cls")
import time
import Excepciones_time
#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'
0               
promociones=[]
promociones_activa=[]

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
            Excepciones_time.excepciones()
            continue    

        if opcion==1:
            crear_promocion()
        elif opcion==2:
            activar_promocion()
        elif opcion==3:
            break
        else:
            Excepciones_time.errores()

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
                    Excepciones_time.errores()
              
            except:
                Excepciones_time.excepciones()
                continue

        promo.append(dia)
        promo.append(numero_porcentaje)
        promociones.append(promo)

        #tiempo(mensaje de proceso,mensaje de finalizar )
        Excepciones_time.tiempo("Creando promoción ...","Promoción creada")
        break


def activar_promocion():

    while True:
        #Verificar existencia de la promocion
        if len(promociones)==0:
            print("No hay ninguna promoción ")
        else:
            contador=1
            #Mostrar promociones
            for i in promociones:
                print(f"{contador}. ---  Día {i[0]} descuento de {i[1]} % ")
                contador+=1
            try:
                #Activar la promo
                opcion = int(input("Ingrese la opcion de descuento a activar --> "))   
                if opcion<=len(promociones) and opcion>=0:
                    promo_activa=promociones[opcion-1]
                    promociones_activa.append(promo_activa)
                    Excepciones_time.tiempo("Activando Promoción ...", "Promoción Activada")
                    break
                else:
                    Excepciones_time.errores()
            except:
                Excepciones_time.excepciones()


<<<<<<< HEAD
=======
menu_promociones()
>>>>>>> 56d1f7df4c2a6fddcf178c87a9a4164ee6accd42
