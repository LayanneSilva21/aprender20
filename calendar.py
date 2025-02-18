import calendar

class Collection:
    def __init__(self, titulo, page_start, length=1):
        self.titulo = titulo
        self.page_start = page_start
        self.page_end = page_start + length - 1
        self.items = []

    def __str__(self):
        return self.titulo

    def expande(self, by):
        self.page_end += by

    def add_item(self, marcador, nota, significado=None):
        """Adiciona um item ao registro mensal"""
        item = {
            'marcador': marcador,
            'nota': nota,
            'significado': significado
        }
        self.items.append(item)

class MesLongo(Collection):
    def __init__(self, mes, ano, page_start, length=2):
        super().__init__(f'{mes} {ano}', page_start, length)
        self.events = []

    def __str__(self):
        return f'{self.titulo} (Mes Longo)'

    def add_event(self, evento, date=None):
        """Registra um evento para a data fornecida (hoje por padrão)."""
        self.events.append({'evento': evento, 'date': date})

class FuturoLongo(Collection):
    def __init__(self, start_mes, page_start):
        super().__init__('Futuro Longo', page_start, 4)
        self.start = start_mes
        self.meses = [start_mes]

    def add_item(self, marcador, nota, significado=None, mes=None):
        """Adiciona um item ao log futuro para o mês especificado."""
        item = {
            'marcador': marcador,
            'nota': nota,
            'significado': significado,
            'mes': mes
        }
        self.items.append(item)

# Exemplo de uso
log = FuturoLongo('Janeiro 2025', 1)
log.add_item('•', 'Limpa o teclado', '!', 'Fevereiro 2025')
print(log.items)

mensal = MesLongo('Março', '2025', 9)
mensal.add_event('Reunião', '2025-03-15')
mensal.add_item('•', 'Concluir relatório')
print(mensal.events)
print(mensal.items)

to_read = Collection('Livros para ler', 1)
to_read.add_item('•', 'Ler "1984" de George Orwell')
print(to_read.items)


