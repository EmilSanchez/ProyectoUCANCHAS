from os import system;system("cls")

import administrador
import time
import reservasclientes

#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'


<<<<<<< HEAD
def menu_arbitros():
        print("=" * 44)
        print("|          CONTROL DE ARBITROS             |")
        print("=" * 44)
        print("|    1.  --   ESCOGER ARBITRO              |")
        print("|    2.  --   REGISTRAR ARBITRO            |")
        print("|    3.  --   EDITAR ARBITRO               |")
        print("|    4.  --   ELIMINAR ARBITRO             |")
        print("|    5.  --   SALIR                        |")

        print("=" * 44);print("")
        
def arbitros():
    
    arbitros = ["Arbtro_001", "Arbtro_002"]
    
    while True:
        try:
            menu_arbitros()
            
            opcion = int(input("Ingrese la opcion a ejecutar --> "))  
            
=======

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
>>>>>>> 56d1f7df4c2a6fddcf178c87a9a4164ee6accd42
        except:
            print(RED,"")
            print("UPS! DEBES INGRESAR UN ENTERO POSITIVO :)...")
            print(WHITE,"")
            input("Presione Enter.. --> ")
            system("cls")
<<<<<<< HEAD
            continue
        
        if opcion == 1:
            system('cls')
            numero_arbitros = len(arbitros)
            print(f"Por el momento solo existen {numero_arbitros} arbitros");print("");print("=" * 16)           
            i = 0
            for i in range(len(arbitros)):
                print(f"{i}. --- {arbitros[i]}")
                i+1
            
            print("")
            opcion = int(input("Elija la pocicion de un arbitro --> "))
            system('cls')
            arbitroelegido = arbitros[opcion]
            print(f"Elejiste el --> ({arbitroelegido})");print("")
            arbitroelegido.append(reservasclientes.reserva)
            input(f"Presiona ENTER para regresar al menu ---> ")
            system('cls')
            continue
            
        elif opcion == 2:
            pass

        elif opcion == 3:
            pass
        
        elif opcion == 4:
            pass
        
        elif opcion == 5:
            system('cls')
            print("Regresando al Menu Administrador..")
            time.sleep(2)
            system('cls') 
            administrador.menu_administrador()
    
        
=======
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

>>>>>>> 56d1f7df4c2a6fddcf178c87a9a4164ee6accd42
