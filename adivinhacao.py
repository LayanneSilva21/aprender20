numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')

    chute = int(input('Digite um numero: '))
    print('Você digitou:', chute)

    if chute == numero_secreto:
        print('Você acertou!')
        break
    elif chute > numero_secreto:
        print('Você Errou! O seu chute foi maior que o número secreto')
    else:
        print('Você Errou! O seu chute foi menor que o número secreto')

if rodada == total_de_tentativas:
    print('Suas tentativas acabaram! O número secreto era:', numero_secreto)