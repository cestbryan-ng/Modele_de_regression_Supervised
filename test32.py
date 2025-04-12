import numpy as np
import matplotlib.pyplot as plt
from random import randint
from copy import deepcopy

# Le nuage de point
x = list(set([randint(1, 10) for i in range(10)]))
y = sorted([randint(500, 800) for i in range(len(x))])

# Régréssion polynomiale
# Principe résoudre SC=W donné par la formule des moindres carrées 
# les solutions de C = (c0, c1, c2, c3, ...) sont les coéfficents du modèle

# W
def calcul_w(x, y, degree = 1) :
    som, w = list(), list()    
    for j in range(degree + 1) :
        for i in range(len(x)) : # or len(y)
            som.append(y[i] * (x[i] ** j))
        w.append(sum(som))
        som.clear()
    w = np.reshape(w, (len(w), 1))
    return w

# S
def calcul_s(x, y, degree = 1) :
    som, s_j = list(), list()
    for j in range((degree + 1) * 2) :
        for i in x :
            som.append(i ** j)
        s_j.append(sum(som))
        som.clear()
    s = np.zeros((degree + 1, degree + 1))
    for i in range(degree + 1) :
        indice = i
        for j in range(degree + 1) :
            s[i][j] = s_j[indice]
            indice += 1
    return s

# C = (c0, c1, c2, c3, ...)
def calcul_c(s, w) :
    c = list()
    for i in range(len(w)) :
        s_copy = deepcopy(s)
        s_copy[:,i] = w[:,0]
        c_i = np.linalg.det(s_copy) / np.linalg.det(s)
        c.append(float(round(c_i, 2)))
    return c

# calcul de la valeur en un point du modèle
def reg_poly(c, x) :
    som = list()
    for i, j in enumerate(c) :
        som.append(j * (x ** i))
    return sum(som)

# Affichage du nuage et du modèle linéaire simple
s = calcul_s(x, y)
w = calcul_w(x, y)
c = calcul_c(s, w)

x_reg, y_reg = np.linspace(min(x) - 1, max(x) + 1, 100), list()
for i in x_reg :
    y_reg.append(reg_poly(c, i))

plt.scatter(x, y, marker = "x")
plt.plot(x_reg, y_reg, label = "Estimation", color = "red")
plt.xlim(min(x) - 1, max(x) + 1)
plt.ylim(min(y) - 50, max(y) + 50)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Régression")
plt.legend()
plt.grid(True)
plt.show()