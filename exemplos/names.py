from name_fuction import get_formatted_name

print('Tecle "q" para sair.')
while True:
    first = input('\nPrimeiro nome: ')
    if first == 'q':
        break
    last = input('Sobrenome: ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f'\nOlá, {formatted_name}!')