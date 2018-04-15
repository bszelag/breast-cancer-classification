from sklearn import tree


# TODO: make this configurable
def get_trained_model(data, target):
    model = tree.DecisionTreeClassifier()
    model.fit(data, target)
    return model

