# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:29:29 2021

@author: brenda
"""
import math
import random as rd
from matplotlib import pyplot as plt

#--------------------------------------------------------------------
def poblacion_i(a,b,mu):
    h=[]
    h1=[1,2,3,4,5,6,7,8,9]
    
    h = [[rd.randint(a,b) for col in range(mu)] for row in range(mu)]
    
    for i in range(0,mu):
        h2=h1[:]
        #print(i)
        for j in range(0,mu):
            #n_ran=rd.choice(h2)
            h[i][j]=rd.choice(h2)
            h2.remove( h[i][j])
    return h
#--------------------------------------------------------------------
def fitness(X):
    f=[]
    f1=[]
    f2=[]
    f3=[]
    f4=[]
    n_repetidos_columnas=[]
    n_repetidos_cuadros=[]
    suma_columnas=0
    suma_cuadros=0
    
    global rep_columnas
    
    #--------------------Verificar números repetidos en columnas--------------------
    for i in range(0,len(X)):
        p=0
        f.clear()
        f1.clear()
        f2.clear()
        for j in range(0,len(X)):
            f.append(X[p][i])
            p+=1
        '''print('')
        print(f)'''
        f1=f[:]
        for m in range(0,len(f)):
            valor=f[m]
            for n in range(0,len(f)):
                if n != m:
                    valor1=f1[n]
                    if valor == valor1:
                        f1[n]=0
                        f2.append(valor1)
        repetidos=len(f2)
        n_repetidos_columnas.append(repetidos)
        '''print("-----------repetidos-----------")
        print(repetidos)
        print("-----------f1-----------")
        print(f1)
        print("-----------f2-----------")
        print(f2)
        
    print('')
    print("-----------columnas repetidas-----------")
    print(n_repetidos_columnas)
    print('')'''
    
    f.clear()
    f1.clear()
    f2.clear()
    f3.clear()
    f4.clear()
    
    f=X[:]
    num=0
    
    #--------------------Verifica números repetidos en cuadros 3x3--------------------
    for i in range(0,len(X),3):
        f1.clear()
        num=i+3
        for j in range(i,num):
            f1.append(X[j])
            
        '''print('')
        print("--------------F1--------------")
        print(f1)'''
        
        for m in range(0,3):
            if(m==0):
                n=0
                o=3
            else:
                n+=3
                o+=3
            for k in range(0, 3):
                if(len(f2)==9):
                    f2.clear()
                for l in range(n, o):
                    f2.append(f1[k][l])
            '''print('')
            print("--------------F2--------------")
            print(f2)'''
            f3=f2[:]
            
            f4.clear()
            for p in range(0,len(f2)):
                valor=f2[p]
                for q in range(0,len(f2)):
                    if p != q:
                        valor1=f3[q]
                        if valor == valor1:
                            f3[q]=0
                            f4.append(valor1)
            repetidos=len(f4)
            n_repetidos_cuadros.append(repetidos)
            '''print(f2)
            print(f3)
            print(f4)
            print(repetidos)
        
        print('')'''
    
    '''print('')
    print("Números repetidos por columna")
    print(n_repetidos_columnas)
    print("Números repetidos por cuadros 3x3")
    print(n_repetidos_cuadros)'''
    
    for i in range(0, len(n_repetidos_columnas)):
        suma_columnas+=n_repetidos_columnas[i]
        suma_cuadros+=n_repetidos_cuadros[i]
    '''print(suma_columnas)
    print(suma_cuadros)'''
    
    numero_repeticiones=suma_columnas+suma_cuadros 
    
    return numero_repeticiones
#--------------------------------------------------------------------
def mutacion(lista,b):
    mut=lista[:]
    posicion_fila1=rd.randint(0,b-1)
    print("Filas")
    print(posicion_fila1)
    posicion_columna1=rd.randint(0,b-1)
    posicion_columna2=rd.randint(0,b-1)
    print("Columnas")
    print(posicion_columna1,posicion_columna2)
    
    num1=mut[posicion_fila1][posicion_columna1]
    num2=mut[posicion_fila1][posicion_columna2]
    
    mut[posicion_fila1][posicion_columna1]=num2
    mut[posicion_fila1][posicion_columna2]=num1
    
    return mut
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------

X=[]
F=[]
mut=[]
rep_columnas=[]

a=1 
b=9
mu=b
X=poblacion_i(a,b,mu)
for i in range (0,len(X)):
    print(X[i])
n_repeticiones=fitness(X)
#print(n_repeticiones)
print("---------------Mutación---------------")
mut=mutacion(X,b)
for i in range(0,len(mut)):
    print(mut[i])
