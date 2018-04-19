from sklearn.naive_bayes import GaussianNB

model = None


# TODO: make naive_bayes configurable
def train_model(data, target):
    global model
    model = GaussianNB()
    model.fit(data, target)


