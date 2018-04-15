import numpy as np
from sklearn.naive_bayes import GaussianNB


def get_trained_model(data, target):
    model = GaussianNB()
    model.fit(data, target)
    return model
