from sklearn import tree

model = None
mask_ = None


def train_model(data, target, mask, **kwargs):
    global model
    global mask_

    mask_ = mask

    model = tree.DecisionTreeClassifier(**kwargs)
    model.fit(data, target)


def predict(data):

    if mask_ is not None:
        data = data[..., mask_]

    return model.predict(data)
