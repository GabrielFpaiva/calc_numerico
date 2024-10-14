import numpy as np
from scipy.linalg import solve

# Coeficientes das equações (matriz A)
A_prod = np.array([[1, 2, 4, 20], 
                   [3, 4, 25, 50], 
                   [10, 15, 18, 22], 
                   [10, 8, 8, 15]])

# Vetor de recursos disponíveis (b)
b_prod = np.array([504, 1970, 970, 601])

# Resolvendo o sistema de equações
x_prod = solve(A_prod, b_prod)

# Arredondando para o número inteiro de computadores produzidos por dia
x_prod_int = np.round(x_prod).astype(int)

# Exibindo o resultado
print(f"Número de computadores produzidos por tipo: {x_prod_int}")
