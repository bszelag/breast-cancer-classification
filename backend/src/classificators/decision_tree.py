from sklearn import tree

model = None


# TODO: make this configurable
def train_model(data, target):
    global model
    model = tree.DecisionTreeClassifier()
    model.fit(data, target)
