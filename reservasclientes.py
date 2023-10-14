from os import system;system("cls")
<<<<<<< HEAD
import inicio
import control_arbitros
=======
import random
>>>>>>> 56d1f7df4c2a6fddcf178c87a9a4164ee6accd42

reserva=[]

#Llenar las listas

dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sábado","Domingo"]

horaabierto=["8:00 a.m. a 9:00 a.m.","9:00 a.m. a 10:00 a.m.","10:00 a.m. a 11:00 a.m. ","11:00 a.m. a 12:00 p.m.","3:00 p.m. a 4:00 p.m.","4:00 p.m. a 5:00 p.m.","5:00 p.m. a 6:00 p.m.","6:00 p.m. a 7:00 p.m.","7:00 p.m. a 8:00 p.m."]

cancha=[[1,2,3,4,5],["001","002","003","004","005"]]

def menudias(datos):
    #validar dia

    while(True):
        
        #extrae y elimina promocion
        promo=datos.pop(2)
        if promo!=0:
            print(f"\t{promo[0]}")
        print("=====================================")
        print("\tDIAS")
        for i in range(len(dias)):
            print(f"{i+1}.{dias[i]}")
        print("=======================================")

        opc=int(input("Ingrese el dia de reserva -> "))
        dia=dias[opc-1]
        datos.append(dia)

        if opc==1:
            menuhoras(datos,promo)
        elif opc==2:
            menuhoras(datos,promo)
        elif opc==3:
            menuhoras(datos,promo)
        elif opc==4:
            menuhoras(datos,promo)
        elif opc==5:
            menuhoras(datos,promo)
            break
        elif opc==6:
            menuhoras(datos,promo)
        elif opc==7:
            menuhoras(datos,promo)
        else:
            print("Ha ingresado un día inexistente")


            
def menuhoras(datos,promo):
    #Validar horas
    while True:

        print("\nHoras:")
        for i in range(len(horaabierto)):
            print(f"{i+1}. --- {horaabierto[i]}")
        horapedida=int(input("Ingrese la hora -> "))
        
        if horapedida <= 9 and horapedida >= 0:
            hora = horaabierto[horapedida-1]
            datos.append(hora)
            canchas(datos,promo)
        else:
            print("Ha ingresado una hora incorrecta")

def canchas(datos,promo):

    #Realizar la reserva
    while True:
        print("\nOPCIONES DE CANCHA")
        for i in cancha[0]:
            print(f"Cancha {i}")
        tipo_cancha=int(input("Ingrese la cancha a apartar -> "))

        if tipo_cancha in cancha[0]:
            
            #validar promocion,dato[2]=Dia
            if promo!=0  and promo[1] == datos[2]:
                valor=20000-(20000*promo[2])
            else:
                valor=20000
            
            datos.append(tipo_cancha)
            datos.append(valor)
            
            rta=input("Desea apartar arbitro? (si/no) -> ")
            if rta=="si":
                control_arbitros.arbitros()
            elif rta=="no":
                datos.append(0)

            #Guardar la reserva
            reserva.append(datos)
            print(reserva)

            repetir = input("Desea reservar otro partido? (si/no) -> ").lower()
            if repetir == "si":
                datos.append(promo)
                menudias(datos)        
            elif repetir == "no" :
                inicio.programa()
        else:
            print("Ingrese una cancha correcta")

if __name__=="__main__":
    menudias()