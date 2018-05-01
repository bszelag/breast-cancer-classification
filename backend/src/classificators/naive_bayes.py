from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB

model = None


def train_model(data, target, **kwargs):
    global model

    if model is not None and kwargs["dist"] == "MultinominalNB":
        model = MultinomialNB()
    else:
        model = GaussianNB()

    model.fit(data, target)
