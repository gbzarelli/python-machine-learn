from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

X, Y = carregar_acessos()

treino_X = X[:90]
treino_Y = Y[:90]

teste_X = X[-9:]
teste_Y = Y[-9:]

modelo = MultinomialNB()
modelo.fit(treino_X, treino_Y)

resultado = modelo.predict(teste_X)
diferencas = resultado - teste_Y
acertos = [d for d in diferencas if d == 0]

quantidade_acertos = len(acertos)
quantidade_dados = len(teste_X)

porcentagem_acertos = 100.0 * quantidade_acertos / quantidade_dados

print(porcentagem_acertos, "% de acertos")
