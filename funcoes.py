import pandas as pd

def is_prime(number):
    if number <= 1:
        return False  # 0 e 1 não são números primos
    if number <= 3:
        return True   # 2 e 3 são primos
    if number % 2 == 0 or number % 3 == 0:
        return False  # Eliminamos múltiplos de 2 e 3
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False  # Eliminamos múltiplos de i e i + 2
        i += 6
    return True

def filter_primes(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

#is_prime(number): Esta função verifica se um número é primo ou não. Ela começa verificando se o número é menor ou igual a 1 (não é primo), depois verifica se é igual a 2 ou 3 (são primos). Em seguida, faz um loop para verificar se o número é divisível por algum número ímpar a partir de 5 até a raiz quadrada do número, com incrementos de 6 (isso é uma otimização para reduzir o número de divisões). Se o número for divisível por algum desses valores, não é primo, caso contrário, é primo.
#filter_primes(numbers): Esta função recebe uma lista de números e retorna uma nova lista contendo apenas os números primos da lista original. Ela itera sobre a lista de números e usa a função is_prime para determinar se cada número é primo ou não. Os números primos são adicionados à lista prime_numbers.

# https://fga.unb.br/articles/0001/4868/out.pdf
 
#A técnica específica que envolve o loop a partir de 5 e a verificação de divisibilidade por i e i + 2, com incrementos de 6, é conhecida como a "Otimização do Crivo de Sundaram". Esta otimização é uma forma eficaz de reduzir o número de divisões que precisam ser verificadas ao testar se um número é primo. Ela é frequentemente usada para tornar o teste de primalidade mais eficiente.

#O Crivo de Sundaram é uma variação do Crivo de Eratóstenes, que é um algoritmo usado para encontrar todos os números primos até um limite dado. A otimização de Sundaram é uma técnica que não encontra todos os números primos, mas é útil para verificar se um número individual é primo.

#Essa otimização se beneficia do fato de que, após verificar divisibilidade por 2 e 3, é possível pular várias verificações de divisibilidade por números que não podem ser primos. A adição de 6 a i em cada iteração, juntamente com a verificação de divisibilidade por i e i + 2, garante que apenas números de forma 6k ± 1 (onde k é um número inteiro) sejam testados, reduzindo assim o número de divisões necessárias.

def elementos_unicos(lista1, lista2):
    # Usamos o operador ^ (XOR) para encontrar os elementos únicos em ambas as listas.
    elementos_unicos = set(lista1) ^ set(lista2)

    # Convertemos o resultado de volta para uma lista.
    resultado = list(elementos_unicos)

    return resultado

#elementos_unicos = set(lista1) ^ set(lista2): Nesta linha, criamos dois conjuntos a partir das listas lista1 e lista2 usando a função set(). Em seguida, usamos o operador ^ (XOR) para calcular a diferença simétrica entre esses conjuntos. A diferença simétrica contém elementos que estão presentes em apenas um dos conjuntos, excluindo aqueles que estão em ambos.
#os conjuntos (sets) em Python são estruturas de dados que armazenam coleções de elementos únicos e não ordenados.

def segundo_maior(lista):
    # Remover duplicatas
    lista = list(set(lista))
    
    if len(lista) < 2:
        return "A lista não contém pelo menos dois elementos."

    # Ordenar em ordem decrescente
    lista.sort(reverse=True)

    # Retornar o segundo elemento (segundo maior valor)
    return lista[1]

#Remover duplicatas da lista para garantir que não haja números repetidos. Você pode fazer isso convertendo a lista em um conjunto e, em seguida, novamente em uma lista.
#Ordenar a lista em ordem decrescente (do maior para o menor).
#Acessar o segundo elemento da lista ordenada para obter o segundo maior valor.

def ordenar_pessoas_por_nome(lista_de_pessoas):
    # Usamos a função sorted para ordenar a lista de acordo com o nome da pessoa.
    lista_ordenada = sorted(lista_de_pessoas, key=lambda pessoa: pessoa[0])

    return lista_ordenada

#lista_ordenada = sorted(lista_de_pessoas, key=lambda pessoa: pessoa[0]): Usamos a função sorted() para ordenar a lista lista_de_pessoas. A chave de ordenação é definida por key=lambda pessoa: pessoa[0], que extrai o primeiro elemento (o nome) de cada tupla para fins de ordenação.

def encontrar_maior_e_menor(lista):
    if not lista:
        return None, None  # Retorna None se a lista estiver vazia

    maior = lista[0]  # Inicializa o maior com o primeiro elemento da lista
    menor = lista[0]  # Inicializa o menor com o primeiro elemento da lista

    for numero in lista:
        if numero > maior:
            maior = numero  # Atualiza o maior se um número maior for encontrado
        elif numero < menor:
            menor = numero  # Atualiza o menor se um número menor for encontrado

    return maior, menor

#usar uma abordagem que percorre a lista uma vez e mantém o controle do maior e do menor número à medida que itera pelos elementos
#percorremos a lista de números com um loop for. Para cada número na lista, comparamos o número com o maior e o menor atuais. Se um número maior for encontrado, atualizamos a variável maior. Se um número menor for encontrado, atualizamos a variável menor.
#Por fim, a função retorna o valor de maior e menor como uma tupla.
#A linha return None, None é usada para retornar uma tupla com dois valores None no caso em que a lista fornecida como entrada está vazia. Isso é feito para indicar que não foi encontrado nem o maior nem o menor valor na lista, já que não há elementos para avaliar.

def ler_arquivo_csv(caminho_do_arquivo, num_linhas=None):
    # Lê o arquivo CSV e retorna um DataFrame
    if num_linhas is None:
        return pd.read_csv(caminho_do_arquivo)
    else:
        return pd.read_csv(caminho_do_arquivo, nrows=num_linhas)
    
    #https://saturncloud.io/blog/how-to-install-pandas-into-visual-studio-code/
    #https://pythonacademy.com.br/blog/importar-csv-no-pandas


import pandas as pd

def selecionar_coluna_e_filtrar_linhas(caminho_do_arquivo, nome_da_coluna, condicao):
    # Lê o arquivo CSV em um DataFrame
    df = pd.read_csv(caminho_do_arquivo)

    # 1. Selecionar uma coluna específica (nome_da_coluna):
    coluna_selecionada = df[nome_da_coluna]

    # 2. Filtrar linhas com base na condição fornecida:
    linhas_filtradas = df.loc[condicao]

    return coluna_selecionada, linhas_filtradas

#O método loc é útil quando você deseja selecionar linhas com base em rótulos de índice ou condições de coluna específicas, o que é mais apropriado para a leitura de dados de um arquivo CSV. Portanto, para operações de seleção de coluna e filtragem, a notação de colchetes e o método loc são as abordagens mais adequadas.

# Função para detectar valores ausentes
def detectar_valores_ausentes(caminho_do_arquivo):
    df = pd.read_csv(caminho_do_arquivo)
    return df.isna()

# Função para remover linhas com valores ausentes
def remover_linhas_valores_ausentes(caminho_do_arquivo):
    df = pd.read_csv(caminho_do_arquivo)
    return df.dropna()

# Função para preencher valores ausentes com um valor específico (0 por padrão)
def preencher_valores_ausentes(caminho_do_arquivo, valor_preenchimento):
    df = pd.read_csv(caminho_do_arquivo)
    return df.fillna(valor_preenchimento)

#https://medium.com/data-hackers/tratamento-e-transforma%C3%A7%C3%A3o-de-dados-nan-uma-vis%C3%A3o-geral-e-pr%C3%A1tica-54efa9fc7a98

# =================

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")

for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row},{col}]', (0.5, 0.5), transform=axs[row, col].transAxes, ha='center', va='center', fontsize=18, color='darkgrey')

fig.suptitle('plt.subplots()')

# =================

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

