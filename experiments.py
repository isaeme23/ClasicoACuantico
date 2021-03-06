import math
import numpy as np
import matplotlib.pyplot as plt

# Funciones Auxiliares
# Funciones que nos ayudan a hacer operaciones dentro de las funciones pedidas
# ---------------------------- * --------------------------------

def modulo(n):
    real = np.real(n)
    comp = np.imag(n)
    modu = (real**2) + (comp**2)
    return math.sqrt(modu)

def matExp(a,n):
    if n == 1:
        return a
    n -= 1
    c_ = a.copy()
    for i in range(n):
        c_ = np.dot(a,a)
    return c_

# ---------------------------- * --------------------------------

# Experimento de las canicas con coeficientes Booleanos
# Recibe la matriz, el estado y el numero de clics

def Matrix_State(matrix, state, clics):
    final = matExp(matrix, clics)
    resp = np.dot(final,state)
    return resp

# Experimento de las multiples rendijas clasico probabilistico
# Recibe el numero de rendijas (slits) y el numero de objetivos (targets)
# Se forma una matriz con estos datos mas el cero de la posicion inicial

def slitsP(slits, targets):
    n = 1+targets+slits
    s = (n,n)
    matrix, state = np.zeros(s), np.zeros(s[1])
    state[0] = 1
    one, two = 1/slits, targets/slits
    for i in range(slits):
        matrix[i+1][0] = one
    if not (two.is_integer):
        two = round(targets/slits)
        a = 1
        j = 1
        for i in range(slits+1, len(matrix)):
            matrix[i][j] = 1/two
            if a == two:
                j += 1
                matrix[i][j] = 1/two
                a = 1
            else:
                a += 1
    else:
        a = 1
        j = 1
        for i in range(slits+1, len(matrix)):
            matrix[i][j] = 1/two
            if a == two:
                a = 1
                j += 1
            else:
                a += 1
    for i in range(slits + 1, len(matrix)):
        matrix[i][i] = 1
    resp = Matrix_State(matrix, state, 2)
    list1 = resp.tolist()
    return list1

# Experimento de las multiples rendijas clasico probabilistico cuantico
# Recibe el numero de rendijas (slits) y el numero de objetivos (targets)
# Permite recibir numeros complejos y ajusta las probablidades para los mismos
# y para la cantidad de rendijas dadas
# Se forma una matriz con estos datos mas el cero de la posicion inicial

def slitsCuantum(slits, targets):
    n = slits + targets + 1
    matrix, state = np.zeros((n, n),dtype=complex), np.zeros((n),dtype=complex)
    state[0] = 1
    one, two = 1 / math.sqrt(slits), targets / slits
    for i in range(slits):
        matrix[i+1][0] = one
    if not (two.is_integer):
        two = round(targets/slits)
        a = 1
        j = 1
        for i in range(slits+1, len(matrix)):
            if i == slits + 1:
                answ = (-1+1j)/math.sqrt(two*slits)
            elif a != two:
                answ = (-1 -1j)/math.sqrt(two*slits)
            elif a == two:
                answ = (1-1j)/math.sqrt(two*slits)
            matrix[i][j] = answ
            if a == two:
                j += 1
                matrix[i][j] = (-1+1j)/math.sqrt(two*slits)
                a = 1
            else:
                a += 1
    else:
        a = 1
        j = 1
        for i in range(slits+1, len(matrix)):
            if i == slits + 1:
                answ = (-1+1j)/math.sqrt(two*slits)
            elif a != two:
                answ = (-1 -1j)/math.sqrt(two*slits)
            elif a == two:
                answ = (1-1j)/math.sqrt(two*slits)
            matrix[i][j] = answ
            if a == two:
                j += 1
                matrix[i][j] = (-1+1j)/math.sqrt(two*slits)
                a = 1
            else:
                a += 1
    for i in range(slits+1, len(matrix)):
        matrix[i][i] = 1
    resp = Matrix_State(matrix, state, 2)
    v = []
    list1 = resp.tolist()
    for i in list1:
        v.append(modulo(i)*modulo(i))
    return v

# Funcion para realizar un diagrama de barras de las porbablidades de vector de estados.
# Utlizando la libreria Mathplot

def barras(vec):
    v = []
    for i in range(len(vec)):
        v.append(i)
    plt.bar(v, vec)
    plt.show()