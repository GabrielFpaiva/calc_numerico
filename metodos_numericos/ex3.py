import numpy as np

# Parâmetros dados
P0 = 50976           # População inicial
b = 2.9e-2           # Taxa de nascimento constante
k = 1.4e-7           # Coeficiente proporcional à taxa de mortalidade
t_final = 5          # Tempo final 
dt = 0.01            # Tamanho do passo temporal

# Definindo a função da EDO
def dPdt(P):
    return b*P - k*P**2

# Método de Runge-Kutta de ordem 4
def runge_kutta_4th(P0, t_final, dt):
    N = int(t_final / dt)  # Número de passos
    t = np.linspace(0, t_final, N)
    P = np.zeros(N)
    P[0] = P0  # Condição inicial
    
    for i in range(1, N):
        k1 = dt * dPdt(P[i-1])
        k2 = dt * dPdt(P[i-1] + 0.5 * k1)
        k3 = dt * dPdt(P[i-1] + 0.5 * k2)
        k4 = dt * dPdt(P[i-1] + k3)
        P[i] = P[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t, P

# Executando o método
t, P = runge_kutta_4th(P0, t_final, dt)

# População estimada após 5 anos
P_estimada_5_anos = P[-1]
print(f'A população estimada após 5 anos é {P_estimada_5_anos:.2f}')
