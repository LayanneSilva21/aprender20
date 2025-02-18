import random

print('*****************************************')
print('***Bem vindo ao jogo da Forca!***')
print('*****************************************')

def escolher_palavra():
    palavras = ['banana', 'macaco', 'laranja', 'uva']
    palavra_secreta = random.choice(palavras)
    return palavra_secreta

def jogar():
    palavra_secreta = escolher_palavra()
    letras_acertadas = ['_' for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print('O Jogo vai Começar......')

    while not enforcou and not acertou:
        chute = input('Qual a letra? ').upper()

        if len(chute) != 1 or not chute.isalpha():
            print('Digite apenas uma letra.')
            continue

        if chute in palavra_secreta.upper():
            for i, letra in enumerate(palavra_secreta.upper()):
                if chute == letra:
                    letras_acertadas[i] = letra
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

        print(' '.join(letras_acertadas))
        print(f'Erros: {erros}')

    if acertou:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
        print('A palavra era:', palavra_secreta)

jogar()

