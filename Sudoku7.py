# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:29:29 2021

@author: brenda
"""
import copy as c
import random as rd
import numpy as np
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
            h[i][j]=rd.choice(h2)
            h2.remove( h[i][j])
    return h
#--------------------------------------------------------------------
def fitness(sudoku_or):
    f=[]
    f1=[]
    f2=[]
    f3=[]
    f4=[]
    n_repetidos_columnas=[]
    n_repetidos_cuadros=[]
    suma_columnas=0
    suma_cuadros=0
    
    #--------------------Verificar números repetidos en columnas--------------------
    for i in range(0,len(sudoku_or)):
        p=0
        f.clear()
        f1.clear()
        f2.clear()
        for j in range(0,len(sudoku_or)):
            f.append(sudoku_or[p][i])
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
    
    f=sudoku_or[:]
    num=0
    
    #--------------------Verifica números repetidos en cuadros 3x3--------------------
    for i in range(0,len(sudoku_or),3):
        f1.clear()
        num=i+3
        for j in range(i,num):
            f1.append(sudoku_or[j])
            
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
def repeticiones_columnas(tablero_c):
    f=[]
    f1=[]
    f2=[]
    f3=[]
    f4=[]
    global rep_columnas
    
    rep_columnas.clear()
    #--------------------Verificar números repetidos en columnas--------------------
    for i in range(0,len(tablero_c)):
        p=0
        f.clear()
        f1.clear()
        f2.clear()
        f3.clear()
        for j in range(0,len(tablero_c)):
            f.append(tablero_c[p][i])
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
                        f3.append(n)
            
        f3.sort()
        f4=f3[:]
        rep_columnas.append(f4)
        
        repetidos=len(f2)   
    columnas=1
#--------------------------------------------------------------------
def repeticiones_cuadros(sudoku_o):
    f=[]
    f1=[]
    f2=[]
    f3=[]
    f4=[]
    f5=[]
    f6=[]
    f7=[]
    f8=[]
    s=0
    global rep_cuadros3x3
    
    
    rep_cuadros3x3.clear()
    n_repetidos_cuadros=[]
    
    #--------------------Verifica números repetidos en cuadros 3x3--------------------
    for i in range(0,len(sudoku_o),3): #Filas
        f1.clear()
        
        num=i+3
        for j in range(i,num):
            f1.append(sudoku_o[j])
        #print(f1)
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
                    f.clear()
                for l in range(n, o):
                    f2.append(f1[k][l])
                    
            
            f3=f2[:]
            #print(f3)
            f4.clear()
            for p in range(0,len(f2)):
                valor=f2[p]
                for q in range(0,len(f2)):
                    if p != q:
                        valor1=f3[q]
                        if valor == valor1:
                            f3[q]=0
                            f4.append(valor1)
                            f.append(q)
            repetidos=len(f4)
            f.sort()
            '''print('')
            print("-----------F-----------")
            print(f)'''
            #print(i)
            
            #Determinar posiciones "reales dentro delo sudoku (fila, columna)" de los números que se repiten en los cuadros3x3
            f8.clear()
            for r in range (len(f)):
                
                f6.clear()
                if s==0:
                    #print("t-----------")
                    if f[r]>=0 and f[r]<=2:
                        t=i
                        #print(t)
                        f6.append(t)
                        if f[r]==0:
                            f6.append(s)
                        if f[r]==1:
                            f6.append(s+1)
                        if f[r]==2:
                            f6.append(s+2)
                            
                    if f[r]>=3 and f[r]<=5:
                        t=i+1
                        #print(t)
                        f6.append(t)
                        if f[r]==3:
                            f6.append(s)
                        if f[r]==4:
                            f6.append(s+1)
                        if f[r]==5:
                            f6.append(s+2)
                            
                    if f[r]>=6 and f[r]<=8:
                        t=i+2
                        #print(t)
                        f6.append(t)
                        if f[r]==6:
                            f6.append(s)
                        if f[r]==7:
                            f6.append(s+1)
                        if f[r]==8:
                            f6.append(s+2)
                            
                if s==1:
                    #print("t-----------")
                    if f[r]>=0 and f[r]<=2:
                        t=i
                        #print(t)
                        f6.append(t)
                        if f[r]==0:
                            f6.append(s+2)
                        if f[r]==1:
                            f6.append(s+3)
                        if f[r]==2:
                            f6.append(s+4)
                            
                    if f[r]>=3 and f[r]<=5:
                        t=i+1
                        #print(t)
                        f6.append(t)
                        if f[r]==3:
                            f6.append(s+2)
                        if f[r]==4:
                            f6.append(s+3)
                        if f[r]==5:
                            f6.append(s+4)
                            
                    if f[r]>=6 and f[r]<=8:
                        t=i+2
                        #print(t)
                        f6.append(t)
                        if f[r]==6:
                            f6.append(s+2)
                        if f[r]==7:
                            f6.append(s+3)
                        if f[r]==8:
                            f6.append(s+4)
                if s==2:
                    #print("t-----------")
                    if f[r]>=0 and f[r]<=2:
                        t=i
                        #print(t)
                        f6.append(t)
                        if f[r]==0:
                            f6.append(s+4)
                        if f[r]==1:
                            f6.append(s+5)
                        if f[r]==2:
                            f6.append(s+6)
                            
                    if f[r]>=3 and f[r]<=5:
                        t=i+1
                        #print(t)
                        f6.append(t)
                        if f[r]==3:
                            f6.append(s+4)
                        if f[r]==4:
                            f6.append(s+5)
                        if f[r]==5:
                            f6.append(s+6)
                            
                    if f[r]>=6 and f[r]<=8:
                        t=i+2
                        #print(t)
                        f6.append(t)
                        if f[r]==6:
                            f6.append(s+4)
                        if f[r]==7:
                            f6.append(s+5)
                        if f[r]==8:
                            f6.append(s+6)
                        
                f7=f6[:]
                f8.append(f7)
            
            
            f9=f8[:]
            '''print("-----------S")
            print(s)
            print("F9")
            print(f9)'''
            f5=f[:]
            n_repetidos_cuadros.append(repetidos)
            rep_cuadros3x3.append(f9) 
            if s<2:
                s+=1
            else:
                s=0                  
#--------------------------------------------------------------------
def mutacion(sudoku_o):
    
    global rep_columnas
    global rep_cuadros3x3
    
    d=0
    e=0
    mu=sudoku_o[:]
    
   
    if m==0:
        fila = rd.randint(0,b-1)
        columna1 = rd.randint(0,b-1)
        columna2 = rd.randint(0,b-1)
        
        valor1 = mu[fila][columna1]
        valor2 = mu[fila][columna2]
        
        mu[fila][columna2] = valor1
        mu[fila][columna1] = valor2
      
    #----------------------------------------------------------------
    if m==1:
        
        for i in range(0, len(rep_columnas)):
            if len(rep_columnas[i]) != 0:
                d+=1
        for i in range(0, len(rep_cuadros3x3)):
            if len(rep_cuadros3x3) != 0:
                e+=1
        if d!=0:
            for k in range (3):
                #print("REP_COLUMNAS")
                #print(rep_columnas)
                n_random = rd.randint(0, len(rep_columnas)-1)
                '''print(n_random)
                print("rep_columnas[n_random]")
                print(rep_columnas[n_random])'''
                if len(rep_columnas[n_random]) == 0:
                    #print("False")
                    while len(rep_columnas[n_random]) == 0:
                        n_random = rd.randint(0, len(rep_columnas)-1)
                
                '''print(n_random)
                print("rep_columnas[n_random]")
                print(rep_columnas[n_random])'''
                
                pos=rd.randint(0, len(rep_columnas[n_random])-1)
                fila=rep_columnas[n_random][pos]
                        
                columna1 = n_random
                columna2 = rd.randint(0,b-1)
                '''print("----------Fila----------")
                print(fila)
                print("----------Columnas----------")
                print(columna1, columna2)
                
                print("-------------------------------------Mu-------------------------------")
                for i in range (len(mu)):
                    print(mu[i])'''
                        
                valor1 = mu[fila][columna1]
                valor2 = mu[fila][columna2]
                
                '''print('')
                print(valor1, valor2)'''
                        
                mu[fila][columna2] = valor1
                mu[fila][columna1] = valor2
                
                '''print("-------------------------------------Muuuutado-------------------------------")
                for i in range (len(mu)):
                    print(mu[i])'''
        
    return mu
#--------------------------------------------------------------------
def seleccion(original, mutado, fit_o, fit_m):
    sel=[]
    global mejor_fit
    
    '''print('')
    print("----------Selección----------")
    print(fit_o, fit_m)'''
    
    if fit_o > fit_m:
        #print("mejor fit fit_mutacion ", fit_m)
        for i in range(0, len(mutado)):
            sel.append(mutado[i])
        mejor_fit = fit_m
    else:
        #print("mejor fit fit_original ", fit_o)
        for i in range(0, len(original)):
            sel.append(original[i])
        mejor_fit = fit_o
    
    return sel
#--------------------------------------------------------------------
sele=[]
m_fit=[]
minimo=[]
tablero_c=[]
sudoku_mutado=[]
sudoku_original=[]

conta=0
mejor_fit=0
iteracion=0
i_encontrado=0
fitness_mutado=0
fit_mas_pequeño=1000
fitness_original=0


rep_columnas=[] #Guarda lista de posiciones de los valores que se repiten por columna
rep_cuadros3x3=[] #Guarda lista de posiciones de los valores que se repiten por cuadros3x3

iteraciones = int(input("Proporcione el numero máximo de iteraciones: "))
m=0
a=1 
b=9
contador=1
mu=b

sudoku_original=poblacion_i(a,b,mu)

while contador<2:
    while iteracion<iteraciones:
        fitness_original= fitness(sudoku_original)
        #print("Fitness del original: ", fitness_original)
        repeticiones_columnas(sudoku_original)
        repeticiones_cuadros(sudoku_original)
    
        tablero_c = c.deepcopy(sudoku_original)
     
        sudoku_mutado = mutacion(tablero_c)
        fitness_mutado = fitness(sudoku_mutado)  
        #print("Fitness de la mutación: ", fitness_mutado)
            
        sele = seleccion(sudoku_original, sudoku_mutado, fitness_original, fitness_mutado)
    
        sudoku_original.clear()
        sudoku_original=sele[:]
        
        #----------------------------------------------------------------
        if fit_mas_pequeño>mejor_fit:
            fit_mas_pequeño=mejor_fit
            i_encontrado=conta
            iteracion=0
            contador=0
            m=0
        else:
            iteracion+=1
        m_fit.append(fit_mas_pequeño)
        #----------------------------------------------------------------
        conta+=1
    m=1
    iteracion=0
    contador+=1
    
print('')
print("Columnas repetidas")
for i in range(len(rep_columnas)):
    print(rep_columnas[i])

print('')    
print("Cuadros repetidos")
for i in range(len(rep_cuadros3x3)):
    print(rep_cuadros3x3[i])
print('')
print("-----------Solución-----------")
for i in range(0,len(sudoku_original)):
        print(sudoku_original[i])
print(min(m_fit))

plt.plot(m_fit)
plt.xlabel('Iteraciones')
plt.ylabel('Fitness')
plt.legend()
plt.show()
