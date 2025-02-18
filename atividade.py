names =['lais', 'maria', 'daniel']
message= (f'Olá que bom te conhecer ')
print(message + names[0].title())
print(message + names[1].title())
print(message + names[2].title())

motors = ['honda', 'suzuki', 'yamaha', 'bros']

motors.insert(2,'ducati')
del motors[1]
popped_motors = motors.pop()
motors.remove('honda')

prim_possui = motors.pop(0)

print(motors)
print(popped_motors)
print('A primeira motocicleta que eu tive foi uma ' + prim_possui.title() + '.\n')

#Pense em pelo menos três tipos de pizzas favoritas. Armazene os nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada pizza.

pizzas = ['baiana', 'quatro queijos', 'cogumelo', 'palmito', 'bolonhesa']
messages=(f'Gosto de pizza de ')

for pizza in pizzas:
    print(messages + pizza + '\n')

print('Eu realmente amo pizza pode ser de qualquer sabor... \n')
#print(pizzas)

#FUNÇÕES

def saudacao_usuario(username):
    print('Olá,' + username.title()+'!')

saudacao_usuario('laiane')
#Escreva uma função chamada display_message() que mostre uma frase informando a todos o que você está aprendendo neste capítulo. Chame a função e certifique-se de que a mensagem seja exibida corretamente.
def display_message():
    print('\nEstou aprendendo funções!!!!')

display_message()
#fim da função display_message

#Escreva uma função chamada favorite_book() que aceite um parâmetro title. A função deve exibir uma mensagem como Um dos meus livros favoritos é Alice no país das maravilhas. Chame a função e não
#se esqueça de incluir o título do livro como argumento na chamada da função.
def livro(title):
    print('\nMeu livro favorito é ' + title.title() +'!')

livro('Alice no pais das maravilhas')
#fim da função livro
def descricao_pet(animal_type, pet_name):
    print('Eu tenho um ' + animal_type + '.')
    print('Meu ' + animal_type+ ' se chama ' + pet_name.title() + '.')

descricao_pet('cachorro', 'pluma')
descricao_pet('cachorro', 'pluto')

def descricao_casa(tipo, cor='azul'):
    print('Em teresina eu tenho uma casa de ' + tipo+ ' na cor ' + cor+ '.')

descricao_casa('alvenaria', 'azul')
descricao_casa('barro', 'terra')

#classe (molde)
class Carro:
    #metodo(uma funcao que faz parte de uma classe)
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo

    #metodo(uma funcao que faz parte de uma classe)
    def exibir_informacoes(self):
        print(f'Este carro é um {self.marca} {self.modelo}')

#Funcao (receita)
def criar_carro(marca, modelo):
    return Carro(marca,modelo)

#objeto (brinquedo)
#instancia
meu_carro=criar_carro('Toyota', 'Corolla')
meu_carro.exibir_informacoes()

#funcao
def calcular_area_retangulo(largura, altura):
    return largura * altura

area= calcular_area_retangulo(10, 5)
print(f'A area do retangulo é {area}')

class Cachorro():
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

    def sit(self):    
        print(f'{self.nome.title()} esta sentado.')
        print(f'{self.nome.title()} tem {self.idade} anos.')

    def rolar(self):
        print(f'{self.nome.title()} rolou sobre o chao.')

meu_cachorro = Cachorro('Rex', 3)
meu_cachorro.sit()
meu_cachorro.rolar()

# Crie uma classe chamada Restaurant. O método __init__() de Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type.

class Restaurante():
    def __init__(self,nome, cozinha):
        self.nome = nome
        self.cozinha = cozinha

    def descricao_restaurante(self):
        print(f'O nome do restaurante é {self.nome.title()} e ele serve {self.cozinha}.')
    
    def abrir_restaurante(self):
        print(f'{self.nome.title()} está aberto.')

meu_restaurante = Restaurante('Churrascaria', 'Churrasco')
meu_restaurante.descricao_restaurante()
meu_restaurante.abrir_restaurante()

seg_restaurante = Restaurante('Pizzaria', 'pizzas')
seg_restaurante.descricao_restaurante()
seg_restaurante.abrir_restaurante()

ter_restaurante = Restaurante('Napolis', 'Massas')
ter_restaurante.descricao_restaurante()
ter_restaurante.abrir_restaurante()

class Usuario():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def descricao_usuario(self):
        print(f'Seu nome é {self.nome.title()} {self.sobrenome.title()} e sua idade é {self.idade} anos.')

    def saudacao(self):
        print(f'Olá, {self.nome.title()} {self.sobrenome.title()}! Seja bem-vindo(a)!')

meu_usuario = Usuario('Laiane', 'Silva', '32')
meu_usuario.descricao_usuario()
meu_usuario.saudacao()

pri_usuario = Usuario('Lais', 'Silva', '21')
pri_usuario.descricao_usuario()
pri_usuario.saudacao()

seg_usuario = Usuario('Maria', 'Sousa', '19')
seg_usuario.descricao_usuario()
seg_usuario.saudacao()

class Tenis():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.leitura = 23

    def descricao_tenis(self):
        nome_comp = str(self.marca) + ' ' + str(self.modelo) + ' ' + str(self.ano)
        return nome_comp.title()

    def leitura_tenis(self):
        print(f'Leitura do tenis: {self.leitura} cm')

    def auto_leitura(self, cm):
        if cm >= self.leitura:
            self.leitura = cm
        else:
            print(f'Voce não pode alterar a leitura abaixo de {cm}')
        

tenis1 = Tenis('nike', 'air max', '2000')
print(tenis1.descricao_tenis())

#tenis1.leitura = 23
#tenis1.leitura_tenis()

tenis1.auto_leitura(30)
tenis1.leitura_tenis()

class Car():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometer_reading = 0

    def get_descritive_name(self):
        long_name = f'{self.marca} {self.modelo} {self.ano}'
        return long_name.title()

    def read_odometer(self):
        print(f'Este carro tem {self.odometer_reading} quilometros rodados.')

    def update_odometer(self, km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print('Voce não pode retroceder o odometro.')

    def increment_odometer(self, km):
        self.odometer_reading += km

class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'Esta carro tem uma bateria de {self.battery_size} kwh.')

    def get_range(self):
        if self.battery_size ==70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        mensagem = f'Este carro pode percorre {range} quilometros com essa bateria.'
        mensagem += f' Com carga completa'
        print(mensagem)


class EletricCar(Car):
    def __init__(self, marca, modelo, ano, battery_size = 70):
        super().__init__(marca, modelo, ano)
        self.battery = Battery()
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'Este carro tem uma bateria de {self.battery_size} kwh.')

    def fill_gas_tank(self):
        print(f'Este carro não tem tanque de gasolina.')


meu_tesla = EletricCar('Tesla', 'roadster', '2020')
print(meu_tesla.get_descritive_name())
meu_tesla.describe_battery()
meu_tesla.battery.get_range()

class Porta():
    def __init__(self, cor, largura, altura, fechadura):
        self.cor = cor
        self.largura = largura
        self.altura = altura
        self.fechadura = fechadura
    
    def descricao_porta(self):
        print(f'Esta porta tem a cor {self.cor} e tem {self.largura} cm de largura e {self.altura} cm de altura e uma fechadura do tipo {self.fechadura}')
    
    def abrir_porta(self):
        print('A porta foi aberta.')

    def fechar_porta(self):
        print('Por favor ao sair, feche a porta.')


porta1 = Porta('Amarelo', '30', '90', 'alumunio')
porta1.descricao_porta()
porta1.abrir_porta()
porta1.fechar_porta()


porta2 = Porta('Cinza', '40', '100', 'cromada')
porta2.descricao_porta()
porta2.abrir_porta()
porta2.fechar_porta()

class MetalicPorta(Porta):
    def __init__(self, cor, largura, altura, fechadura, tipo):
        super().__init__(cor, largura, altura, fechadura)
        self.tipo = tipo

    def get_descricao_tipo(self):
        return f'Esta é uma porta feita de {self.tipo}'


porta_metal = MetalicPorta('Cinza', '50', '100', 'Cromada', 'Vidro')
print(porta_metal.get_descricao_tipo())

class LateralPorta(Porta):
    def __init__(self, cor, largura, altura, fechadura, forma):
        super().__init__(cor, largura, altura, fechadura)
        self.forma = forma
    
    def get_descricao_forma(self):
        return f'Esta porta abre de forma {self.forma}'

porta_later = LateralPorta('fosca', '60', '120', 'cromada', 'lateral')
print(porta_later.get_descricao_forma())

class Roupa():
    def __init__(self, marca, tamanho, cor):
        self.marca = marca
        self.tamanho= tamanho
        self.cor = cor

    
    def descricao_roupa(self):
        print(f'Essa roupa é da marca {self.marca}, no tamanho {self.tamanho} e da cor {self.cor}')

    def vendida(self):
        print(f'Essa roupa já foi vendida')

    def amassa_roupa(self):
        print(f'Essa roupa não amassa!')

roupa1 = Roupa('Gucci', 'g', 'Azul')
roupa1.descricao_roupa()
roupa1.vendida()
roupa1.amassa_roupa()

class Janela():
    def __init__(self, marca, tamanho, modelo):
        self.marca = marca
        self.tamanho= tamanho
        self.modelo = modelo
    
    def descricao_janela(self):
        print(f'Essa janela é da marca {self.marca}, feita no tamanho {self.tamanho} e na modelo {self.modelo}')

    def abrir_janela(self):
        print(f'Esta janela está aberta!')

    def cortina(self):
        print(f'Está janela tem uma bela cortina!')
    

janela1= Janela('tramontina', '80 x 60', 'quadradro')
janela1.descricao_janela()
janela1.abrir_janela()
janela1.cortina()

class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def info(self):
        print(f'Nome : {self.titular}')
        print(f'Saldo: {self.saldo}')
      
    def info_saldo(self):
        print(f'Olá Sr(a) {self.titular}, saldo disponivel R$ {self.saldo:.2f}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saldo indiponivel! Informe um outro valor!!!')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso')

    def depositar(self, quantia):
        self.saldo += quantia
        print(f'Deposito de R${quantia:.2f} realizado com sucesso!')


novo_user= ContaBancaria(input ('Digite o nome do titular: '), float(input('Informe o saldo: R$ ')))
novo_user.info()
novo_user.info_saldo()
valor_saque = float(input(f'Digite o valor a ser sacado: R$ '))
novo_user.sacar(valor_saque)
novo_user.info_saldo()
valor_deposito = float(input(f'Digite o valor a ser depositado: R$'))
novo_user.depositar(valor_deposito)
novo_user.info_saldo()

def velocidade_media():
    distancia = float(input(f'Informe a distancia percorrida:'))
    tempo = float(input(f'Informe o tempo gasto:'))
    velocidade = distancia / tempo
    return velocidade

print(velocidade_media())

def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": float(saldo), "limite": float(limite)}
    return conta

def depositar(conta, valor):
    conta['saldo'] += valor

def sacar(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f'Numero da conta: {conta["numero"]}, Titular: {conta["titular"]}, Saldo: {conta["saldo"]}, Limite: {conta["limite"]}')

# Criando a conta com os parâmetros necessários
conta = criar_conta('123', 'Laiane Pereira', 1000, 1000)

# Realizando operações na conta
depositar(conta, 100)
sacar(conta, 50)
extrato(conta)

