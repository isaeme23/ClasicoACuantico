import unittest
import experiments as ex
import numpy as np
import matplotlib.pyplot as plt


class TestExperiments(unittest.TestCase):

    def test_Matrix_State(self):
        matrix = np.array([[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 1, 0, 0, 0, 1],[0, 0, 0, 1, 0, 0],[0, 0, 1, 0, 0, 0],[1, 0, 0, 0, 1, 0]])
        state = [6, 2, 1, 5, 3, 10]
        self.assertEqual(ex.Matrix_State(matrix, state, 1), [0, 0, 12, 5, 1, 9])

    def test_slitsP(self):
        slits, targets = 2, 5
        self.assertEqual(ex.slitsP(slits,targets), [0.0, 0.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2])

    def test_slitsCuantum(self):
        slits, targets = 2, 5
        self.assertEqual(ex.slitsCuantum(slits,targets), [0.0, 0.0, 0.0, 0.19999999999999993, 0.19999999999999993, 0.19999999999999993, 0.19999999999999993, 0.19999999999999993])

if __name__ == '__main__':
    unittest.main()

def barras(vec):
    v = []
    for i in range(len(vec)):
        v.append(i)
    plt.bar(v, vec)
    plt.show()


matrix = ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0])
state = [6, 2, 1, 5, 3, 10]
barras(ex.Matrix_State(matrix,state,1))
slits, targets = 2, 5
barras(ex.slitsP(slits,targets))
barras(ex.slitsCuantum(slits,targets))