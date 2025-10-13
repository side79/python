from pytest import mark
# from unittest import TestCase
from solver import Solver, mul

@mark.parametrize(
    "values, expected_result",
    [
        ((3, 5), 15),
        ((1, 10), 10),
        ((1, 0), 0),
        ((4, 8), 32),
    ]
)
def test_mul(values, expected_result):
    res = mul(*values)
    assert res == expected_result

# class TestSolver(TestCase):
#     def test_add(self):
#         res = Solver.add(1, 2)
#         self.assertEqual(res, 3)

#         res = Solver.add(4, 5)
#         self.assertEqual(res, 9)

