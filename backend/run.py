# import src.data_preparation.data_loader as dl
# import src.classificators.naive_bayes as nb
# import src.data_visualization.data_printer as dp
# import src.classificators.svm as svm
# import src.classificators.decision_tree as tree

from src.backend import app

# # temp----------------------------------
# data, target, ids = dl.read_file("data/train.data")
# model = nb.get_trained_model(data, target)
# model2 = svm.get_trained_model(data, target)
# model3 = tree.get_trained_model(data, target)
#
# test_data, target, ids = dl.read_file("data/test.data")
# predicted = model.predict(test_data)
# predicted2 = model2.predict(test_data)
# predicted3 = model3.predict(test_data)
#
# print("Bayes--------------------")
# dp.print_confusion_matrix_from_data(predicted, target)
# print("SVM----------------------")
# dp.print_confusion_matrix_from_data(predicted2, target)
# print("Decision Tree------------")
# dp.print_confusion_matrix_from_data(predicted3, target)
# # ----------------------------------

app.run(host='0.0.0.0', port=5000, debug=True)
