# import matplotlib.pyplot as plt
# import numpy as np

# # Gere valores de x de 0 a 2π
# x = np.linspace(0, 2*np.pi, 400)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# # Encontrar o ponto de interseção (onde sin(x) = cos(x))
# # Isso ocorre em x = π/4 e 5π/4
# x_intersec = np.pi/4
# y_intersec = np.sin(x_intersec)

# # Criar a figura e os eixos
# plt.figure()

# # Plote as funções seno e cosseno
# plt.plot(x, y_sin, label='sin(x)')
# plt.plot(x, y_cos, label='cos(x)')

# # Marcar o ponto de interseção
# plt.scatter([x_intersec], [y_intersec], color='red')
# plt.annotate(f'Intersecção ({x_intersec:.2f}, {y_intersec:.2f})',
#              xy=(x_intersec, y_intersec), xycoords='data',
#              xytext=(-90, -50), textcoords='offset points',
#              arrowprops=dict(arrowstyle="->",
#                              connectionstyle="arc3,rad=.2"))

# # Adicione legendas e título
# plt.legend()
# plt.title('Gráfico de sin(x) e cos(x) com Ponto de Interseção')
# plt.grid(True)

# # Mostrar o gráfico
# plt.show()



## V2

import matplotlib.pyplot as plt
import numpy as np

# Gere valores de x de 0 a 2π
x = np.linspace(0, 2*np.pi, 400)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Pontos de interseção (onde sin(x) = cos(x)) no intervalo 0 a 2π são π/4 e 5π/4
intersection_points = [(np.pi/4, np.sin(np.pi/4)), (5*np.pi/4, np.sin(5*np.pi/4))]

# Criar a figura e os eixos
plt.figure()

# Plote as funções seno e cosseno
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')

# Marcar os pontos de interseção
for x_intersec, y_intersec in intersection_points:
    plt.scatter([x_intersec], [y_intersec], color='red')
    plt.annotate(f'Intersecção ({x_intersec:.2f}, {y_intersec:.2f})',
                 xy=(x_intersec, y_intersec), xycoords='data',
                 xytext=(-90, -50), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3,rad=.2"))

# Adicione legendas e título
plt.legend()
plt.title('Gráfico de sin(x) e cos(x) com Pontos de Interseção')
plt.grid(True)

# Mostrar o gráfico
plt.show()
