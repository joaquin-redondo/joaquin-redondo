def most(a,b):
     if(a>b):
         return a
     else:
        return b

def least(a,b):
     if (a<b) :
         return a
     else:
        return b
    
x= int(input("un numero: "))
y= int(input("otro numero: "))
print(most(x-3, least(x+2, y-5)))

#el problema del codigo era que al pasar como parametro como a y b hay que trabajar en los subprogramas con esos dos, no con x e y porque sino te estaria retornando lo que vale y o x no lo que le cambiamos en el subprograma.

def adder(a,b):
    number=(a + b)
    return number

number1= int(input("ingrese un numero: "))
number2= int(input("ingrese el otro numero: "))

print(adder(number1, number2))