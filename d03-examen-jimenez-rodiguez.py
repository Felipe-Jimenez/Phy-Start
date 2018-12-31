#jimenez castillo felipe alejandro codigo:215671386
#rodriguez lomeli nadia nayely codigo:215423676
#Examen

import os
import time
from colorama import *
from msvcrt import getch

################################################################################

init(autoreset=True)
empresa=[]
personal={}
nombre={}
precios={}
cantidad={}
compra={}
di=[100]

#################################  FUNCIONES  ##################################

def lectura(a):
    with open(a,"r") as e:
        e=e.readlines(1)
        # e=e.split(" ")
        for name_emp in e:
            if(name_emp[0]=="E"):
                name=name_emp[2:]
                empresa.append(name)
            else:
                pass #LECTURA DEL NOMBRE DE LA EMPRESA

def l_personal(a):
    name=""
    with open(a,"r") as e:
        e=e.readlines()
        for p in e:
            if(p[0]=="P"):
                for i in p[5:]:
                    if(i != "\n"):
                        name+=i
                personal[p[2:4]]=name
                name="" #LECTURA DEL PERSONAL

def l_inventario(a):
    name=""
    with open(a,"r") as inv:
        inv=inv.readlines()
        for a in inv:
            if(a[0]=="A"):
                for i in a[11:]:
                    if(i != "\n"):
                        name+=i
                precios[a[2:4]]=a[5:7]
                cantidad[a[2:4]]=a[8:10]
                nombre[a[2:4]]=name
                name="" #LECTURA DEL INVENTARIO

def m_personal():
    cont=3
    for p in personal.keys():
        cont+=1
        print(Cursor.POS(90,cont)+Back.RED+p," -- ",personal[p]) #MOSTRAR PERSONAL

def m_inventario():
    cont=3
    print(Cursor.POS(85,2)+Back.WHITE+Fore.BLACK+"ID/PRECIO/CANTIDAD/DESCRIPCIÓN")
    for i in nombre.keys():
        cont+=1
        print(Cursor.POS(85,cont)+i)
        print(Cursor.POS(89,cont)+Back.RED+Fore.BLACK+precios[i])
        print(Cursor.POS(94,cont)+Back.BLUE+Fore.BLACK+cantidad[i])
        print(Cursor.POS(99,cont)+Back.MAGENTA+Fore.BLACK+nombre[i]) #MOSTRAR INVENTARIO

def m_compra():
    cont=20
    for i in compra.keys():
        print(Cursor.POS(5,cont)+i, end=" ")
        print(compra[i])
        cont+=1

def tiket(total,pagar):
    cambio=pagar-total
    total=0
    os.system("cls")
    ventana(40,28)
    print(Cursor.POS(13,5)+Back.WHITE+Fore.MAGENTA+empresa[0])
    print(Cursor.POS(10,6)+time.strftime("%c"))
    print(Cursor.POS(13,8)+Back.WHITE+Fore.BLACK+"PRODUCTO/SUBTOLTA")
    cont=9
    for i in compra.keys():
        print(Cursor.POS(13,cont)+i,"  ",compra[i])
        cont+=1
    for p in compra.keys():
        p_p=int(compra[p])
        total+=p_p
    print(Cursor.POS(10,22)+"Total a pagar $",total)
    print(Cursor.POS(10,23)+"Pago con $",pagar)
    print(Cursor.POS(10,24)+"Su cambio son $",cambio)
    print(Cursor.FORWARD(8)+"Gracias por su preferencia")
    input(Cursor.DOWN(2))

def ventana(x,y):
    cont=0
    for i in range(3,x):
        print(Cursor.POS(i,3)+Back.YELLOW+(" "))
        print(Cursor.POS(i,y)+Back.YELLOW+(" "))
        cont+=1

    for i in  range(3,(y+1)):
        print(Cursor.POS(3,i)+Back.YELLOW+(" "))
        print(Cursor.POS((cont+3),i)+Back.YELLOW+(" ")) #VENTANA

def sprites(opc):
    if(opc==1):
        print(Cursor.POS(9,6)+Back.WHITE+Fore.BLACK+"--> EMPRESA <--")
        print(Cursor.POS(9,7)+Back.BLACK+"    PERSONAL    ")
        print(Cursor.POS(9,8)+Back.BLACK+"    INVENTARIO    ")
        print(Cursor.POS(9,9)+Back.BLACK+"    VENTA    ")
        print(Cursor.POS(9,10)+Back.BLACK+"    SALIR    ")
    elif(opc==2):
        print(Cursor.POS(9,6)+Back.BLACK+"    EMPRESA    ")
        print(Cursor.POS(9,7)+Back.WHITE+Fore.BLACK+"--> PERSONAL <--")
        print(Cursor.POS(9,8)+Back.BLACK+"    INVENTARIO    ")
    elif(opc==3):
        print(Cursor.POS(9,7)+Back.BLACK+"    PERSONAL    ")
        print(Cursor.POS(9,8)+Back.WHITE+Fore.BLACK+"--> INVENTARIO <--")
        print(Cursor.POS(9,9)+Back.BLACK+"    VENTA    ")

    elif(opc==4):
        print(Cursor.POS(9,6)+Back.BLACK+"    EMPRESA    ")
        print(Cursor.POS(9,8)+Back.BLACK+"    INVENTARIO    ")
        print(Cursor.POS(9,9)+Back.WHITE+Fore.BLACK+"--> VENTA <--") #SPRITES PRINCIPALES
        print(Cursor.POS(9,10)+Back.BLACK+"    SALIR    ")
    elif(opc==5):
        print(Cursor.POS(9,6)+Back.BLACK+"    EMPRESA    ")
        print(Cursor.POS(9,8)+Back.BLACK+"    INVENTARIO    ")
        print(Cursor.POS(9,9)+Back.BLACK+"    VENTA    ") #SPRITES PRINCIPALES
        print(Cursor.POS(9,10)+Back.WHITE+Fore.BLACK+"--> SALIR <--")

def error():
    a="-"
    print(Cursor.POS(27,24)+Fore.RED+(a*11))
    print(Cursor.POS(30,25)+Back.RED+"ERROR")
    print(Cursor.POS(27,26)+Fore.RED+(a*11))
    time.sleep(1)
    print(Cursor.POS(27,24)+Back.BLACK+Fore.BLACK+a*11)
    print(Cursor.POS(27,25)+Back.BLACK+Fore.BLACK+a*11)
    print(Cursor.POS(27,26)+Back.BLACK+Fore.BLACK+a*11)

#############################  PRINCIPAL  ######################################

def alta(emp):
    ventana(60,13)
    while(True):
        try:
            print(Cursor.POS(23,5)+Back.RED+empresa[0])
            if(len(emp)>0):
                print(Cursor.POS(17,7)+"Ya hay una empresa registrada")
                des=input(Cursor.POS(16,8)+Back.BLACK+"Dar de alta nueva empresa[s/n]")
                if(des=="s"):
                    emp=input(Cursor.POS(26,10)+"Nombre- ")
                    if(len(emp)>0):
                        empresa.pop(0)
                        empresa.append(emp)
                        print(Cursor.POS(22,11)+"Empresa Registrada")
                        time.sleep(1.5)
                        break
                    else:
                        error()
                else:
                    print(Cursor.POS(26,10)+"Gracias")
                    time.sleep(1)
                    break
            else:
                print(Cursor.POS(20,5)+"Nombre de la empresa- ")
                emp=input(Cursor.POS(19,6)+Back.RED)
                if(len(emp)>0):
                    empresa.pop(0)
                    empresa.append(emp)
                    print(Cursor.POS(22,9)+"Empresa Registrada")
                    break
                else:
                    error()
        except:
            error() #ALTA DE LA EMPRESA Y CAMBIO DE NOMBRE

def trabajadores():
    while(True):
        m_personal()
        ventana(50,14)
        try:
            print(Cursor .POS(17,5)+Back.WHITE+Fore.BLACK+"   - PERSONAL -   ")
            opcion=input(Cursor.POS(10,7)+"--Agregar[a]-Editar[e]-Borrar[b]--")
            if(opcion=="a"):
                ID=input(Cursor.POS(21,9)+"ID- ")
                if(ID not in personal):
                    nombre=input(Cursor.POS(21,10)+"Nombre- ")
                    personal[ID]=nombre
                else:
                    print(Cursor.POS(18,11)+"ID ya registrada")
                    time.sleep(1)
            elif(opcion=="e"):
                ID=input(Cursor.POS(21,9)+"ID- ")
                if(ID in personal):
                    nombre=input(Cursor.POS(21,10)+"Nombre- ")
                    personal[ID]=nombre
                else:
                    print(Cursor.POS(18,11)+"ID no registrada")
                    time.sleep(1)
            elif(opcion=="b"):
                ID=input(Cursor.POS(21,9)+"ID- ")
                if(ID in personal):
                    del personal[ID]
                else:
                    print(Cursor.POS(18,11)+"ID no registrada")
            else:
                print(Cursor.POS(18,11)+"   -Gracias-   ")
                time.sleep(1)
                break
            os.system("cls")
        except:
            error() #PERSONAL Y EDICIÓN

def inventario():
    os.system("cls")
    while(True):
        try:
            m_inventario()
            ventana(50,15)
            print(Cursor.POS(21,5)+Back.WHITE+Fore.BLACK+"  -VENTA-  ")
            print(Cursor.POS(13,7)+"Agragar-Eliminar-Finalizar")
            des=input(Cursor.POS(21,8))
            if(des=="a" or des=="A"):
                id=input(Cursor.POS(13,9)+"Id del producto ")
                if(id not in nombre.keys()):
                    pro=str(input(Cursor.POS(13,10)+"Nombre del producto "))
                    can=int(input(Cursor.POS(13,11)+"Cantidad de productos "))
                    pre=int(input(Cursor.POS(13,12)+"Precio del producto "))
                    if(can<=100 and pre<=200):
                        nombre[id]=pro
                        precios[id]=str(pre)
                        cantidad[id]=str(can)
                        time.sleep(1)
                    else:
                        error()
                        os.system("cls")
                else:
                    print(Cursor.POS(15,11)+"Id ya registrada")
                    time.sleep(1)
            elif(des=="e" or des=="E"):
                id=input(Cursor.POS(13,9)+"Id del pruducto ")
                if(id in nombre.keys()):
                    del nombre[id]
                    del cantidad[id]
                    del precios[id]
                    time.sleep(0.5)
                    os.system("cls")
                else:
                    print(Cursor.POS(15,11)+"Id no encontrada")
                    time.sleep(1)
            else:
                print(Cursor.POS(22,10)+Back.WHITE+Fore.BLACK+"Gracias")
                time.sleep(1)
                break
            os.system("cls")
        except:
            error() #INVENTARIIO Y EDICIÓN

def venta():
    x=[1]
    while(True):
        try:
            din=di[0]
            if(len(x)>1):
                break
            os.system("cls")
            ventana(30,10)
            if(di[0]==0):
                print(Cursor.POS(11,5)+"Dinero base")
                din=int(input(Cursor.POS(15,6)))
                di.append(din)
                di.pop(0)
                continue
            if(din>0):
                m_personal()
                id_us=input(Cursor.POS(9,7)+"Id del usuario")
                if(id_us in personal.keys()):
                    us=id_us+" "+personal[id_us]
                    while(True):
                        os.system("cls")
                        ventana(60,15)
                        m_inventario()
                        m_compra()
                        print(Cursor.POS(22,5)+Back.WHITE+Fore.BLACK+empresa[0])
                        print(Cursor.POS(15,7)+"Agregar[a]-Borrar[b]-Finalizar[f]")
                        acc=input(Cursor.POS(27,8))
                        if(acc=="a" or acc=="A"):
                            id_p=str(input("id del producto "))
                            if(id_p in nombre.keys()):
                                can_p=int(cantidad[id_p])
                                pre_p=int(precios[id_p])
                                nom_p=str(nombre[id_p])
                                comp_cantidad=int(input("Cantidad "))
                                if(can_p>=comp_cantidad):
                                    time.sleep(.5)
                                    compra[nom_p]=(comp_cantidad*pre_p)
                                    cantidad[id_p]=str((can_p-comp_cantidad))
                                    os.system("cls")
                                else:
                                    print("No hay suficientes productos")

                        elif(acc=="b" or acc=="B"):
                            id_p=str(input("Nombre del producto "))
                            if(id_p in compra.keys()):
                                del compra[id_p]
                                print("Producto elimiando")
                                time.sleep(.5)
                        elif(acc=="f" or acc=="F"):
                            total=0
                            for p in compra.keys():
                                p_p=int(compra[p])
                                total+=p_p
                            os.system("cls")
                            ventana(30,15)
                            print(Cursor.POS(8,5)+"Total a pagar $",total)
                            pagar=int(input(Cursor.POS(10,6)+"Dinero "))
                            if(pagar>=total):
                                tiket(total,pagar)
                                x.append(1)
                                din+=total
                                di.pop(0)
                                di.append(din)
                                break
                            else:
                                print("Monto incorrecto")
                        else:
                            error()
                else:
                    error()
            else:
                error()
            os.system("cls")
        except Exception as e:
            error() #VENTA DE PRODUCTOS

def salir():
    data=open("d03-examen-jimenez-rodriguez.txt","w")
    for i in empresa:
        data.write("E"+" "+i+"\n")
    for i in personal.keys():
        data.write("U"+" "+i+" "+personal[i]+"\n")
    for i in nombre.keys():
        data.write("P"+" "+i+" "+precios[i]+" "+cantidad[i]+" "+nombre[i]+"\n")
    data.close()

################################# MENÚ #########################################

def menu():
    lectura("d03-examen-jimenez-rodriguez.txt")
    l_personal("d03-examen-jimenez-rodriguez.txt")
    l_inventario("d03-examen-jimenez-rodriguez.txt")
    while(True):
        os.system("cls")
        print(Cursor.POS(3,27)+"jiménez castillo felipe alejandro")
        print(Cursor.POS(3,28)+"rodriguez lomeli nadia nayely")
        print(Cursor.POS(3,29))
        ventana(30,12)
        print(Cursor.POS(5,14)+Fore.BLACK+Back.WHITE+time.strftime("%c"))
        opc=1
        sprites(1)
        while(True):
            key=ord(getch())
            if(key==80 and opc==1):
                opc+=1
                sprites(opc)
            elif(key==80 and opc==2):
                opc+=1
                sprites(opc)
            elif(key==80 and opc==3):
                opc+=1
                sprites(opc)
            elif(key==80 and opc==4):
                opc+=1
                sprites(opc)
            elif(key==72 and opc==5):
                opc-=1
                sprites(opc)
            elif(key==72 and opc==4):
                opc-=1
                sprites(opc)
            elif(key==72 and opc==3):
                opc-=1
                sprites(opc)
            elif(key==72 and opc==2):
                opc-=1
                sprites(opc)
            elif(key==13):
                break
        if(opc==1):
            os.system("cls")
            alta(empresa[0])
            opc=1
        elif(opc==2):
            os.system("cls")
            trabajadores()
            opc=1
        elif(opc==3):
            inventario()
            opc=1
        elif(opc==4):
            venta()
            opc=1
        elif(opc==5):
            salir()
            break

menu()
