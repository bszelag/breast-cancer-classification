import numpy as np
from sklearn.feature_selection import SelectKBest, chi2


def read_file(file, with_target=True):
    if isinstance(file, str):
        with open(file, 'r') as f:
            file = f.read()

    file = [line for line in file if '?' not in line]
    data = np.loadtxt(file, delimiter=',')

    def float_to_str(num):
        return ('%.15f' % num).rstrip('0').rstrip('.')

    target = None
    ids = [float_to_str(sample_name) for sample_name in data[:, 0]]
    data = np.delete(data, np.s_[0], axis=1)

    if with_target:
        target = [sample_name for sample_name in data[:, -1]]
        data = np.delete(data, np.s_[-1], axis=1)

    return data, target, ids


def feature_selection(data, target):

    new_data = SelectKBest(chi2, k=5).fit(data, target)
    mask_selected = new_data.get_support()
    new_data = new_data.transform(data)
    return new_data, mask_selected
