import numbers

import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

class MyMixins:

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.data:
                file.write(' '.join(map(str, row)) + '\n')

    def __str__(self):
        return str(self.data)

    @property
    def shape(self):
        return self.data.shape

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    def get_element(self, i, j):
        return self.data[i, j]

    def set_element(self, i, j, value):
        self.data[i, j] = value

class MixinMatrix(NDArrayOperatorsMixin, MyMixins):
    def __init__(self, data):
        self.data = np.array(data)

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (MixinMatrix,)):
                return NotImplemented
        inputs = tuple(x.data if isinstance(x, MixinMatrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.data if isinstance(x, MixinMatrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)