atletas = [
    ["Maria Silva", 1.75, 65],
    ["João Santos", 1.80, 72],
    ["Ana Pereira", 1.68, 58],
    ["Pedro Oliveira", 1.92, 85],
    ["Carlos Lima", 1.85, 78],
    ["Beatriz Souza", 1.70, 60],
    ["Fernanda Costa", 1.62, 55],
    ["Lucas Almeida", 1.88, 82],
    ["Rafaela Gomes", 1.74, 63],
    ["Gustavo Ferreira", 1.90, 88],
    ["Larissa Rocha", 1.66, 57],
    ["Henrique Nunes", 1.83, 76],
    ["Juliana Martins", 1.72, 59],
    ["Ricardo Carvalho", 1.86, 80],
    ["Sofia Alves", 1.64, 54],
    ["Matheus Ribeiro", 1.89, 84],
    ["Camila Duarte", 1.69, 61],
    ["Gabriel Monteiro", 1.77, 73],
    ["Eduarda Farias", 1.71, 62],
    ["Thiago Mendes", 1.84, 79],
]

for atleta in atletas:
    print('Nome:' , atleta[0], '\nAltura:' , atleta[1], 'm','\nPeso:', atleta[2], 'Kg')


minha_tupla = atletas = [
    ("Maria Silva", 1.75, 65),
    ("João Santos", 1.80, 72),
    ('Ana Pereira', 1.68, 58), 
    ('Pedro Oliveira', 1.92, 85), 
    ('Carlos Lima', 1.85, 78), 
    ('Beatriz Souza', 1.7, 60), 
    ('Fernanda Costa', 1.62, 55), 
    ('Lucas Almeida', 1.88, 82), 
    ('Rafaela Gomes', 1.74, 63), 
    ('Gustavo Ferreira', 1.9, 88), 
    ('Larissa Rocha', 1.66, 57), 
    ('Henrique Nunes', 1.83, 76), 
    ('Juliana Martins', 1.72, 59), 
    ('Ricardo Carvalho', 1.86, 80), 
    ('Sofia Alves', 1.64, 54), 
    ('Matheus Ribeiro', 1.89, 84), 
    ('Camila Duarte', 1.69, 61), 
    ('Gabriel Monteiro', 1.77, 73), 
    ('Eduarda Farias', 1.71, 62), 
    ('Thiago Mendes', 1.84, 79),
]
minha_tupla = tuple(atletas)

print(minha_tupla)

# Lista para armazenar as tuplas
atletas_tuplas = []

# Loop para converter cada sublista em uma tupla
for atleta in atletas:
    nome = atleta[0]       # Nome do atleta
    altura = atleta[1]     # Altura do atleta
    peso = atleta[2]       # Peso do atleta
    atleta_tupla = (nome, altura, peso)  # Criação da tupla
    atletas_tuplas.append(atleta_tupla)  # Adição da tupla na nova lista

# Impressão da lista de tuplas
print(atletas_tuplas)






