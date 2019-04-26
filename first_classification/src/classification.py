from loader import load
from sklearn.naive_bayes import MultinomialNB

X, Y = load()

trainingX = X[:90]
trainingY = Y[:90]

testX = X[-9:]
testY = Y[-9:]

model = MultinomialNB()
model.fit(trainingX, trainingY)

result = model.predict(testX)
diffs = result - testY
hits = [d for d in diffs if d == 0]

hitsLength = len(hits)
dataLength = len(testX)

percentage = 100.0 * hitsLength / dataLength

print(percentage, "% of hits")
