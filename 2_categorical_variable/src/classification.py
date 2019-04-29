from loader import load
from sklearn.naive_bayes import MultinomialNB

X, Y = load()

training_percent = 0.9

len_training = int(training_percent * len(X))
len_test = len(X) - len_training

X_training = X[:len_training]
Y_training = Y[:len_training]

X_test = X[-len_test:]
Y_test = Y[-len_test:]

model = MultinomialNB()
model.fit(X_training, Y_training)

result = model.predict(X_test)
diffs = result - Y_test
hits = [d for d in diffs if d == 0]

hits_length = len(hits)

percent_success_hits = 100.0 * hits_length / len_test

print(percent_success_hits, "% of hits")
