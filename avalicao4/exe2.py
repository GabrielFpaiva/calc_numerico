import numpy as np

# Função que representa a variação da pressão em função da profundidade
def pressure(h):
    return 5 * h**2 + 3 * h + 2

# Intervalo de profundidade (0 a 10 metros) e número de segmentos
h_start = 0
h_end = 10
n_segments = 5

# Dividindo o intervalo em 5 segmentos iguais
h_values = np.linspace(h_start, h_end, n_segments + 1)
pressures = pressure(h_values)

# Aplicando a Regra dos Trapézios Generalizada
def trapezoidal_rule(h_values, pressures):
    # Calculando a largura de cada segmento
    h_step = (h_end - h_start) / n_segments
    # Calculando a área usando a regra dos trapézios
    area = (h_step / 2) * (pressures[0] + 2 * sum(pressures[1:-1]) + pressures[-1])
    return area

# Estimativa da área sob a curva (pressão total)
estimated_area = trapezoidal_rule(h_values, pressures)

# Exibindo o resultado
print(f"Pressão total estimada: {estimated_area:.2f} unidades de pressão.")
