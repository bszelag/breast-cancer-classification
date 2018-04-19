from sklearn import svm

model = None


# TODO: make svm configurable
def train_model(data, target):
    global model
    model = svm.SVC()
    model.fit(data, target)
