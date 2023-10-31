import funcoes

print("==========================================================================")
print("Questão 01")
print("==========================================================================")
print("")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primos = funcoes.encontrar_primos_na_lista(numeros)
print("Números primos na lista:", primos)

print("")
print("==========================================================================")
print("Questão 02")
print("==========================================================================")
print("")

lista1 = [1, 2, 3, 4, 5, 7]
lista2 = [3, 4, 5, 6, 7]
result2 = funcoes.elementos_unicos(lista1, lista2)
print("Elementos presentes em uma única lista:",result2)

print("")
print("==========================================================================")
print("Questão 03")
print("==========================================================================")
print("")

numeros = [3, 7, 2, 10, 8, 7, 5]
segundo_maior_valor = funcoes.segundo_maior(numeros)
print("O segundo maior valor na lista é:", segundo_maior_valor)

print("")
print("==========================================================================")
print("Questão 04")
print("==========================================================================")
print("")

pessoas = [
    ("Bob", 25),
    ("Alice", 30),
    ("Eve", 22),
    ("David", 35),
    ("Charlie", 28)
]

lista_ordenada = funcoes.ordenar_pessoas_por_nome(pessoas)
print(lista_ordenada)

print("")
print("==========================================================================")
print("Questão 05")
print("==========================================================================")
print("")

numeros = [10, 5, 20, 3, 15, 30]
maior, menor = funcoes.encontrar_maior_e_menor(numeros)
print("Maior número:", maior)
print("Menor número:", menor)

print("")
print("==========================================================================")
print("Questão 06")
print("==========================================================================")
print("")

caminho_do_arquivo = './bandas.csv'
musicas_todas = funcoes.ler_arquivo_csv(caminho_do_arquivo,7)
print(musicas_todas)
musicas_head = funcoes.ler_arquivo_csv(caminho_do_arquivo)
print(musicas_head)
musicas_head = funcoes.ler_arquivo_csv(caminho_do_arquivo)
print(musicas_head.head())

print("")
print("==========================================================================")
print("Questão 07")
print("==========================================================================")
print("")

# Defina a condição corretamente
condicao = funcoes.ler_arquivo_csv(caminho_do_arquivo)['ano de lancamento'] > 2000

# Chame a função do módulo funcoes
coluna_selecionada, linhas_filtradas = funcoes.selecionar_coluna_e_filtrar_linhas(
    caminho_do_arquivo,
    nome_da_coluna='artista',
    condicao=condicao
)

print("Coluna selecionada:")
print(coluna_selecionada)
print("\nLinhas filtradas:")
print(linhas_filtradas)

print("")
print("==========================================================================")
print("Questão 08")
print("==========================================================================")
print("")

caminho_do_arquivo = './bandas_NaN.csv'

print("Valores ausentes:")
print(funcoes.detectar_valores_ausentes(caminho_do_arquivo))

print("\nDataFrame após remover linhas com valores ausentes:")
print(funcoes.remover_linhas_valores_ausentes(caminho_do_arquivo))

print("\nDataFrame após preencher valores ausentes com 0:")
print(funcoes.preencher_valores_ausentes(caminho_do_arquivo,0))

print("")
print("==========================================================================")
print("Questão 09")
print("==========================================================================")
print("")
print("Encontra-se dentro do arquivo funcoes.py")
print("")
print("==========================================================================")
print("Questão 10")
print("==========================================================================")
print("")
print("Encontra-se dentro do arquivo funcoes.py")
print("")
print("==========================================================================")