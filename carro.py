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