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
    h = [[rd.randint(0, 1) for col in range(n)] for row in range(p)]
    
    '''print('')
    print("***************************Poblacion inicial****************************")
    for i in range(0,p):
        print("h",i+1,"=",h[i])'''
    
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

    '''print('')
    print("***************************Valores en decimal***************************")
    for i in range(0,p):
        print("d",i+1,"=",decima[i])'''
    return decima
#-----------------------------------------------------------------------------------------
def x(decima):
    X=[]
    x1=0.0
    for i in range(0,p):
        dec=decima[i]
        x1=a+(dec*((b-a)/(2**n-1)))
        X.append(x1)
        
    '''print('')
    print("***************************Valores de X***************************")
    for i in range(0,p):
        print("x",i+1,"=",X[i]) ''' 
    return X
#-----------------------------------------------------------------------------------------   
def fitness(X):
    f=[]
    for i in range(0,p):
        x=X[i]
        f1=(x*math.sin(10*math.pi*x))+1.0
        f.append(f1)
    
    '''print('')
    print("***************************Valores de Fitness***************************")
    for i in range(0,p):
        print("Fitness",i+1,"=",f[i])'''
    return f
#-----------------------------------------------------------------------------------------   
def ruleta(funcion):
    suma=0.0
    R=[]
    rul=[]
    s=0.0
    i=0
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
    
    ran=rd.uniform(0,1)
    for i in range(0,len(R)):
        if ran>=R[i] and ran<R[i+1]:
            return i    
#-----------------------------------------------------------------------------------------
def torneo(funcion):
    torne=0
    tor=[]
       
    for j in range(0,2):
        tor.append(rd.randint(0, p-1))
    if funcion[tor[0]] > funcion[tor[1]]: 
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
    
    for i in range(0,len(rulet_torne)):
        ps.append(po[rulet_torne[i]])
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
#-----------------------------------------------------------------------------------------   
prom=[]
maxi=[]
iteraciones=[]
longitud=0
maximo1=0.0
maximo2=0.0
contador=0
contador1=0
maxim=0.0
m1=0.0

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
iteraciones=int(input("Proporciona el numero maximo de iteraciones que se repetirá el mejor fitness: "))
#----------------------------------------------------------------------------
n=size()
#print('')
#print("***************************Cantidad de bits a usar: ", n)
po=poblacion_i()


while contador1<2:
    
    ps_cruza=[]
    ps_seleccion=[]
    ps=[]
    
    dec1=decimal()
    valor_x=x(dec1)
    valor_fit=fitness(valor_x)   
    
    if(contador > iteraciones-1): #si it llega al numero maximo de iteraciones establecido por el usuario entonces la mutación se vuelve más intensa
        m1=m    
        m*=2
        contador=0
        contador1+=1
        if contador1==2:
            break
    
    if(maxim<max(valor_fit)):
        maxim=max(valor_fit)
        if contador!=0:
            m=m1
        contador=0
        contador1=0
    maxi.append(maxim)
        

    ps_cruza=cruza(valor_fit,r,p)
    #print(longitud)
    
    ps_seleccion=seleccion(ps_cruza,valor_fit,p)
    
    ps=mutacion(ps_seleccion)
    
    po.clear()
    copia(ps)
    #imp_po()    
    
    #prom.append(promedio(valor_fit)/p) 
    
    ps_cruza.clear()
    ps_seleccion.clear()
    ps.clear()
    
    contador+=1
    
#print(maxi)
#plt.plot(prom, label='promedio fitness')
plt.plot(maxi, label='mejor fitness')

plt.legend()

plt.xlabel('Iteraciones')
plt.ylabel('Fitness')
#plt.title('Genetic Algorithms (f(x)=x*sen(10π*x)+1)')
#plt.plot(mejor)
plt.show()
