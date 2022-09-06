import random
import words
import ascii


def imprimr(lista):
    palavra = ''
    for _ in lista:
        palavra += _
    return print(palavra)


display = []
palavra_escolhida = random.choice(words.lista_palavras)

for char in palavra_escolhida:
    display.append('_')
vidas = 6
fim_de_jogo = False
while not fim_de_jogo:
    letra = input('Advinhe uma letra: ').lower()
    if letra in display:
        print(f'Você já advinhou a letra {letra.upper()}. Tente uma diferente!')
    for posicao in range(len(palavra_escolhida)):
        if palavra_escolhida[posicao] == letra:
            display[posicao] = letra
    if letra not in palavra_escolhida:
        print(f'Você digitou {letra.upper()}. Letra não existe nessa palavra. Perdeu uma vida!')
        vidas -= 1
        if vidas == 0:
            fim_de_jogo = True
            print('Game Over!')
    imprimr(display)
    if '_' not in display:
        fim_de_jogo = True
        print('Você venceu!')
    print(ascii.stages[vidas])
