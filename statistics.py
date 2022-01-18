import numpy as np
import pandas as pd

def calculate(digits):
    if len(digits) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        series = pd.Series(digits)
        n_array = np.array(digits).reshape((3, 3))
        matrix = pd.DataFrame(n_array)

        f_mean = series.mean()
        a1_mean = matrix.mean(axis=0).to_list()
        a2_mean = matrix.mean(axis=1).to_list()

        f_var = np.var(digits)
        a1_var = list(n_array.var(axis=0))
        a2_var = list(n_array.var(axis=1))

        f_std = np.std(digits)
        # check out why these values are wrong
        a1_std = list(n_array.std(axis=0))
        a2_std = list(n_array.std(axis=1))

        f_min = series.min()
        a1_min = matrix.min(axis=0).to_list()
        a2_min = matrix.min(axis=1).to_list()

        f_max = series.max()
        a1_max = matrix.max(axis=0).to_list()
        a2_max = matrix.max(axis=1).to_list()

        f_sum = series.sum()
        a1_sum = matrix.sum(axis=0).to_list()
        a2_sum = matrix.sum(axis=1).to_list()

        result = {
            'mean': [a1_mean, a2_mean, f_mean],
            'variance': [a1_var, a2_var, f_var],
            'standard deviation': [a1_std, a2_std, f_std],
            'max': [a1_max, a2_max, f_max],
            'min': [a1_min, a2_min, f_min],
            'sum': [a1_sum, a2_sum, f_sum]
        }
        return result

        






example = [0, 1, 2, 3, 4, 5, 6, 7, 8]
calculate(example)