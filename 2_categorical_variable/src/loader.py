import csv
import pandas as pd  # pd as 'Python data analise'


def load_manually():
    X = []  # Dados
    Y = []  # Marcacoes

    file = open('cursos.csv', "r")
    reader = csv.reader(file)

    next(reader)  # Skip the first line

    # home,search,logged,comprou
    for home, search, logged, purchased in reader:
        dado = [int(home), search, int(logged)]
        X.append(dado)
        Y.append(int(purchased))

    return X, Y


def load_data_frame():
    # df as 'Data Frame'
    df = pd.read_csv('cursos.csv')
    return df


def load():
    # df as 'Data Frame'
    df = load_data_frame()

    X_df = df[['home', 'busca', 'logado']]
    Y_df = df['comprou']

    Xdummies_df = pd.get_dummies(X_df)  # Using when have categorical variables

    # Here I don't use 'get_dummies' because dont have categorical variable, and, in this case,
    # if I use 'get_dummies' the method returns two columns with the correct values in the column position 1;
    # - Like 'get_dummies()[1], unnecessary
    Ydummies_df = Y_df

    return Xdummies_df.values, Ydummies_df.values
