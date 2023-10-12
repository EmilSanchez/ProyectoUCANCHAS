from os import system;system("cls")
import inicio
promocion=[["Lunes con 15% de descuento","Lunes",0.15,],["Domingo con 20% de descuento","Domingo",0.2],["Viernes con 10% de descuento","Viernes",0.1]]

RED = '\033[31m'
WHITE = '\033[37m'

def menu_administrador(promo):
    while True:
        while True:
            print("=" * 44)
            print("| ADMINISTRACION DE CANCHAS DEPORTIVAS SAS |"); print("=" * 44)
            print("|    1.  --   GESTION DE USUARIOS          |")
            print("|    2.  --   GESTION DE CLIENTES          |")
            print("|    3.  --   GESTION DE RESERVAS          |")
            print("|    4.  --   GESTION DE ARBITROS          |")
            print("|    5.  --   GESTION DE PROMOCIONES       |")
            print("|    6.  --   GESTION DE REPORTES          |")
            print("|    7.  --   SALIR                        |"); print("=" * 44); print("")
            
            try:
                opcion = int(input("Ingrese la opcion a ejecutar --> "))
                break
                
            except:
                print("")
                print(RED,"UPS! DEBES INGRESAR UN ENTERO POSITIVO :)...")
                print(WHITE,"")
                input("Press Enter.. --> ")
                system ("cls")
                continue
        
        if opcion == 1:
            inicio.cuentas()
        elif opcion == 2:
            pass
        elif opcion == 3:
            inicio.menudias()
            inicio.menuhoras()
            inicio.canchas()
        elif opcion == 4:
            inicio.canchas()
        elif opcion == 5:
            promociones(promo)
        elif opcion == 6:
            pass
        elif opcion == 7:
            print("")
            print("Gracias por visitarnos!"); print("")
            break

def promociones(promo):
    print("1). Activar promocion")
    print("2). Desactivar promociones")
    print("3). Salir")
    
    opc=int(input("Ingrese una opcion->"))
    
    if opc==1:
        for i in range(len(promocion)):
            print(f"{i+1}).{promocion[i][0]}")
        opc=int(input("Ingrese una promocion->"))
        promo=promocion[opc-1]
        print (promo)
        return promo
    elif opc==2:
        if promo!=0:
            promo=0
            return promo
    elif opc == 3:
        print("Regresando al manu principal...")
        
        

