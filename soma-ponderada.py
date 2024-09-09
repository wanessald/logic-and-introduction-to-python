import os
import platform

def input_notas():
    nota_A1 = float(input("Informe a nota A1: "))
    nota_A2 = float(input("Informe a nota A2: "))
    nota_A3 = float(input("Informe a nota A3: "))
    nota_A4 = float(input("Informe a nota A4: "))
    return [nota_A1, nota_A2, nota_A3, nota_A4]

def dados_pesos():
    peso_1 = 0.4
    peso_2 = 0.3
    peso_3 = 0.3
    return [peso_1, peso_2, peso_3]

def soma_ponderada_original(notas, pesos):
    soma = 0
    produto = []
    for nota, peso in zip(notas, pesos):
        produto = nota * peso
        soma += produto
    return soma

def soma_ponderada_substituindo(notas, pesos):
    nota_substitutiva = notas[-1]
    resultados = []
    for indice in range(3):   
        notas_temporarias = notas[:3].copy()
        notas_temporarias[indice] = nota_substitutiva
        soma_substituindo = soma_ponderada_original(notas_temporarias, pesos)
        resultados.append((indice + 1, soma_substituindo))
    return resultados

def extrair_soma(tupla):
    return tupla[1]
        
def comparar_soma_original_e_soma_substituindo(notas, pesos):
    soma_original = soma_ponderada_original(notas[:3], pesos)
    print(f"Soma ponderada original: {soma_original}")

    substituicoes = soma_ponderada_substituindo(notas, pesos)

    for posicao, soma_substituindo in substituicoes:
        print(f"Soma ponderada substituindo a nota A{posicao}: {soma_substituindo}")

    melhor_cenario = max(substituicoes, key=extrair_soma)
    if melhor_cenario[1] > soma_original:
        print(f"\nMelhor cenário para o aluno: Substituir a nota A{melhor_cenario[0]} resulta na maior soma ponderada: {melhor_cenario[1]}.")
    else:
         print(f"\nMelhor cenário para o aluno: Manter a nota A{melhor_cenario[0]} resulta na maior soma ponderada: {soma_original}.")

def main():
        system_name = platform.system()
        
        try:
            if system_name == 'Windows':
                os.system("cls")
            elif system_name in ['Linux', 'Darwin']:
                os.system("clear")
            else:
                print(f"Unsupported operating system: {system_name}")
        except Exception as e:
            print(f"An error occurred while trying to clear the terminal: {e}")     
        
        notas = input_notas()
        pesos = dados_pesos()
        comparar_soma_original_e_soma_substituindo(notas, pesos)

main()