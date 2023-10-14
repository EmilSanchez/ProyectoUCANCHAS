from os import system;system("cls")

#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'



def menu_arbitro():
    while True: 
        system("cls")
        print("=" * 49)
        print("|   CONTROL DE USUARIO DE CANCHAS DEPORTIVAS SAS |")
        print("=" * 49)
        print("|    1.  --   REGISTRAR ARBITRO                 |")
        print("|    2.  --   ELIMINAR ARBITRO                  |")
        print("|    3.  --   ACTUALIZAR ARBITRO                |")
        print("|    4.  --   ACTIVAR ARBITRO                   |")
        print("|    5.  --   SALIR                             |")
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
            registrarar_bitro()
        elif opcion==2:

        elif opcion==3:
            actualizar_abitro()
        elif opcion==4:
            activar_arbitro()
        elif opcion==5:
            break
        else:
            print("Ingreso de opcion invalida")
def registrarar_bitro():
    pass

