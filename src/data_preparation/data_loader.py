import numpy as np


def read_file(file_name):
    if isinstance(file_name, str):
        with open(file_name, 'r') as f:
            file = f.read()
    else:
        file = file_name.read().decode('ascii')
        file = file.splitlines()
    file = [line for line in file if '?' not in line]
    data = np.loadtxt(file, delimiter=',')

    def float_to_str(num):
        return ('%.15f' % num).rstrip('0').rstrip('.')

    ids = [float_to_str(sample_name) for sample_name in data[:, 0]]
    data = np.delete(data, np.s_[0], axis=1)
    target = [sample_name for sample_name in data[:, -1]]
    data = np.delete(data, np.s_[-1], axis=1)
    return data, target, ids
