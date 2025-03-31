import numpy as np
from scipy.optimize import newton

def f_polynomial(x, coeffs):
    return sum(c * x**i for i, c in enumerate(coeffs))

def f_trigonometric(x, A, B, C, D, E, F):
    return A * np.sin(B * x + C) + D * np.cos(E * x + F)

def bisection_method(f, a, b, tol, max_iter):
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c, i+1
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, max_iter

def secant_method(f, x0, x1, tol, max_iter):
    for i in range(max_iter):
        if abs(f(x1)) < tol:
            return x1, i+1
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_temp
    return x1, max_iter

def false_position_method(f, a, b, tol, max_iter):
    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c, i+1
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, max_iter

print("Seleccione la función: 1) Polinómica  2) Trigonométrica")
func_choice = int(input())

if func_choice == 1:
    coeffs = list(map(float, input("Ingrese los coeficientes a0 a5 separados por espacio: ").split()))
    f = lambda x: f_polynomial(x, coeffs)
elif func_choice == 2:
    A, B, C, D, E, F = map(float, input("Ingrese A B C D E F separados por espacio: ").split())
    f = lambda x: f_trigonometric(x, A, B, C, D, E, F)
else:
    print("Opción inválida")
    exit()

print("Seleccione el método: 1) Bisección  2) Newton  3) Secante  4) Regla Falsa")
method_choice = int(input())

tol = float(input("Ingrese la tolerancia: "))
max_iter = int(input("Ingrese el número máximo de iteraciones: "))

if method_choice == 1:
    a, b = map(float, input("Ingrese el intervalo [a, b]: ").split())
    root, iterations = bisection_method(f, a, b, tol, max_iter)
elif method_choice == 2:
    x0 = float(input("Ingrese el valor inicial: "))
    root = newton(f, x0, tol=tol, maxiter=max_iter)
    iterations = max_iter
elif method_choice == 3:
    x0, x1 = map(float, input("Ingrese los valores iniciales x0 y x1: ").split())
    root, iterations = secant_method(f, x0, x1, tol, max_iter)
elif method_choice == 4:
    a, b = map(float, input("Ingrese el intervalo [a, b]: ").split())
    root, iterations = false_position_method(f, a, b, tol, max_iter)
else:
    print("Opción inválida")
    exit()

print(f"Raíz encontrada: {root}, Iteraciones: {iterations}")
