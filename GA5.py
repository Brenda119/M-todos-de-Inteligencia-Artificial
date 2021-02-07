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
def ruleta(l,l_Ps,f):
    suma=0.0
    R=[]
    rul=[]
    s=0.0
    j=0
    i=0
    ruleta1=[]
    for i in range(0,p):
        suma+=f[i]
    if l==0:
        r1=int((r*p)/2)
        r1*=2
    else:
        r1=p-l_Ps
        '''print('')
        print("----------------------------------VAlor de r1")
        print(r1)'''
    R.append(0)
    for i in range(0,p):
        if f[i]>0:
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
                ruleta1.append(i)
        j=j+1 
    
    return ruleta1
#-----------------------------------------------------------------------------------------
def torneo(p,l,l_ps,decima):
    torne=[]
    tor=[]
    
    if l==0:
        r1=int((r*p)/2)
        r1*=2
    else:
        r1=p-l_ps
    print(r1)
    
    for i in range(0,r1):    
        for i in range(0,2):
            tor.append(rd.randint(0, p-1))
        if decima[tor[0]] > decima[tor[1]]: #---------------
            torne.append(tor[0])
        else:
            torne.append(tor[1])
        '''print('')
        print(tor)
        print(decima[tor[0]])
        print(decima[tor[1]])'''
        tor.clear()
    #print(tor1)
        #tor1.clear()
    #print(torne)
    return torne
#-----------------------------------------------------------------------------------------
def seleccion(rulet,Ps):
    ps=[]
    ps=Ps.copy()
    '''print("PS con cruza-------------------")
    print(len(ps))
    for i in range(len(ps)):
        print(ps[i])'''
    for i in range(0,len(rulet)):
        ps.append(po[rulet[i]])
    
    '''print('')
    print("***************************Población Ps***************************")
    for i in range(0,len(ps)):
         print("h",i+1,"=",ps[i]) '''
    return ps
#-----------------------------------------------------------------------------------------
def cruza(rulet):
    ps=[]
    pb=[]
    s0=[]
    s1=[]
    p1=[]
    cruce=rd.randint(0,n-1)
    print ("-------------cruce-------------",'',cruce)
    ps = [[rd.randint(0, 1) for col in range(n)] for row in range(len(rulet))]
    '''print('')
    print("PS con numeros random")
    for i in range(len(rulet)):
        print(Ps[i])'''
    
    for i in range(0,len(rulet)):
        pb.append(po[rulet[i]])
    
    if cruce!=0:
        for i in range(0,len(pb),2):
            p1.clear()
            s0.clear()
            s1.clear()
            p1.append(pb[i])
            p1.append(pb[i+1])
            print('')
            print("-------------P1-------------")
            for j in range(0,len(p1)):
                print(p1[j])
            
            for k in range(0,n):
                if k<cruce:
                    ps[i][k]=p1[0][k]
                    ps[i+1][k]=p1[1][k]
                    #s0.append(p1[0][k])
                    #s1.append(p1[1][k])
                else: 
                    ps[i][k]=p1[1][k]
                    ps[i+1][k]=p1[0][k]
                    #s0.append(p1[1][k])
                    #s1.append(p1[0][k])
            print('')
            print("s0,s1")
            print(s0)
            print(s1)
    else:
        for i in range(0,len(pb)):
            ps.append(pb[i])
    print('')
    print("----------Cruza----------")
    for i in range(len(rulet)):
        print(ps[i])
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
itera=0
prom=[]


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
    dec1=decimal()
    valor_x=x(dec1)
    valor_fit=fitness(valor_x)
    
    ruleta_cruza=ruleta(0,0,valor_fit)
    print("Ruleta de cruza")
    print(ruleta_cruza)
    ps_cruza=cruza(ruleta_cruza)
    
    #print("longitud de ps")
    #print(len(ps_cruza))
    ruleta_seleccion=ruleta(1,len(ps_cruza),valor_fit)
    print("Ruleta de seleccion")
    print(ruleta_seleccion)
    ps_seleccion=seleccion(ruleta_seleccion,ps_cruza)
    
    ps=mutacion(ps_seleccion)
    po.clear()
    copia(ps)
    imp_po()
    
    
    prom.append(promedio(valor_fit)/p)
    ps_cruza.clear()
    ps_seleccion.clear()
    ps.clear()
    dec1.clear()
    valor_x.clear()
    valor_fit.clear()
    itera+=1
#print(prom)
plt.plot(prom)
plt.show()


'''while itera<it:
    dec1=decimal()
    valor_x=x(dec1)
    valor_fit=fitness(valor_x)
    
    torneo_cruza=torneo(p,0,0,dec1)
    ps_cruza=cruza(torneo_cruza)
    
    #print("-----------------longitud de ps cruza-----------------", len(ps_cruza))
    torneo_seleccion=torneo(p,1,len(ps_cruza),dec1)
    ps_seleccion=seleccion(torneo_seleccion,ps_cruza)
    
    ps=mutacion(ps_seleccion)
    po.clear()
    copia(ps)
    imp_po()
    
    
    prom.append(promedio(valor_fit)/p)
    torneo_cruza.clear()
    torneo_seleccion.clear()
    ps.clear()
    dec1.clear()
    valor_x.clear()
    valor_fit.clear()
    itera+=1
#print(prom)
plt.plot(prom)
plt.show()'''
