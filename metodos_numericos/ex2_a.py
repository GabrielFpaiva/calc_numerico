def derivada(v, g, k, m):
    # Calcula a derivada da velocidade (aceleração) com base na EDO fornecida.
    return g - k*abs(v)*v/m

def euler_step(m, g, k, v0, dt, n_steps):
    # Inicializa a velocidade com seu valor inicial.
    v = v0
    # Inicializa uma lista para armazenar as velocidades em cada passo.
    velocities = [v0]

    for _ in range(n_steps):
        # Atualiza a velocidade somando a variação de velocidade.
        v += dt * derivada(v, g, k, m)
        # Adiciona a velocidade atualizada à lista de velocidades.
        velocities.append(v)

    return velocities


# Parâmetros
m = 0.11       # Massa do projétil
g = -9.8       # Aceleração da gravidade
k = 0.002      # Coeficiente de resistência do ar 
v0 = 8         # Velocidade inicial 
dt = 0.1       # Intervalo de tempo para discretização da EDO.
n_steps = 10   # Número de passos para a simulação.

# Chamando a função método de Euler para os parâmetros definidos.
velocities = euler_step(m, g, k, v0, dt, n_steps)


# Exibindo as velocidades em cada passo.
for i, v in enumerate(velocities):
    print(f"Tempo {i*dt:.1f}s: Velocidade = {v:.2f} m/s")
