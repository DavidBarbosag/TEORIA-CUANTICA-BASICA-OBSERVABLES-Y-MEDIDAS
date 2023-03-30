import numpy as np
import math
import cmath
import Veccplx as vc



def normvec(A):
    tamanofA = len(A)
    den = 0
    resultado = np.zeros((tamanofA,1),dtype=np.complex_)
    if vc.norma(A) == 1:
        resultado = A
    else:
        j = 0
        for j in range(tamanofA):
           resultado[j][0] = (A[j][0]) *  (1/vc.norma(A))
    return resultado


# punto 1.1

def prob(A):
    tamanofA = len(A)
    num = A[3] * np.conjugate(A[3])
    den = 0
    j = 0
    for j in range(tamanofA):
        den = ((A[j]) * np.conjugate((A[j])) + den)
    resultado = num / den
    return resultado

# punto 1.2
def amptrans(A, B):
    if vc.norma(A) == 1 and vc.norma(A) == 1:
        resultado = vc.prodint(B, A)
    else:
        norm_A = normvec(A)
        norm_B = normvec(B)
        resultado = vc.prodint(norm_B,norm_A)
    return resultado

# punto 1 retos
def probtrans(A,B):
    amptra = amptrans(A,B)
    resultado = vc.norma(amptra)**2
    return resultado

def valEsp(omeg,B):
    bra = vc.multmat(omeg,B)
    resultado = vc.prodint(bra,B)
    return resultado

# punto 2 retos
def var(omeg,B):
    verHerm = vc.hermi(omeg)
    if verHerm == True:
        tamanofomeg = len(A)
        n = np.identity(tamanofomeg)
        # valor esperado * matriz identidad
        veI = vc.multescmtx(n, valEsp(omeg,B))
        delta = np.add(omeg,-veI)
        multdel = vc.multmat(delta,delta)
        adjB = vc.adj(B)
        part1 = vc.multmat(adjB,multdel) 
        resultado = vc.multmat(part1,B) 
    else: 
        resultado = False
    return resultado
# punto 3 retos
def med(omeg,si):
    valprop = vc.valProp(omeg)
    columna = np.zeros((2,1), dtype=np.complex_)
    for i in range(0,2):
        columna[i][0] = valprop[i]
    norm = normvec(columna)
    norm2 = vc.adj(norm)
    resultado = vc.prodint(norm,si)
    return resultado*np.conjugate(resultado)

# punto 4 retos


si = np.array([   
    [-1],
    [-1 - 1j]
])

omeg = np.array([   
    [-1, -1j],
    [1j , 1]
])

A = np.array([
    [1,2],
    [2,1]

])

# ejercicio 4.3.2
print(med(omeg,si))


# ejercicio 4.4.1

U1 = np.array([
    [0, 1],
    [1, 0]

])

U2 = np.array([
    [((2)**0.5)/2, ((2)**0.5)/2],
    [((2)**0.5)/2, -((2)**0.5)/2]

])

mult = vc.multmat(U1,U2)
veri = vc.unit(mult)

if veri == True:
    print("Es unitaria")
else:
    print("No es unitaria") 


# ejercicio 4.4.2

Mat = np.array([
    [0, 1/((2)**0.5), 1/((2)**0.5), 0 ],
    [1j/((2)**0.5), 0, 0, 1/((2)**0.5)],
    [1/((2)**0.5), 0, 0, 1j/((2)**0.5)],
    [0, 1/((2)**0.5), -1/((2)**0.5), 0]
])

isv = np.array([   
    [1],
    [0],
    [0],
    [0]
])

X0 = vc.multmat(Mat,isv) 
X1 = vc.multmat(Mat,X0)
X2 = vc.multmat(Mat,X1)
print(prob(X2))
