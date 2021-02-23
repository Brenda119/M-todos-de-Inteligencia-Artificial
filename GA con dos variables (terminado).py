# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:53:14 2021
@author: Brenda Pedraza Melendez
"""
import math
import random as rd
from matplotlib import pyplot as plt

#-----------------------------------------------------------------------------------------
def size(a,b,n):
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
def poblacion_i(n,p):
    h=[]
    h = [[rd.randint(0, 1) for col in range(n)] for row in range(p)]
    
    return h
#-----------------------------------------------------------------------------------------
def copiar_valores(inter1, inter2, p, po):
    
    var = [[rd.randint(0, 1) for col in range(inter2-inter1)] for row in range(p)]
    
    for i in range(0,p):
        k=0
        for j in range(inter1, inter2):
            var[i][k]=po[i][j]
            k+=1
    
    '''for i in range(0,p):
        print(var[i])'''
    
    return var
#-----------------------------------------------------------------------------------------
def decimal (po,n):
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

    '''for i in range(0,p):
        print("d",i+1,"=",decima[i])'''
    return decima
#-----------------------------------------------------------------------------------------
def x(decima,a,b,n):
    X=[]
    x1=0.0
    for i in range(0,p):
        x1=a+(decima[i]*((b-a)/((2**n)-1)))
        X.append(x1)
        
    '''for i in range(0,p):
        print("x",i+1,"=",X[i])''' 
    return X
#-----------------------------------------------------------------------------------------   
def fitness(X, Y):
    f=[]
    k=9
    for i in range(0,p):
        x=X[i]
        y=Y[i]
        f1=(21.5+(x*math.sin(4*math.pi*x))+(y*math.sin(20*math.pi*y)))
        #f1=((((1-x)**2)*math.exp(-x**2-(y+1)**2))-((x-x**3-y**3)*math.exp(-x**2-y**2)))
        #f1=(16*x*(1-x)*y*(1-y)*math.sin(k*math.pi*x)*math.sin(k*math.pi*y))**2
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
    
    '''print("Población con seleccion")
    for i in range(0,p):
        print(ps[i])'''
    return ps
#-----------------------------------------------------------------------------------------
def cruza(fit,r,p,n):
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
    
    '''print("Población con cruza")
    print(len(ps))
    for i in range(0,r1):
        print(ps[i])'''
    return ps
#-----------------------------------------------------------------------------------------
def mutacion(Ps,n):
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
    po=[]
    for i in range(0,len(Ps)):
        po.append(Ps[i])
    return po
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
itera=0
prom=[]
maxi=[]
maxi1=-100000000000 #variable
longitud=0
contador=0
maximo=[]
m1=0.0
i_encontrado=0
conta=0
ps_cruza=[]
ps_seleccion=[]
ps=[]
X=[]
Y=[]


#---------------Valores para X--------------------------------
print("A continuación proporcionará los valores para X")
n=int(input("Proporciona el valor de la presición: "))
a=float(input("Valor del primer punto: "))
b=float(input("Valor del segundo punto: "))
print('')

#---------------Valores para Y--------------------------------
print("--------------------------------------------------")
print("A continuación proporcionará los valores para Y")
n1=int(input("Proporciona el valor de la presición: "))
a1=float(input("Valor del primer punto: "))
b1=float(input("Valor del segundo punto: "))
print('')

#---------------Tamaño de la población-------------------------
print("--------------------------------------------------")
p=int(input("El tamaño de la población será de: "))
print('')

#---------------Valores para cruza, mutación e iteraciones-------------------------
print("Proporciona el valor de la población que será reemplazada por cruza (en decimal)")
r=float(input("r: "))
print('')
print("Proporciona la tasa de mutacion que habrá en la población")
m=float(input("m: "))
print('')
it=int(input("Proporciona el numero maximo de iteraciones que se repetirá el mejor fitness: "))
#----------------------------------------------------------------------------
n=size(a,b,n) #Tamaño de X
n1=size(a1,b1,n1) #Tamaño de Y

po=poblacion_i((n+n1),p)

m1=m
#en qué x se entontró 
while contador<2:
    while itera<it:
        
        X=copiar_valores(0,n,p,po) #Valores que le tocan a X de la poblacion
        Y=copiar_valores(n,(n+n1),p,po) #Valores que le tocan a Y de la poblacion
        
        dec_x=decimal(X,n)
        x_x=x(dec_x,a,b,n)
    
        dec_y=decimal(Y,n1)
        x_y=x(dec_y,a1,b1,n1)
         
        valor_fit=fitness(x_x, x_y)                     
        
        ps_cruza=cruza(valor_fit,r,p,(n+n1))
        #print(longitud)
            
        ps_seleccion=seleccion(ps_cruza,valor_fit,p)
            
        ps=mutacion(ps_seleccion,(n+n1))
            
        prom.append(promedio(valor_fit)/p)
        
        po.clear() 
        po=copia(ps)
        #-----------------------------------------------------
        if maxi1<max(valor_fit):
            maxi1=max(valor_fit)
            i_encontrado=conta
            itera=0
            contador=0
            m=m1
        else:
            itera+=1
        maximo.append(maxi1)
        #-----------------------------------------------------
        X.clear()
        Y.clear()
        ps_cruza.clear()
        ps_seleccion.clear()
        ps.clear()
        conta+=1
        
    m*=2
    itera=0
    contador+=1
        
#print(maxi)
print('El mejor fitness fue: ', maxi1, 'en la iteración: ',i_encontrado)
plt.plot(prom)
plt.plot(maximo)
#plt.plot(maximo, label='criterio de paro')

plt.legend()

plt.xlabel('Iteraciones')
plt.ylabel('Fitness')
#plt.title('Genetic Algorithms (f(x)=x*sen(10π*x)+1)')
plt.show()
