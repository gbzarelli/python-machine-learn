import csv


def carregar_acessos():
    X = []  # Dados
    Y = []  # Marcacoes

    arquivo = open('acesso.csv', "r")
    leitor = csv.reader(arquivo)

    next(leitor)  # Skip the first line

    for home, como_funciona, contato, comprou in leitor:
        dado = [int(home), int(como_funciona), int(contato)]
        X.append(dado)
        Y.append(int(comprou))

    return X, Y
