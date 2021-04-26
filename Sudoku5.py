# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:29:29 2021

@author: brenda
"""
import copy as c
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
    global rep_cuadros3x3
    
    rep_cuadros3x3.clear()
    n_repetidos_cuadros=[]
    
    #--------------------Verifica números repetidos en cuadros 3x3--------------------
    for i in range(0,len(sudoku_o),3):
        f1.clear()
        num=i+3
        for j in range(i,num):
            f1.append(sudoku_o[j])
            
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
                    f.clear()
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
                            f.append(q)
            repetidos=len(f4)
            f.sort()
            f5=f[:]
            n_repetidos_cuadros.append(repetidos)
            rep_cuadros3x3.append(f5)             
#--------------------------------------------------------------------
def mutacion(sudoku_o):
    
    mu=sudoku_o[:]
    #print('')
    fila = rd.randint(0,b-1)
    columna1 = rd.randint(0,b-1)
    columna2 = rd.randint(0,b-1)
    
    '''print("----------Fila----------")
    print(fila)
    print("----------Columnas----------")
    print(columna1, columna2)'''
    
    valor1 = mu[fila][columna1]
    valor2 = mu[fila][columna2]
    
    mu[fila][columna2] = valor1
    mu[fila][columna1] = valor2
    
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
m_fit=[]
sele=[]
tablero_c=[]
sudoku_mutado=[]
sudoku_original=[]

mejor_fit=0
iteracion=0
fitness_mutado=0
fitness_original=0

rep_columnas=[] #Guarda lista de posiciones de los valores que se repiten por columna
rep_cuadros3x3=[] #Guarda lista de posiciones de los valores que se repiten por cuadros3x3

iteraciones = int(input("Proporcione el numero máximo de iteraciones: "))
a=1 
b=9
contador=1
mu=b

sudoku_original=poblacion_i(a,b,mu)

while iteracion<iteraciones:
    fitness_original= fitness(sudoku_original)
    repeticiones_columnas(sudoku_original)
    repeticiones_cuadros(sudoku_original)

    tablero_c = c.deepcopy(sudoku_original)
 
    sudoku_mutado = mutacion(tablero_c)
    fitness_mutado = fitness(sudoku_mutado)  

    sele = seleccion(sudoku_original, sudoku_mutado, fitness_original, fitness_mutado)

    sudoku_original.clear()
    sudoku_original=sele[:]

    m_fit.append(mejor_fit)
    iteracion+=1
    
print('')
print("-----------Solución-----------")
for i in range(0,len(sudoku_original)):
        print(sudoku_original[i])
print(m_fit.pop())

plt.plot(m_fit)
plt.xlabel('Iteraciones')
plt.ylabel('Fitness')
plt.legend()
plt.show()
