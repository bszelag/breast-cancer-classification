import src.data_preparation.data_loader as dl
import src.classificator.naive_bayes as nb

data, target, ids = dl.read_file("data/train.data")
model = nb.get_trained_model(data, target)

#TODO guess statistics
test_data, target, ids = dl.read_file("data/test.data")
predicted = model.predict(data)
print(predicted)

