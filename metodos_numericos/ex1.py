# Função que define a derivada de y em relação a x
def dydx(x, y):
    return (y**2 - 2*x)/y

# Método de Euler
def euler_method(h, x_end):
    n = int(x_end / h)  # Número de passos
    y = 1.0  # Condição inicial
    x = 0.0
    for i in range(n):
        y += h * dydx(x, y)  # Atualização de y
        x += h  # Atualização de x
    return y

# Método de Runge-Kutta de 3ª ordem
def runge_kutta_3rd_order(h, x_end):
    n = int(x_end / h)
    y = 1.0  # Condição inicial
    x = 0.0
    for i in range(n):
        k1 = h * dydx(x, y)
        k2 = h * dydx(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x + h, y - k1 + 2 * k2)
        y += (k1 + 4 * k2 + k3) / 6.0  # Atualização de y
        x += h
    return y

h = 0.2
x_end = 1.0

# Valores aproximados
y_euler = euler_method(h, x_end)
y_rk3 = runge_kutta_3rd_order(h, x_end)

# Exibição dos resultados
print(f"Valor aproximado usando Euler: {y_euler}")
print(f"Valor aproximado usando Runge-Kutta de 3ª ordem: {y_rk3}")

# Solução exata
y_exato = 3**0.5

# Erros absolutos percentuais
erro_euler = abs((y_exato - y_euler) / y_exato) * 100
erro_rk3 = abs((y_exato - y_rk3) / y_exato) * 100

print(f"O erro absoluto do método de Euler foi: {erro_euler:.2f}%")
print(f"O erro absoluto do método de Runge-Kutta foi: {erro_rk3:.2f}%")
