def derivada(v, g, k, m):
    return (g - k * abs(v) * v) / m

def runge_kutta_4(m, g, k, v0, dt):
    v = v0
    t = 0
    while v >= 0:
        k1 = dt * derivada(v, g, k, m)
        k2 = dt * derivada(v + k1/2, g, k, m)
        k3 = dt * derivada(v + k2/2, g, k, m)
        k4 = dt * derivada(v + k3, g, k, m)
        v += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += dt
    return t

#parâmetros
m = 0.11  # massa 
g = -9.8  # aceleração da gravidade(negativo para queda)
k = 0.002 # coeficiente de arrasto
v0 = 8    # velocidade inicial 
dt = 0.001  # intervalo de tempo 

tempo_queda = runge_kutta_4(m, g, k, v0, dt)
print(f"O projétil começa a cair após {tempo_queda:.2f} segundos.")
