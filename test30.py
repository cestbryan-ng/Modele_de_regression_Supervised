import numpy as np
import matplotlib.pyplot as plt
import customtkinter as ctk
from tkinter import messagebox
from math import *

# Génerer les points de Chebyshev
def cheb(born_inf : int, born_sup : int, n : int) :
    x_i = list()
    for k in range(1, n + 1) :
        x_i.append((born_inf + born_sup) / 2 + ((born_sup - born_inf) / 2) * np.cos(((2 * k - 1) * np.pi) / (2 * n)))
    return x_i

# Génerer des points équidisants
def equi(born_inf : int, born_sup : int, n : int) :
    return np.linspace(born_inf, born_sup, n)

# Calcul de la valeur en point du polynome de lagrange
def p(a, n : int, fonction : str, liste_points : list) :
    # Calcul de la valeur du polynome en un point x
    somme_poly = 0

    for i in range(n) :
        produit_lag = 1
        for j in range(n) :
            if not i == j :
                division_lag = a - liste_points[j][0]
                division_lag /= liste_points[i][0] - liste_points[j][0]
                produit_lag *= division_lag
        somme_poly += liste_points[i][1] * produit_lag
    
    return somme_poly

# Interface
class MonApp(ctk.CTk) :
    X = np.linspace(-25, 25, 500)

    def __init__(self):
        super().__init__()
        self.title("Interpolation")
        self.geometry("300x250")

        #polices
        self.font1 = ctk.CTkFont(family = "Cambria", size = 15, weight = "bold", underline = True)
        self.font2 = ctk.CTkFont(family = "Cambria", size = 15, weight = "bold")

        #Elements de l'interface
        self.labe1 = ctk.CTkLabel(self, text = "Interpolation Lagrangienne", font = self.font1)
        self.labe1.pack(pady = 15)

        self.labe2 = ctk.CTkLabel(self, text = "Entrer le nombre de points à interpoler", font = self.font2)
        self.labe2.pack(pady = 15)

        self.combobox1 = ctk.CTkComboBox(self,  width = 100, corner_radius = 10, border_width = 2, values = ['2', '3', '10', '30','40', '80', '160'])
        self.combobox1.place(x= 100, y = 180)

        self.combobox2 = ctk.CTkComboBox(self,  width = 130, corner_radius = 10, border_width = 2, values = ["1/(1+x**2)", "1/(1+exp(-x**2))"])
        self.combobox2.place(x = 60, y = 130)

        self.button1 = ctk.CTkButton(self, text = "Valider", width = 20, corner_radius = 10, border_width = 2, command = self.tracer, hover_color = "gray")
        self.button1.place(x = 200, y = 130)

    # Evenements
    def tracer(self) :
        fonction = self.combobox2.get()

        if fonction == "" :
            messagebox.showinfo("Erreur", "Entrer une fonction")
            return

        if self.combobox1.get() == "" :
            messagebox.showinfo("Erreur", "Donner une valeur")
            return
        
        try :
            nombre_points = int(self.combobox1.get())

            if nombre_points <= 0 :
                messagebox.showinfo("Erreur", "Entrer un nombre superieur à 0")
                return
            
            # Generer une liste de points
            x_i = equi(-25, 25, nombre_points)
            liste_points = list()
            for x in x_i :
                liste_points.append((x, eval(fonction)))

            Y, Y_polynome = list(), list()
            for x in MonApp.X :
                Y.append(eval(fonction))
                Y_polynome.append(p(x, nombre_points, fonction, liste_points))
            Y = np.array(Y)
            Y_polynome = np.array(Y_polynome)

            plt.plot(MonApp.X, Y, label = fonction, linewidth = 2)
            plt.plot(MonApp.X, Y_polynome, ls = "--", label = f"Polynome d'interpolation en {nombre_points} points")
            plt.xlabel("Axe des x")
            plt.ylabel("Axe des y")
            plt.xlim(-25, 25)
            plt.ylim(-0.25, 1.25)
            plt.grid(True)
            plt.legend()
            plt.title("Interpolation Lagrangienne")
            plt.show()
            
        except ValueError :
            messagebox.showinfo("Erreur", "Entrer un nombre")

# Point de demarrage de l'interface
if __name__ == "__main__" :
    app = MonApp()
    app.mainloop()