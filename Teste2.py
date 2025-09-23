class Dados():
        def __init__(self, dados):
            self.BancoDados = dados

        def Imprimir(self):
            for p, v in enumerate(self.BancoDados):
                print(f'{v}')

def main():
    dados1 = ['Carlos', 'Kadu', 'Maverick']
    banco1 = Dados(dados1)
    banco1.Imprimir()

# parte principal
if __name__ == "__main__":
    main()