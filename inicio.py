from os import system
system("cls")
import administrador
import responsable

#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'
                    
def programa():
    #validar usuario
    while(True):

        print("=" * 44)
        print("|          CANCHAS DEPORTIVAS SAS          |")
        print("=" * 44)
        print("|    1.  --   ADMINISTRADOR                |")
        print("|    2.  --   RESPONSABLE                  |")
        print("|    3.  --   SALIR                        |")
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

        if opcion==1:
            administrador.validar_admin()
        elif opcion==2:
            responsable.validar_respon()
        elif opcion==3:
            exit()


programa()