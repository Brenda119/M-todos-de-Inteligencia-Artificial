# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:29:29 2021

@author: brend
"""
import math
import random as rd
from matplotlib import pyplot as plt

#--------------------------------------------------------------------
def poblacion_i(lim_i, lim_s, tam_p):
    h=[]
    for i in range(0,tam_p):
        h.append(rd.uniform(lim_i, lim_s))
    
    '''print("\n------------------Población nueva------------------")
    for i in range(0,tam_p):
        print(h[i])'''
        
    return h
#--------------------------------------------------------------------
def fitness(X):
    f=[]
    for i in range(0,len(X)):
        x=X[i]
        f1=(x*math.sin(10*math.pi*x))+1.0
        f.append(f1)
    
    '''print('')
    print("***************************Valores de Fitness***************************")
    for i in range(0,len(X)):
        print("Fitness",i+1,"=",f[i])'''
    return f
#--------------------------------------------------------------------
def numero_normal():
    z=0
    #print("\n------------------Numeros normales------------------")
    for i in range(0,12):
        z+=rd.uniform(0,1)
    x=z-6
    return x
#--------------------------------------------------------------------
def mutacion(X, linf, lsup, desviacion):
    aleatorio=rd.randint(0,mu-1)
    miembro_al=(X[aleatorio]+(numero_normal()*desviacion))    
    if miembro_al>lsup:
        miembro_al=lsup
        
    if miembro_al<linf:
        miembro_al=linf
        
    return miembro_al
#--------------------------------------------------------------------
def cruza(mu, X):
    miembro1=X[rd.randint(0, mu-1)]
    miembro2=X[rd.randint(0, mu-1)]
    miembro=((miembro1+miembro2)/2)
    return miembro
#--------------------------------------------------------------------
def ordenar(X, Fitness, mu):
    Fit=[]
    P_nueva=[]
    Fit=Fitness[:]
    '''print("\n------------------Valores Fit desordenados------------------")
    for i in range(0,len(Fit)):
        print(Fit[i])
     
    #Fit.sort(reverse=True)
    print("\n------------------Valores Fit ordenados------------------")
    for i in range(0,len(Fit)):
        print(Fit[i])'''
    Fit.sort(reverse=True)
    
    for  i in range(0, mu):
        valor_fit=Fit[i]
        for j in range(0, len(Fit)):
            if valor_fit==Fitness[j]:
              P_nueva.append(X[j]) 
              
    '''print("\n------------------Valores nuevos------------------")
    for i in range(0,len(P_nueva)):
        print(P_nueva[i])'''
    return P_nueva
#--------------------------------------------------------------------
maxi=-100000000000
conta=0
contador=0
iteracion=0
desviacion=1
i_encontrado=0

X=[]
F=[]
F1=[]
F2=[]
maximo=[]
P_lambda=[]
ind_totales=[]


print("--------------------------------------------------")
a=float(input("Valor del primer punto: "))
b=float(input("Valor del segundo punto: "))
mu=int(input("El tamaño de la población será de: "))
lam=int(input("Numero de individuos nuevos (lambda): "))
#r=float(input("La fracción de lambda para generar por cruza: "))
m=float(input("La fracción de lambda para generar por mutación: "))
iteraciones=int(input("Proporciona el numero maximo de iteraciones que se repetirá el mejor fitness: "))
X=poblacion_i(a,b,mu)



while contador<2:
    
    while iteracion<iteraciones:
        
        F1=fitness(X)
        members=round(m*lam)
        for i in range(members):
            P_lambda.append(mutacion(X, a, b, desviacion))
        
        members=lam-len(P_lambda)
        for i in range(members):
            P_lambda.append(cruza(mu, X))
            
        '''print("\n------------------Individuos nuevos------------------")
        for i in range(0,len(P_lambda)):
            print(P_lambda[i])'''
        
        F2=fitness(P_lambda)
        
        for i in range(0, mu):
                ind_totales.append(X[i])
                F.append(F1[i])
        
        for i in range(0, lam):
                ind_totales.append(P_lambda[i])
                F.append(F2[i])
        
        '''print("\n------------------Individuos totales------------------")
        for  i in range(0,len(ind_totales)):
            print(ind_totales[i])
        
        print("\n------------------Fitness de los individuos totales------------------")
        for  i in range(0,len(F)):
            print(F[i])'''
            
        X.clear()
        X=ordenar(ind_totales, F, mu)
        '''print("\n------------------Población modificada------------------")
        for i in range(0,mu):
            print(X[i])'''
        F=fitness(X)
        #-----------------------------------------------------
        if maxi<max(F):
            maxi=max(F)
            i_encontrado=conta
            iteracion=0
            contador=0
            desviacion=1
        else:
            iteracion+=1
        maximo.append(maxi)
        #-----------------------------------------------------
        
        F.clear()
        F1.clear()
        F2.clear()
        P_lambda.clear()
        ind_totales.clear()
        
        conta+=1
    desviacion=2
    iteracion=0
    contador+=1
    
print('El mejor fitness fue: ', maxi, 'en la iteración: ',i_encontrado)
print("El maximo de iteraciones fue de: ", conta)

plt.plot(maximo)

plt.xlabel('Iteraciones')
plt.ylabel('Fitness')
plt.show()
