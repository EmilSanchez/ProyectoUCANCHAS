from os import system
system("cls")
import reservasclientes
import administrador
#todos[[nombre , cedula, cuenta , contraseña]]
todos = [["Didier","10657","didier55","d563"],["Luisa","1065","luisa23","13"]]

def cuentas(rta):#Validar cuentas
    cuenta=[]
    if rta == "no":   
        print("REGISTRAR CUENTA")
        nombre = input("Ingrese nombre-> ").capitalize()
        identificacion = input("Ingrese cedula-> ")
        for i in range(len(todos)):
            a=todos[i][1].count(identificacion)
        if a>0:
            print("Ya tienes cuenta")
            rta="si"
        elif a==0:
            usuario=input("Ref el usuario->")
            #falta validar usuario repetido
            contraseña=input("Registre la contraseña->")
            cuenta.append(nombre)
            cuenta.append(identificacion)
            cuenta.append(usuario)
            cuenta.append(contraseña)
            todos.append(cuenta)#registrar cuenta
                


    if rta=="si":
        while True:
            usuario=input("Ingrese el nombre de usuario-> ")
            contraseña=input("Ingrese la contraseña-> ")
            for i in todos:
                if usuario in i and contraseña in i:
                    return "Bienvenido"         
            print("Usuario o contraseña incorrecta")  


def roles(promo):#validar usuario
    while(True):
        print(""" 
        .======================.
        |        ROLES         |
        |                      |
        |   1.Administrador    |
        |   2.Responsable      |
        |   3.Clientes         |   
        |                      |
        .======================.
        """)
        opc=int(input("Ingrese una opción para ingreso-> "))
        datos=[]
        if opc==1:        
            usuario=cuentas(rta="si")
            promo=administrador.promociones(promo)#funciones del administrador

        elif opc==2:
            cuentas(rta="si")
        elif opc==3:
            rta=input("Tiene cuenta de usuario-> ").lower()
            if rta=="si":
                res=cuentas(rta) 
                print(res)
                reservasclientes.menudias(promo)#reservas clientes
            elif rta=="no":
                cuentas(rta)
                cantidad=len(todos)-1
                datos.append(todos[cantidad][2])#Usuario
                datos.append(todos[cantidad][0])#Nombre cliente
                datos.append(promo)
                reservasclientes.menudias(datos)
        else:
            print("Ha ingresado un rol invalido")
        return promo
    
def programa():
    promo=0
    while (True):
        promocion=promo
        print(""" 
        .======================.
        |     CANCHA NOSE      |
        |                      |
        |   1.Ingresar         |
        |   2.Salir            |
        |                      |
        .======================.
        """)
        try:
            opcion=int(input("Por favor ingrese una opción->"))
            if opcion==1:
                promo=roles(promocion)
            elif opcion==2:
                break
            else:
                print("No se existe esta")
        except:
            print("\nIngrese el numero de la opcion elegida")

if __name__=="__main__":
    programa()