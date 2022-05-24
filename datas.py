

class Data:

    def __init__(self, dia, mes, ano):
        self.data = [dia, mes, ano]

    def formatada(self):
        print(f'{self.data[0]}/{self.data[1]}/{self.data[2]}')