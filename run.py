import src.data_preparation.data_loader as dl
import src.classificator.naive_bayes as nb
import src.data_visualization.data_printer as dp

data, target, ids = dl.read_file("data/train.data")
model = nb.get_trained_model(data, target)

test_data, target, ids = dl.read_file("data/test.data")
predicted = model.predict(test_data)

dp.print_confusion_matrix_from_data(predicted, target)

