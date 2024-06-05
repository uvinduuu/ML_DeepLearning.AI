import sympy

J, w = sympy.symbols('J,w')
J=w**3
dJ_dw=sympy.diff(J,w)
print(dJ_dw)