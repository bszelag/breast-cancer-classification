from sklearn.naive_bayes import GaussianNB


# TODO: make naive_bayes configurable
def get_trained_model(data, target):
    model = GaussianNB()
    model.fit(data, target)
    return model
