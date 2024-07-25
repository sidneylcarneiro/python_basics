from time import sleep
from random import randint
import os

# Função para limpar a tela
def limpar_tela():
    # Se o sistema operacional for Windows, usa 'cls', senão usa 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

# String original
h = "Hello World"
h2 = ""  # String inicial
cont = 0  # Contador para adicionar caracteres a h2
timer = 0.15  # Tempo de espera entre impressões

# Loop infinito para repetir o processo
while True:

    # Verifica se h2 já atingiu a string completa 'Hello World'
    if h2 == h:
        break  # Sai do loop se h2 for igual a h

    # Parte 1: Imprime cada caractere de h individualmente com o prefixo h2
    for char in h:
        print(f"\033[1;{randint(31, 37)};{randint(41, 47)}m", f"{h2 + char:^15}", f"\033[m", flush=True)
        sleep(timer)
        # Limpa a tela antes de cada iteração
        limpar_tela()

    # Parte 2: Adiciona o próximo caractere de h a h2, se ainda não completou
    if cont < len(h):
        h2 += h[cont]
        cont += 1

print(f"\033[1;{randint(31, 37)};{randint(41, 47)}m", f"{h2:^15}", f"\033[m", flush=True)
