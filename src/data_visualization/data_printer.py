

def get_classification_accuracy(predicted_values, true_values, mapper=lambda x: 1 if x == 4 else 0):

    if len(predicted_values) != len(true_values):
        return

    predicted_values = list(map(mapper, predicted_values))
    true_values = list(map(mapper, true_values))

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for i in range(len(true_values)):
        if true_values[i] == predicted_values[i] == 1:
            tp += 1
        if true_values[i] == predicted_values[i] == 0:
            tn += 1
        if true_values[i] == 1 and predicted_values[i] == 0:
            fn += 1
        if true_values[i] == 0 and predicted_values[i] == 1:
            fp += 1

    num_of_samples = tp + fp + tn + fn
    tp = tp/num_of_samples * 100
    fp = fp/num_of_samples * 100
    tn = tn/num_of_samples * 100
    fn = fn/num_of_samples * 100

    return {"tp": tp, "fp": fp, "tn": tn, "fn": fn}


def print_confusion_matrix(classification_accuracy):

    print("true positive: {0:2.2f}%".format(classification_accuracy["tp"]))
    print("true negative: {0:2.2f}%".format(classification_accuracy["tn"]))
    print("false positive: {0:2.2f}%".format(classification_accuracy["fp"]))
    print("false negative: {0:2.2f}%".format(classification_accuracy["fn"]))


def print_confusion_matrix_from_data(predicted_values, true_values, mapper=lambda x: 1 if x == 4 else 0):

    print_confusion_matrix(get_classification_accuracy(predicted_values, true_values, mapper))

