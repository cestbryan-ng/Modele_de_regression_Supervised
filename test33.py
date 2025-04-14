import numpy as np
import matplotlib.pyplot as plt
from random import randint

# Le nuage de point
x = list(set([randint(1, 50) for i in range(80)]))
y = sorted([randint(500, 800) for i in range(len(x))])
plt.scatter(x, y, marker = "x", color = "gray")

# Régression par gradient descent

theta = np.random.randn(2, 1)
x = np.reshape(x, (len(x), 1))
y = np.reshape(y, (len(x), 1))
X = np.hstack((x, np.ones(x.shape)))

# Géneration d'un modèle F = XO
def model(X, theta) :
    return np.dot(X, theta) # F
    

# Fonction de coût
def cost(F, Y) :
    return np.sum((F - Y) ** 2) / (2 * len(Y))

# Gradients
def gradient(X, Y, theta) :
    return np.dot(X.T, (np.dot(X, theta) - Y)) / len(Y)

# Gradient Descent
def gradient_descent(theta, X, Y, pas, nombre_iter) :
    for i in range(nombre_iter) :
        theta -= pas * gradient(X, Y, theta)
    return theta

# Répresentation de la régression
theta = gradient_descent(theta, X, y, 0.001, 100000)
modele = model(X, theta)
plt.plot(x, modele, color = "red", label = "Estimation descent gradient")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Coût de la régression : {cost(modele, y):.2f}")
plt.show()
