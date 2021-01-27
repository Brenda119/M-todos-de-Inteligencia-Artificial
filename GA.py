# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:53:14 2021

@author: Brenda Pedraza Melendez
"""
import math
import random as rd
#-----------------------------------------------------------------------------------------
def size():
    y=b-a
    partition=y*10**n
    n1 = math.log(partition+1, 2)
    n2=int(n1)
    n3=n1-n2
    if n3>=0.5:
        n1=n2+1
    else:
        n1=n2
    return n1
#-----------------------------------------------------------------------------------------
def poblacion_i():
    h=[]
    i=0
    h = [[rd.randint(0, 1) for col in range(n)] for row in range(p)]
    
    print('')
    print("***************************La poblacion inicial****************************")
    for i in range(0,p):
        print("h",i+1,"=",h[i])
    
    return h
#-----------------------------------------------------------------------------------------
def decimal ():
    en=0
    lista1=[]
    for i in range(0,p):
        n1=n-1
        m=0
        for j in range(0,n):
            en=po[i][j]
            m=m+en*2**n1
            n1-=1
        lista1.append(m)

    print('')
    print("***************************Valores en decimal***************************")
    for i in range(0,p):
        print(lista1[i])
    return lista1
#-----------------------------------------------------------------------------------------
def x():
    x1=0.0
    lista1=[]
    
    for i in range(0,p):
        m=d[i]
        x1=a+(m*((b-a)/(2**n-1)))
        lista1.append(x1)
        
    print('')
    print("***************************Valores de X***************************")
    for i in range(0,p):
        print("x",i+1,"=",lista1[i])   
    return lista1
#-----------------------------------------------------------------------------------------   
def fitness():
    f=[]
    for i in range(0,p):
        x=X[i]
        f1=(x*math.sin(10*math.pi*x))+1.0
        f.append(f1)
    
    print('')
    print("***************************Valores de Fitness***************************")
    for i in range(0,p):
        print("Fitness",i+1,"=",f[i])
    return f
#-----------------------------------------------------------------------------------------   
def ruleta():
    suma=0.0
    R=[]
    rul=[]
    rulet=[]
    s=0.0
    j=0
    i=0
    #Suma de todos los fitness
    for i in range(0,p):
        suma=suma+f[i]
    
    i=0
    R.append(0)
    for i in range(0,p):
        valor=0.0
        if f[i]>0:
            valor=f[i]/suma
            rul.append(valor)
            s=s+valor
            R.append(s)
    
    r1=(1-r)*p
    
    i=0
    while j<r1:
        ran=rd.uniform(0,1)
        for i in range(0,p+1):
            if ran>R[i] and ran<R[i+1]:
                rulet.append(i)
        j=j+1 
        print()
        print(ran)
    
    print('')
    print(rul)
    print(R)
    print(rulet)
    
    return rulet
#-----------------------------------------------------------------------------------------   
n=int(input("Proporciona el valor de la presición: "))
print('')
print("Ingresar los valores del intervalo")
a=int(input("Valor del primer punto: "))
b=int(input("Valor del segundo punto: "))
n=size()

print('')
print("***************************Cantidad de bits a usar:", n)
p=int(input("El tamaño de la población será de: "))
po=poblacion_i()
d=decimal()
X=x()
f=fitness()

print('')
print("Proporciona el valor de la población que será reemplazada por el cruce (en número decimal)")
r=float(input("r: "))
ruleta()
#Si un numero es negativo se "convierte a 0"
