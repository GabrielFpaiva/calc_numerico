import numpy as np

# Sistema de equações ajustado
A_new = np.array([[3, -1, 1], [1, 3, 7], [3, 6, 2]])
b_new = np.array([1, 4, 0])

# Critério das linhas: verifica se a diagonal de A domina
def criterio_das_linhas(A):
    for i in range(len(A)):
        diagonal_element = abs(A[i, i])
        off_diagonal_sum = sum(abs(A[i, j]) for j in range(len(A)) if i != j)
        if diagonal_element <= off_diagonal_sum:
            return False
    return True

# Critério de Sassenfeld: verifica a convergência pelo método de Sassenfeld
def criterio_de_sassenfeld(A):
    n = len(A)
    beta = np.zeros(n)
    for i in range(n):
        sum_a = 0
        for j in range(n):
            if i != j:
                sum_a += abs(A[i, j]) * (beta[j] if j < i else 1)
        beta[i] = sum_a / abs(A[i, i])
    return max(beta) < 1

# Método de Gauss-Seidel ajustado para melhor precisão
def gauss_seidel_adjusted(A, b, tol=0.001, max_iterations=100):
    n = len(b)
    x = np.zeros_like(b, dtype=np.float64)
    for it_count in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            sum_ax = np.dot(A[i, :i], x_new[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum_ax) / A[i, i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, it_count
        x = x_new
    return x, it_count

# Verificando os critérios de convergência
crit_linhas_new = criterio_das_linhas(A_new)
crit_sassenfeld_new = criterio_de_sassenfeld(A_new)

# Resolvendo o sistema pelo método de Gauss-Seidel
solution_new_adjusted, iterations_new_adjusted = gauss_seidel_adjusted(A_new, b_new)

# Exibindo o resultado
print(f"Critério das Linhas: {crit_linhas_new}")
print(f"Critério de Sassenfeld: {crit_sassenfeld_new}")
print(f"Solução encontrada: {solution_new_adjusted}")
print(f"Iterações: {iterations_new_adjusted}")
