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
