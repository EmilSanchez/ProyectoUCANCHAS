from os import system
system("cls")
import administrador
import responsable
import Excepciones_time
                    
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
            Excepciones_time.excepciones()
            continue    

        if opcion==1:
            administrador.validar_admin()
        elif opcion==2:
            responsable.validar_respon()
        elif opcion==3:
            exit()
        else:
            Excepciones_time.errores()


programa()