# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:53:14 2021

@author: Brenda Pedraza Melendez
"""
import math
import random as rd
import matplotlib as matp
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
    lista1=[]
    for i in range(0,p):
        n1=n-1
        m=0
        for j in range(0,n):
            en=po[i][j]
            m+=en*2**n1
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
def ruleta(l):
    suma=0.0
    R=[]
    rul=[]
    s=0.0
    j=0
    i=0
    #Suma de todos los fitness
    for i in range(0,p):
        #suma=suma+f[i]
        suma+=f[i]
    
    if l==0:
        r1=int((r*p)/2)
        #r1=(r*p)/2
        #round(r1)
        r1*=2
        #print("*************************************************",r1)
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
        
    #print('')
    #print("Valor de R1")
    #print(r1)
    i=0
    '''print('')
    print("***************************Valores aleatorios***************************")'''
    while j<r1:
        ran=rd.uniform(0,1)
        for i in range(0,len(R)):
            if ran>R[i] and ran<R[i+1]:
                rulet.append(i)
        j=j+1 
        #print(ran)
    
    return suma
    '''print('')
    print("***************************Ruleta***************************")
    print(rul)
    print('')
    print("***************************Intervalos***************************")
    print(R)
    print('')
    print("***************************Individuos que pasan a la poblacion siguiente***************************")
    print(rulet)'''
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
    #print('')
    #print(cruce)
    #print('')
   
    for i in range(0,len(rulet)):
        pb.append(po[rulet[i]])
    
    '''print('')
    for i in range(len(pb)):
        print(pb[i])
    print('')'''
    
    if cruce!=0:
        for i in range(1,len(pb),2):
            p1.clear()
            s0.clear()
            s1.clear()
            p1.append(pb[i-1])
            p1.append(pb[i])
        
            '''print("----P1------")
            print('')
            for i in range(len(p1)):
                print(p1[i])
            print('')'''
                  
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
        #for i in range(0,len(pb)):
       Ps.append(pb)
   
    rulet.clear()
    #print(Ps)
    #p1.clear()
    #pb.clear()
    #print(rulet)
#-----------------------------------------------------------------------------------------
def mutacion():
    in_mut=int(m*p)
    '''ind=int(in_mut)
    mut=in_mut-ind
    if mut>0 and mut<0.5:
        in_mut=ind
    if mut>=0.5 and mut<1:
        in_mut=ind+1
    if mut==0:
        in_mut=int(in_mut)'''
    i=0
    
    #for i in range(0,in_mut):
    while i<in_mut:
        fila=rd.randint(0,len(Ps)-1)
        columna=rd.randint(0,n-1)
        #print("fila",fila+1,"columna",columna+1)
        
        if Ps[fila][columna]==1:
            '''print('')
            print("La posicion que se cambiará es la posicion ", columna+1, "de la fila: ",fila+1)'''
            Ps[fila][columna]=0
        else:
            '''print('')
            print("La posicion que se cambiará es la posicion ", columna+1, "de la fila: ",fila+1)'''
            Ps[fila][columna]=1
        i+=1
    
    '''print('')
    print("***************************Población Ps con mutación***************************")
    for i in range(0, len(Ps)):
        print("h",i+1,"=",Ps[i])   '''       
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
print("***************************Cantidad de bits a usar:", n)
po=poblacion_i()

'''d=decimal()
X=x()
f=fitness()

su=ruleta(0)
cruza()
ruleta(1)
seleccion()
mutacion()
po.clear()
copia()
imp_po()
Ps.clear()'''
itera=0

while itera<it:
    d=decimal()
    X=x()
    f=fitness()

    su=ruleta(0)
    cruza()
    ruleta(1)
    seleccion()
    mutacion()
    po.clear()
    copia()
    imp_po()
    Ps.clear()
    itera+=1
#promedio=su/len(po)
#print(promedio)


