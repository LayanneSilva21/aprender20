from carro import Car

meu_novo_carro = Car('Audi', 'a4', '2016')
print(meu_novo_carro.get_descritive_name())

meu_novo_carro.odometer_reading = 23
meu_novo_carro.read_odometer()

print(bin(0b1100<< 4))