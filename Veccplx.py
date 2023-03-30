import numpy as np
import math
import cmath


def sumavec(v, w):
    tamano = len(v)
    suma = np.zeros(tamano, dtype=np.complex_)
    k = 0
    while k < tamano:
        suma[k] = v[k] + w[k]
        k = k + 1
    return suma


def invvec(v):
    tamano = len(v)
    resultado = np.zeros(tamano, dtype=np.complex_)
    k = 0
    while k < tamano:
        resultado[k] = v[k] * -1
        k = k + 1
    return resultado


def multescvec(v, c):
    tamano = len(v)
    resultado = np.zeros(tamano, dtype=np.complex_)
    k = 0
    while k < tamano:
        resultado[k] = v[k] * c
        k = k + 1
    return resultado


def sumamtx(A, B):
    tamanofA = len(A)
    tamanocA = len(A[0])
    tamanofB = len(B)
    tamanocB = len(B[0])
    if tamanofA != tamanocB and tamanocA != tamanofB:
        raise Exception('Incompatible types')
    else:
        suma = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
        for j in range(tamanofA):
            for k in range(tamanocA):
                suma[j][k] = A[j][k] + B[j][k]
    return suma


def invmtx(A):
    tamanofA = len(A)
    tamanocA = len(A[0])
    resultado = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
    for j in range(tamanofA):
        for k in range(tamanocA):
            resultado[j][k] = A[j][k] * -1

    return resultado


def multescmtx(A, c):
    tamanofA = len(A)
    tamanocA = len(A[0])
    resultado = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
    for j in range(tamanofA):
        for k in range(tamanocA):
            resultado[j][k] = A[j][k] * c
    return resultado

def trans(A):
    tamanofA = len(A)
    tamanocA = len(A[0])
    if tamanocA > 1 and tamanofA > 1:
            resultado = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
            for j in range(tamanofA):
                for k in range(tamanocA):
                    resultado[j][k] = A[k][j]
    elif tamanocA > 1:
        resultado = np.zeros((tamanocA,1), dtype=np.complex_)    
        for i in range(tamanocA):
            resultado[i][0] = A[0][i]
    elif tamanofA > 1 and tamanocA == 1:
        resultado = np.zeros((1,tamanofA), dtype=np.complex_)    
        for j in range(tamanofA):
            resultado[0][j] = A[j][0]       
    return resultado

def conj(A):
    tamanofA = len(A)
    tamanocA = len(A[0])
    resultado = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
    for j in range(tamanofA):
        for k in range(tamanocA):
            resultado[j][k] = np.conjugate((A[j][k]))
    return resultado

def adj(A):
    tamanofA = len(A)
    tamanocA = len(A[0])
    if tamanocA > 1 and tamanofA > 1:
        resultado = np.zeros((tamanocA, tamanofA), dtype=np.complex_)
        for j in range(tamanocA):
            for k in range(tamanofA):
                resultado[j][k] = np.conjugate((A[k][j]))        
    else:
        resultado = np.zeros((tamanocA, 0), dtype=np.complex_)
        At = A.T
        resultado = np.conjugate(At)         
    return resultado

def multmat(A, B):
    tamanofA = len(A)
    tamanocA = len(A[0])
    tamanofB = len(B)
    tamanocB = len(B[0])

    if tamanocA != tamanofB:
        raise Exception('Incompatible types')
    else:
        mult = np.zeros((tamanofA, tamanocB), dtype=np.complex_)
        for j in range(tamanofA):
            for k in range(tamanocB):
                for l in range(tamanofB):
                    mult[j][k] += A[j][l] * B[l][k]
    return mult

def accvec(A, x):
    tamanofA = len(A)
    tamanocA = len(A[0])
    tamanov = len(x[0])
    tamanovf = len(x)
    resultado = np.zeros((tamanofA, tamanov), dtype=np.complex)
    for j in range(tamanofA):
        for k in range(tamanov):
            for l in range(tamanovf):
                resultado[j][k] += A[j][l] * x[l][k]
    return resultado

def prodint(A,B):
    tamanofA = len(A)
    tamanocA = len(A[0])
    tamanofB = len(B)
    tamanocB = len(B[0])
    m1 = np.zeros((tamanofA, tamanocB), dtype=np.complex_)
    j = 0
    resultado = np.complex_()
    m1 = multmat(adj(A),B)
    tamanom1f = len(m1)
    for j in range(tamanom1f):
        resultado = resultado + m1[j][j]
    return resultado

def norma(A):
    resultado = np.complex_()
    resultado = cmath.sqrt(prodint(A,A))
    return resultado


def dist(A,B):
    resultado = np.complex_()
    resultado = cmath.sqrt(prodint(A-B, A-B))
    return resultado

def hermi(A):
    if np.array_equal(A,adj(A)):
        resultado = True
    else:
        resultado = False

    return resultado

def unit(A):
    tamanofA = len(A)
    tamanocA = len(A[0])

    m = np.zeros((tamanofA, tamanocA), dtype=np.complex_)
    m = multmat(A,adj(A))
    n = np.identity(tamanocA)

    if np.array_equal(m,n):
        resultado = True
    else:
        resultado = False


    return resultado

def prodtens(A,B):
    tamanofA = len(A)
    tamanocA = len(A[0])
    tamanofB = len(B)
    tamanocB = len(B[0])
    nfilas = tamanofA * tamanofB
    ncolumnas = tamanocA * tamanocB
    resultado = np.zeros((nfilas, ncolumnas), dtype=np.complex_)
    for j in range(nfilas):
        for k in range(ncolumnas):
            resultado[j][k] = A[j // tamanofB, k // tamanocB] * B[j % tamanofB, k % tamanocB]
    return resultado

def valProp(A):
    eigenvalue = np.zeros(2, dtype=np.complex_)
    eigenvalue, featurevector = np.linalg.eig(A)
    return eigenvalue

def vecProp(A):
    eigenvalue, featurevector = np.linalg.eig(A)
    return featurevector
