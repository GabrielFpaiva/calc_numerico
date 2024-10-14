# Dados fornecidos
t = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
v = [0, 4.67, 7.34, 8.86, 9.73, 10.22, 10.51, 10.67, 10.76, 10.81, 10.81]

# Definindo o tamanho do intervalo
h = (t[-1] - t[0]) / (len(t) - 1)

# Aplicando a regra 1/3 de Simpson
integral = v[0] + v[-1]
for i in range(1, len(t)-1):
    if i % 2 == 0:  # índices pares
        integral += 2 * v[i]
    else:          # índices ímpares
        integral += 4 * v[i]

integral *= h/3

print(f"Distância estimada percorrida nos primeiros 5 segundos: {integral:.2f} metros")
