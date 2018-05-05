from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB

model = None
mask_ = None


def train_model(data, target, mask, **kwargs):

    global model
    global mask_

    mask_ = mask

    if kwargs is not None and "dist" in kwargs and kwargs["dist"] == "MultinominalNB":
        model = MultinomialNB()
    else:
        model = GaussianNB()

    model.fit(data, target)


def predict(data):

    if mask_ is not None:
        data = data[..., mask_]

    return model.predict(data)

