""""
Desenvolva um jogo da forca em Python, no qual o programa escolhe aleatoriamente uma palavra secreta de um conjunto pré-definido. O jogador deve tentar adivinhar a palavra digitando letras. Se a letra estiver na palavra secreta, ela deve ser revelada nas posições corretas. Caso contrário, o jogador perde uma vida. O jogo continua até que o jogador adivinhe corretamente a palavra secreta ou perca todas as vidas. O número máximo de vidas deve ser definido pelo programador. O jogo deve exibir uma “representação” da forca conforme o jogador erra letras. Ao final do jogo, o programa deve informar se o jogador venceu ou perdeu, e perguntar se deseja jogar novamente. 
"""
import os
import requests
import random

url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
response = requests.get(url)
palavras = response.text.split('\n')

secreta = random.choice(palavras).upper()
palavra = '_' * len(secreta)
chances = 5
letras_digitadas = ''

print('-=' * 20)
print('JOGO DA FORCA')
print('-=' * 20)

print(palavra)

while chances > 0:
    letra = input('Escolha uma letra: ').upper()

    if letra in letras_digitadas:
        print('Você já digitou essa letra. Tente novamente.')
        continue

    letras_digitadas += letra

    if letra in secreta:
        nova_palavra = ''
        for i in range(len(secreta)):
            if secreta[i] == letra:
                nova_palavra += letra
            else:
                nova_palavra += palavra[i]
        palavra = nova_palavra

        print('Letra correta!')
        print(palavra)

        if palavra == secreta:
            print('Parabéns! Você acertou a palavra secreta:', secreta)
            break
    else:
        chances -= 1
        print('Letra incorreta! Você tem', chances, 'chance(s) restante(s).')

        if chances == 0:
            print('Game Over! A palavra secreta era:', secreta)



    
