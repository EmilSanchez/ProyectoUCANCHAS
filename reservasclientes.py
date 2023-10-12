import inicio
import random


reserva=[]

#Llenar las listas
 
dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sábado","Domingo"]

horaabierto=["8:00 a.m. a 9:00 a.m.","9:00 a.m. a 10:00 a.m.","10:00 a.m. a 11:00 a.m. ","11:00 a.m. a 12:00 p.m.","3:00 p.m. a 4:00 p.m.","4:00 p.m. a 5:00 p.m.","5:00 p.m. a 6:00 p.m.","6:00 p.m. a 7:00 p.m.","7:00 p.m. a 8:00 p.m."]

cancha=[[1,2,3,4,5],["001","002","003","004","005"]]

def menudias(promo):
    
    while(True):
        #Menu  dias:
        
        if promo!=0:
            print(f"\n\t{promo[0]}")
        print("\n\tDIAS")
        for i in range(len(dias)):
            print(f"{i+1}.{dias[i]}")
        opc=int(input("Ingrese el dia de reserva -> "))
        dia=dias[opc-1]
        
        if opc==1:
            menuhoras(dia,promo)
            break
        elif opc==2:
            menuhoras(dia,promo)
            break
        elif opc==3:
            menuhoras(dia,promo)
            break
        elif opc==4:
            menuhoras(dia,promo)
            break
        elif opc==5:
            menuhoras(dia,promo)
            break
        elif opc==6:
            menuhoras(dia,promo)
            break
        elif opc==7:
            menuhoras(dia,promo)
            break
        else:
            print("Ha ingresado un día inexistente")


            
def menuhoras(dia,promo):
    #Validar horas
    while True:
        print("\nHoras:")
        for i in range(len(horaabierto)):
            print(f"{i+1}). {horaabierto[i]}")
        horapedida=int(input("Ingrese la hora -> "))
        
        if horapedida <= 9 and horapedida >= 0:
            hora = horaabierto[horapedida-1] 
            canchas(hora,dia,promo)

def canchas(hora,dia,promo):
    reservadia=[]
    #Realizar la reserva
    while True:
        print("\nOPCIONES DE CANCHA")
        for i in cancha[0]:
            print(f"Cancha {i}")
        can=int(input("Ingrese la cancha a apartar -> "))
        if can in cancha[0]:
            nombre=input("Ingrese el nombre->")
            #validar promocion
            if promo!=0  and promo[1]==dia:
                valor=20000-(20000*promo[2])
            else:
                valor=20000

            reservadia.append(nombre)
            reservadia.append(dia)
            reservadia.append(hora)
            reservadia.append(can)
            reservadia.append(valor) #valor de la cancha
            rta=input("Desea apartar arbitro? (si/no) -> ")
            if rta=="si":
                arbitro=random.choice(cancha[1])
                reservadia.append(arbitro)
            elif rta=="no":
                reservadia.append(0)
                
            reserva.append(reservadia)
            print(reserva)


            repetir=input("Desea reservar otro partido? (si/no) -> ").lower()
            if repetir == "si":
                menudias(promo=["15% descuento","Lunes",0.15])        
            elif repetir == "no" :
                inicio.programa()
            break
        else:
            print("Ingrese una cancha correcta")
        break




if __name__=="__main__":
    menudias(promo=["15% descuento","Lunes",0.15])