from colorama import *
init(autoreset=True)

def ventana(x,y):
    cont=0
    for i in range(3,x):
        print(Cursor.POS(i,3)+Back.WHITE+(" "))##largo/ancho
        print(Cursor.POS(i,y)+Back.WHITE+(" "))
        cont+=1

    for i in range(3,(y+1)):
        print(Cursor.POS(3,i)+Back.WHITE+(" "))
        print(Cursor.POS((cont+3),i)+Back.WHITE+(" "))

ventana(70,25)
