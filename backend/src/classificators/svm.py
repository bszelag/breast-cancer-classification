from sklearn import svm

model = None
mask_ = None


def train_model(data, target, mask, **kwargs):
    global model
    global mask_

    mask_ = mask
    model = svm.SVC(**kwargs)
    model.fit(data, target)


def predict(data):

    if mask_ is not None:
        data = data[..., mask_]

    return model.predict(data)
