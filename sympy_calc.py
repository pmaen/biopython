#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 07:47:45 2021
@author: paul
"""

from sympy import *
from IPython.display import Math
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Α, α, Β, β, Γ, γ, Δ, δ, Ε, ε, Ζ, ζ, Η, η, Θ, θ, Ι, ι, Κ, κ, Λ, λ, Μ, μ, Ν, ν, Ξ, ξ, Ο, ο, Π, π, Ρ, ρ, Σ, σ, ς, Τ, τ, Υ, υ, Φ, φ, Χ, χ, Ψ, ψ, Ω, ω = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Α α Β β Γ γ Δ δ Ε ε Ζ ζ Η η Θ θ Ι ι Κ κ Λ λ Μ μ Ν ν Ξ ξ Ο ο Π π Ρ ρ Σ σ ς Τ τ Υ υ Φ φ Χ χ Ψ ψ Ω ω')
mode = input("Choose the operation:\n Differentiate (1)\n Integrate (2)\n Limit (3)\n Series expansion (4)\n Finite differentiation (5)\n Expand (6)\n Simplify (7)\n")

#Notes about the different modes
if mode == str(2):
    print("Be aware that multiple integrals have to be performed by hand on the code.")    
function = input("Function:\t")
if mode == str(1):
    print("Note: For the following part you can use x, 2 instead of x, x (second derivative) and multiple variables separated by comma give the total differential.")
if mode == str(2) or mode == str(3):
    print("Note: Infinity is written as two lowercase 'o'.")
if mode != str(5) and mode != str(6) and mode != str(7):
    parameter = input("Parameters:\t")

if mode == str(1):
    deriv = diff(function, *parameter.split(','))
    print(str(deriv) + "\t\t LaTeX:\t" + str(printing.latex(deriv)))
if mode == str(2):
    intg = integrate(function, *parameter.split(','))
    print(str(intg) + "\t\t LaTeX:\t" + str(printing.latex(intg)))
if mode == str(3):
    lim = limit(function, *parameter.split(','))
    print(str(lim) + "\t\t LaTeX:\t" + str(printing.latex(lim)))
if mode == str(4):
    expr = function
    serex = series(function, *parameter.split(','))
    print(str(serex) + "\t\t LaTeX:\t" + str(printing.latex(serex)))
if mode == str(5):
    findif = differentiate_finite(function)
    print(str(findif) + "\t\t LaTeX:\t" + str(printing.latex(findif)))
if mode == str(6):
    expan = expand(function)
    print(str(expan) + "\t\t LaTeX:\t" + str(printing.latex(expan)))
if mode == str(7):
    simp = simplify(function)
    print(str(simp) + "\t\t LaTeX:\t" + str(printing.latex(simp)))      