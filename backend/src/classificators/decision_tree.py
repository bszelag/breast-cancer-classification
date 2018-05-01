from sklearn import tree

model = None


def train_model(data, target, **kwargs):
    global model
    model = tree.DecisionTreeClassifier(**kwargs)
    model.fit(data, target)
