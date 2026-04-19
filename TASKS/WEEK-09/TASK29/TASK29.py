import numpy
from sklearn import linear_model


# Build training data:
# class 0 -> numbers from 10 to 50
# class 1 -> numbers from 51 to 100
class_0 = list(range(10, 51))
class_1 = list(range(51, 101))

X = numpy.array(class_0 + class_1).reshape(-1, 1)
y = numpy.array([0] * len(class_0) + [1] * len(class_1))

logr = linear_model.LogisticRegression()
logr.fit(X, y)

numbers_to_predict = numpy.array([34, 77]).reshape(-1, 1)
predicted = logr.predict(numbers_to_predict)

for number, label in zip(numbers_to_predict.flatten(), predicted):
    print(f"{number} -> {label}")
