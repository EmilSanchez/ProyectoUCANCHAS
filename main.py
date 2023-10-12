from os import system
system ("cls")

RED = '\033[31m'
WHITE = '\033[37m'

import random

reserva=[]

c=0

dias=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
cancha=[[1,2,3,4,5],["001","002","003","004","005"]]
horaabierto=["8:00 a.m.","9:00 a.m.","10:00 a.m.","11:00 a.m.","3:00 p.m.","4:00 p.m.","5:00 p.m.","6:00 p.m.","7:00 p.m."]

todos=[["Didier","55"],["Luisa","55"],["Emil", "15"]]

def cuentas():
    cuenta=[]
    while(True):
        print("")
        print("BIENVENID@S");print("")
        print("1. Administrador")
        print("2. Responsable" )
        print("3. Clientes "); print("")
        opc=int(input("Ingrese una opción para ingreso -> "))
        
        if opc == 1 or opc == 2:
            
            usuario=input("Ingrese el nombre de usuario -> ")
            contraseña=input("Ingrese la contraseña -> ")
            for i in todos:
                if usuario and contraseña in i:
                    print(f"Bienvenido {usuario}")
                    
        elif opc == 3:
            
            rta = input("Tiene cuenta de usuario (s/n)-> ").lower()
            
            if rta == 's':
                usuario=input("Ingrese el nombre de usuario->")
                contraseña=input("Ingrese la contraseña->")
                for i in todos:
                    if usuario and contraseña in i:
                        print(f"Bienvenido {usuario}")
                                   
            elif rta == "n":
                print("REGISTRAR CUENTA")
                nombre=input("Ingrese nombre->")
                identificacion=input("Ingrese cedula->")
                if identificacion in todos[1]:
                    print("Ya tienes cuenta")
                    
                else:
                    usuario=input("registre el nombre de usuario o identificacion->")
                    contraseña=input("Registre la contraseña->")
                    cuenta.append(identificacion)
                    cuenta.append(usuario)
                    cuenta.append(contraseña)
                    todos.append(cuenta)    
                print(todos)
            menudias()
        else:
            print("Ha ingresado un rol invalido")
        break

def menudias():
    while(True):
        print("\n\tDIAS DISPONIBLES "); print("")
        for i in range(len(dias)):
            print(f"{i+1}. {dias[i]}")
        print("")
        opc=int(input("Ingrese el dia de reserva -> "))
        if opc==1:
            menuhoras(opc)
        elif opc==2:
            menuhoras(opc)
        elif opc==3:
            menuhoras(opc)
        elif opc==4:
            menuhoras(opc)
        elif opc==5:
            menuhoras(opc)
        elif opc==6:
            menuhoras(opc)
        elif opc==7:
            menuhoras(opc)
        else:
            print("Ha ingresado un día inexistente")
        system('cls')


def menuhoras(opc):
    while True:
        print("\nHoras:"); print("")
        for i in horaabierto:
            print(i)
        horapedida=int(input("Ingrese la hora -> "))
        if horapedida>=8 and horapedida<=11:
            hora= f"{horapedida}:00 a.m."
            canchas(hora,opc)
        elif horapedida>=3 and horapedida<=7:
            hora=f"{horapedida}:00 p.m."
            canchas(hora,opc)
        else:
            print("Ingresa una hora correcta")

def canchas(hora,opc):
    reservadia=[]
    while True:
        print("\nOPCIONES DE CANCHA")
        for i in cancha[0]:
            print(f"Cancha {i}")
        can=int(input("Ingrese la cancha a apartar -> "))
        if can in cancha[0]:
            nombre=input("Ingrese el nombre->")
            reservadia.append(nombre)
            dia=dias[opc-1]
            reservadia.append(dia)
            reservadia.append(hora)
            reservadia.append(can)
            reservadia.append(50000)#valor de la cancha
            rta=input("Desea apartar arbitro? (Si)/(No) -> ").capitalize()
            if rta=='Si':
                arbitro=random.choice(cancha[1])
                reserva.append(reservadia)
                reservadia.append(arbitro)
                print(reserva)
                
            else:
                reserva.append(reservadia)
                print(reserva)
        else:
            print("Ingrese una cancha correcta")

def menu():
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
            cuentas()
        elif opcion == 2:
            pass
        elif opcion == 3:
            menudias()
            menuhoras()
            canchas()
        elif opcion == 4:
            canchas()
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            print("")
            print("Gracias por visitarnos!"); print("")
            exit()
            
if __name__ == "__main__":
    menu()