with open ('glpi.txt' , encoding="utf8") as file_object:
    contents = file_object.read()
    linhas = file_object.readlines()
    print(contents)

    for linha in linhas:
        print(line.rstrip())

filename = 'programacao.txt'

with open(filename, 'r+') as file_object:
    file_object.write('Eu amo programacao')

#Escreva um programa que pergunte o nome ao usuário. Quando ele responder, escreva o nome em um arquivo chamado guest.txt.

while True:
    nome = input('Qual o seu nome? ou digite "sair" para sair. ')
    if nome == 'sair':
        break
    idade = input('Qual a sua idade? ')
    with open('guest.txt', 'a') as file_object:
        file_object.write(f'Seja bem-vindo(a)!\n {nome} voce tem {idade} anos.\n')
