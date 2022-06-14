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
