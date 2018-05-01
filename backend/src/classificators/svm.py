from sklearn import svm

model = None


def train_model(data, target, **kwargs):
    global model
    model = svm.SVC(**kwargs)
    model.fit(data, target)
