# =========================================
# EJEMPLOS DE COMENTARIOS EN PYTHON
# =========================================

# Los comentarios se usan para explicar
# qué hace el código. Todo lo que esté
# después del símbolo # es ignorado por Python.

# -----------------------------------------
# Ejemplo 1: calcular la hipotenusa
# -----------------------------------------

# lado_a y lado_b representan los catetos
# de un triángulo rectángulo

lado_a = 3.0
lado_b = 4.0

# Aplicamos el teorema de Pitágoras:
# h = √(a² + b²)

# En Python las potencias se calculan con **
# y **0.5 sirve para obtener la raíz cuadrada

h = (lado_a ** 2 + lado_b ** 2) ** 0.5

# Imprimir resultado en pantalla
print("Hipotenusa calculada:", h)