import matplotlib.pyplot as plt

# Função de cálculo
def calcular_funcao(x):
    return x ** 2 + 2 * x + 1

# Solicita ao usuário para inserir os valores
x_inicial = int(input("Digite o valor inicial de x: "))
x_final = int(input("Digite o valor final de x: "))
passo = float(input("Digite o valor do passo: "))

# Cálculo dos resultados
x_valores = []
y_valores = []
x = x_inicial

while x <= x_final:
    x_valores.append(x)
    y_valores.append(calcular_funcao(x))
    x += passo

# Criação do gráfico de linha
plt.plot(x_valores, y_valores)

# Configurações do gráfico
plt.title('Gráfico da Função')
plt.xlabel('X')
plt.ylabel('Y')

# Exibição do gráfico
plt.show()
