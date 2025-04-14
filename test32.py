import numpy as np
import matplotlib.pyplot as plt
from random import randint
from copy import deepcopy

# Dataset
print("Remplissement du dataset")
while True :
    x = input("Valeur du tableau x : ").split()
    x = [int(i) for i in x]
    y = input("Valeur du tableau y : ").split()
    y = [float(i) for i in y]
    if len(x) != len(y) :
        print("Les deux tableaux doivent avoir la même taille.")
        continue
    break
# x = list(set([randint(1, 50) for i in range(80)]))
# y = sorted([randint(500, 800) for i in range(len(x))])

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

# fonction coût
def cost(x, y, c) :
    som = list()
    for i in range(len(x)) :
        som.append((reg_poly(c, x[i]) - y[i]) ** 2)
    return sum(som) / (2 * len(x))

# calcul du dégrée
def calcul_degree(y) :
    degree = 1
    for i in range(len(y) - 1) :
        if y[i] > y[i + 1] :
            degree += 1
    return degree

# Affichage du nuage et du modèle linéaire simple
degree = calcul_degree(y)
s = calcul_s(x, y, degree)
w = calcul_w(x, y, degree)
c = calcul_c(s, w)

x_reg, y_reg = np.linspace(min(x) - 1, max(x) + 1, 100), list()
for i in x_reg :
    y_reg.append(reg_poly(c, i))

plt.scatter(x, y, marker = "x", color = "gray")
plt.plot(x_reg, y_reg, label = f"Estimation moindre carré degrée polynome = {degree}", color = "red")
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Coût de la régression (Pas encore optimal) : {cost(x, y, c):.2f}")
plt.legend()
plt.show()