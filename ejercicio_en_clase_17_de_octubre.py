# 1. Escribir una función que simule el siguiente experimento: Se tiene una rata en una
# jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma
# probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5
# minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula.
# La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero
# quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
# La función debe devolver el tiempo que tarda la rata en salir de la jaula.

import random
cage=0
time=0

def escap_mouse (cage, time):
    cage= random.randint(1,3)
    
    if cage==1:
        time=time+3
        escap_mouse(cage,time)
        
    elif cage==2:
        time=time+5
        escap_mouse(cage,time)
        
    elif cage==3:
        time=time+7
        print("La rata tardó:", time, "minutos en salir de la jaula")    
        
escap_mouse(cage,time)


#punto 2

#La consigna que para mi es que cree una funcion recursiva que connvierta un numero entero a texto y luego lo devuelve invertido