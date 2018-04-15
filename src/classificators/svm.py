from sklearn import svm


# TODO: make svm configurable
def get_trained_model(data, target):
    model = svm.SVC()
    model.fit(data, target)
    return model
