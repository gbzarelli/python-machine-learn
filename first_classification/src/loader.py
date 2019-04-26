import csv


def load():
    X = []  # Dados
    Y = []  # Marcacoes

    file = open('access.csv', "r")
    reader = csv.reader(file)

    next(reader)  # Skip the first line

    for home, howToWork, contact, purchased in reader:
        dado = [int(home), int(howToWork), int(contact)]
        X.append(dado)
        Y.append(int(purchased))

    return X, Y
