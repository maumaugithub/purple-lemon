import unittest
from parameterized import parameterized

from src.algorithms.array.product_of_array_except_self import ArrayProduct


class TestArrayProduct(unittest.TestCase):
    def setUp(self):
        baseline_nums = [1, 2, 3, 4, 5]
        self.product = ArrayProduct(nums=baseline_nums)
        self.expected = [120, 60, 40, 30, 24]

    def test_solution1_baseline(self):
        self.assertEqual(self.product.product_except_self(), self.expected)

    def test_solution2_baseline(self):
        self.assertEqual(self.product.product_except_self_o1(), self.expected)

    def test_solution3_baseline(self):
        self.assertEqual(self.product.product_except_self_poc(), self.expected)

    @parameterized.expand([
        ["baseline", [1, 2, 3, 4, 5], [120, 60, 40, 30, 24]],
        ["zero_proof", [-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]],
        ["example", [1, 2, 3, 4], [24, 12, 8, 6]],
    ])
    def test_solution_o1(self, test_name, given_nums, expected):
        product = ArrayProduct(nums=given_nums)
        calculated = product.product_except_self_poc()
        self.assertEqual(calculated, expected)
        print(f'{test_name} - {calculated}')


# if __name__ == '__main__':
#     unittest.main()
