# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:53:14 2021

@author: Brenda Pedraza Melendez
"""
import math
import random as rd
from matplotlib import pyplot as plt
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
    print("***************************Poblacion inicial****************************")
    for i in range(0,p):
        print("h",i+1,"=",h[i])
    
    return h
#-----------------------------------------------------------------------------------------
def decimal ():
    en=0
    for i in range(0,p):
        n1=n-1
        m=0
        for j in range(0,n):
            en=po[i][j]
            m+=en*2**n1
            n1-=1
        decima.append(m)

    print('')
    print("***************************Valores en decimal***************************")
    for i in range(0,p):
        print(decima[i])
#-----------------------------------------------------------------------------------------
def x():
    x1=0.0
    for i in range(0,p):
        dec=decima[i]
        x1=a+(dec*((b-a)/(2**n-1)))
        X.append(x1)
        
    print('')
    print("***************************Valores de X***************************")
    for i in range(0,p):
        print("x",i+1,"=",X[i])   
#-----------------------------------------------------------------------------------------   
def fitness():
    for i in range(0,p):
        x=X[i]
        f1=(x*math.sin(10*math.pi*x))+1.0
        f.append(f1)
    
    print('')
    print("***************************Valores de Fitness***************************")
    for i in range(0,p):
        print("Fitness",i+1,"=",f[i])
#-----------------------------------------------------------------------------------------   
def ruleta(l):
    suma=0.0
    R=[]
    rul=[]
    s=0.0
    j=0
    i=0
    for i in range(0,p):
        suma+=f[i]
    if l==0:
        r1=int((r*p)/2)
        r1*=2
    else:
        #r1=(1-r)*p
        r1=len(po)-len(Ps)

    R.append(0)
    for i in range(0,p):
        #valor=0.0
        if f[i]>0:
            #valor=f[i]/suma
            rul.append(f[i]/suma)
            s=s+(f[i]/suma)
        else:
            rul.append(0)
        R.append(s)
        
    i=0
    '''print('')
    print("***************************Valores aleatorios***************************")'''
    while j<r1:
        ran=rd.uniform(0,1)
        for i in range(0,len(R)):
            if ran>R[i] and ran<R[i+1]:
                rulet.append(i)
        j=j+1 
    
    return suma
#-----------------------------------------------------------------------------------------
def seleccion():
    for i in range(0,len(rulet)):
       Ps.append(po[rulet[i]])
    
    print('')
    print("***************************Población Ps***************************")
    for i in range(0,len(Ps)):
         print("h",i+1,"=",Ps[i])     
#-----------------------------------------------------------------------------------------
def cruza():
    pb=[]
    s0=[]
    s1=[]
    p1=[]
    cruce=rd.randint(0,n-1)

   
    for i in range(0,len(rulet)):
        pb.append(po[rulet[i]])
    
    if cruce!=0:
        for i in range(1,len(pb),2):
            p1.clear()
            s0.clear()
            s1.clear()
            p1.append(pb[i-1])
            p1.append(pb[i])
                  
            for j in range(0,len(p1)):
                for k in range(0,n):
                    if j==0:
                        if k<cruce:
                            s0.append(p1[j][k])
                            s1.append(p1[j+1][k])
                        else: 
                            s0.append(p1[j+1][k])
                            s1.append(p1[j][k])
            Ps.append(s0)
            Ps.append(s1)
    else:
        for i in range(0,len(pb)):
            Ps.append(pb[i])

#-----------------------------------------------------------------------------------------
def mutacion():
    in_mut=int(m*p)
    i=0
    while i<in_mut:
        fila=rd.randint(0,len(Ps)-1)
        columna=rd.randint(0,n-1)
        
        if Ps[fila][columna]==1:
            Ps[fila][columna]=0
        else:
            Ps[fila][columna]=1
        i+=1     
#-----------------------------------------------------------------------------------------
def copia():
    for i in range(0,len(Ps)):
        po.append(Ps[i])
#-----------------------------------------------------------------------------------------
def imp_po():
    print('')
    print("***************************Población nueva***************************")
    for i in range(0,len(po)):
        print("h",i+1,"=",po[i])
#-----------------------------------------------------------------------------------------   
Ps=[]
rulet=[]
decima=[]
X=[]
f=[]
itera=0
prom=[]
repeticion=[]

n=int(input("Proporciona el valor de la presición: "))
print('')
print("Ingresar los valores del intervalo")
a=int(input("Valor del primer punto: "))
b=int(input("Valor del segundo punto: "))
print('')
p=int(input("El tamaño de la población será de: "))
print('')
print("Proporciona el valor de la población que será reemplazada por cruza (en decimal)")
r=float(input("r: "))
print('')
print("Proporciona la tasa de mutacion que habrá en la población")
m=float(input("m: "))
print('')
it=int(input("Proporciona el numero de iteraciones: "))
#----------------------------------------------------------------------------
n=size()
print('')
print("***************************Cantidad de bits a usar: ", n)
po=poblacion_i()

while itera<it:
    rulet.clear()
    decima.clear()
    X.clear()
    f.clear()
    Ps.clear()
    
    decimal()
    x()
    fitness()
    
    su=ruleta(0)
    cruza()
    rulet.clear()
    
    ruleta(1)
    seleccion()
    
    mutacion()
    po.clear()
    copia()
    imp_po()
    
    prom.append(su/p)
    repeticion.append(itera)
    itera+=1

print(prom)
plt.plot(prom)
plt.show()

