# Módulos.
from random import randint
""" Módulo para gerar números aleatórios. """
from time import sleep
""" Módulo para aguardar. """

# Variáveis.
lista = list()
""" Lista para armazenar os números gerados. """
jogos = list()
""" Lista para armazenar os jogos gerados. """

# Titulo do programa.
print('-' * 30)
print('         MEGA SENA         ')
print('-' * 30)
""" Printa o título do programa. """

# Pede para o usuário quantos jogos serão gerados.
quantidade = int(input('Quantos bilhetes serão gerados? '))
total = 1
""" Variável para armazenar a quantidade de jogos. """

# Loop para gerar os jogos.
while total <= quantidade:
    contador = 0
    """ Variável para armazenar a contagem. """
    while True:
        """ Loop para gerar os números. """
        numero = randint(1, 60)
        """ Variável para armazenar o número gerado. """
        if numero not in lista:
            """ Verifica se o numero ja existe na lista. """
            lista.append(numero)
            """ Adiciona o numero na lista. """
            contador += 1
            """ Conta o numero adicionado. """
        if contador >= 6:
            """ Verifica se ja existe 6 números. """
            break
            """ Sai do loop. """
    lista.sort()
    """ Ordena a lista. """
    jogos.append(lista[:])
    """ Adiciona a lista na lista de jogos. """
    lista.clear()
    """ Limpa a lista. """
    total += 1
