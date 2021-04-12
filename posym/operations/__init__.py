import numpy as np
from itertools import permutations


class Operation:
    def __init__(self, label):

        self._label = label
        self._measure_mode = []
        self._measure_coor = []

    def get_permutation(self, operation, coordinates, symbols):
        operated_coor = np.dot(operation, coordinates.T).T

        coor_list = []
        permu_list = []
        for iter in permutations(enumerate(operated_coor), len(operated_coor)):

            iter_num = [c[0] for c in iter]

            if not (np.array(symbols)[iter_num] == symbols).all():
                continue

            permu_list.append(iter_num)
            permu_coor = np.array([c[1] for c in iter])

            coor_list.append(np.average(np.linalg.norm(np.subtract(coordinates, permu_coor), axis=0)))

        return np.min(coor_list), permu_list[np.nanargmin(coor_list)]

    def get_coor_measure(self, coordinates):
        #  normalization

        if len(self._measure_coor) == 0:
            raise Exception('Measure coord not calculated')

        sum_list = []
        for r1 in coordinates:
            for r2 in coordinates:
                subs = np.subtract(r1, r2)
                sum_list.append(np.dot(subs, subs))
        d = np.average(sum_list)

        return np.average(self._measure_coor) / d

    @property
    def label(self):
        return self._label
