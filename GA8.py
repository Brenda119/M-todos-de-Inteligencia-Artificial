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
    decima=[]
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
        print("d",i+1,"=",decima[i])
    return decima
#-----------------------------------------------------------------------------------------
def x(decima):
    X=[]
    x1=0.0
    for i in range(0,p):
        dec=decima[i]
        x1=a+(dec*((b-a)/(2**n-1)))
        X.append(x1)
        
    print('')
    print("***************************Valores de X***************************")
    for i in range(0,p):
        print("x",i+1,"=",X[i])  
    return X
#-----------------------------------------------------------------------------------------   
def fitness(X):
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
def ruleta(funcion):
    suma=0.0
    R=[]
    rul=[]
    s=0.0
    i=0
    ruleta1=0
    for i in range(0,p):
        suma+=funcion[i]
    R.append(0)
    for i in range(0,p):
        if funcion[i]>0:
            rul.append(funcion[i]/suma)
            s=s+(funcion[i]/suma)
        else:
            rul.append(0)
        R.append(s)
        
    '''print('')
    print("***************************Valores aleatorios***************************")'''
    ran=rd.uniform(0,1)
    for i in range(0,len(R)):
        if ran>R[i] and ran<R[i+1]:
            ruleta1=i
    
    return ruleta1
#-----------------------------------------------------------------------------------------
def torneo(funcion):
    torne=0
    tor=[]
       
    for j in range(0,2):
        tor.append(rd.randint(0, p-1))
    if funcion[tor[0]] > funcion[tor[1]]: #---------------
        torne=tor[0]
    else:
        torne=tor[1]
    return torne
#-----------------------------------------------------------------------------------------
def seleccion(Ps,fit,p):
    ps=[]
    rulet_torne=[]
    ps.clear()
    ps=Ps.copy()
    global longitud
    
    r1=int(p-longitud)
    
    for i in range(0,r1):
        #rulet_torne.append(ruleta(fit))
        rulet_torne.append(torneo(fit))
    '''print("ruleta torneo------------------------")
    print(rulet_torne)'''
    
    for i in range(0,len(rulet_torne)):
        ps.append(po[rulet_torne[i]])
    
    '''print('')
    print("***************************Población Ps***************************")
    for i in range(0,len(ps)):
         print("h",i+1,"=",ps[i])'''
    return ps
#-----------------------------------------------------------------------------------------
def cruza(fit,r,p):
    ps=[]
    pb=[]
    p1=[]
    rulet_torne=[]
    global longitud
    
    ps.clear()
    r1=int((r*p)/2)
    r1*=2
    
    for i in range(0,r1):
        #rulet_torne.append(ruleta(fit))
        rulet_torne.append(torneo(fit))
    longitud=len(rulet_torne)
        
    cruce=rd.randint(0,n-1)
    
    ps = [[rd.randint(0, 1) for col in range(n)] for row in range(len(rulet_torne))]
    
    for i in range(0,len(rulet_torne)):
        pb.append(po[rulet_torne[i]])
    
    #if cruce!=0:
    for i in range(0,len(pb),2):
        p1.clear()
        p1.append(pb[i])
        p1.append(pb[i+1])
            
        for k in range(0,n):
            if k<cruce:
                ps[i][k]=p1[0][k]
                ps[i+1][k]=p1[1][k]
            else: 
                ps[i][k]=p1[1][k]
                ps[i+1][k]=p1[0][k]
    '''else:
        for i in range(0,len(pb)):
            ps.append(pb[i])
    print('')
    print("----------Cruza----------")
    for i in range(len(rulet_torne)):
        print(ps[i])'''
    return ps
#-----------------------------------------------------------------------------------------
def mutacion(Ps):
    ps=[]
    ps=Ps.copy()
    in_mut=int(m*p)
    i=0
    while i<in_mut:
        fila=rd.randint(0,len(ps)-1)
        columna=rd.randint(0,n-1)
        
        if ps[fila][columna]==1:
            ps[fila][columna]=0
        else:
            ps[fila][columna]=1
        i+=1 
    '''print("Población con mutacion")
    for i in range(len(ps)):
        print(ps[i])'''
    return ps
#-----------------------------------------------------------------------------------------
def copia(Ps):
    for i in range(0,len(Ps)):
        po.append(Ps[i])
#-----------------------------------------------------------------------------------------
def imp_po():
    print('')
    print("***************************Población nueva***************************")
    for i in range(0,len(po)):
        print("h",i+1,"=",po[i])
#-----------------------------------------------------------------------------------------
def promedio(f):
    suma=0.0
    for i in range(0,p):
        suma+=f[i]
    return suma
#-----------------------------------------------------------------------------------------
def valor_maximo(funcion):
    maximo=0.0
    maximo=max(funcion)
    return maximo
#-----------------------------------------------------------------------------------------   
itera=0
prom=[]
maxi=[]
iteraciones=[]
longitud=0

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
    
    ps_cruza=[]
    ps_seleccion=[]
    ps=[]
    
    dec1=decimal()
    valor_x=x(dec1)
    valor_fit=fitness(valor_x)   

    ps_cruza=cruza(valor_fit,r,p)
    #print(longitud)
    
    ps_seleccion=seleccion(ps_cruza,valor_fit,p)
    
    ps=mutacion(ps_seleccion)
    
    po.clear()
    copia(ps)
    imp_po()    
    
    prom.append(promedio(valor_fit)/p)
    maxi.append(valor_maximo(valor_fit))
    
    
    ps_cruza.clear()
    ps_seleccion.clear()
    ps.clear()
    
    itera+=1
    
#print(maxi)
plt.plot(prom)
plt.plot(maxi)
#plt.plot(mejor)
plt.show()
