import unittest

from chapter4 import maximum_subarray


class MaximumArrayTest(unittest.TestCase):
    test_cases = [([0, 1, -4, 3, -4], (3, 3, 3)),
                  ([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], (7, 10, 43))]

    def test_maximum_array(self):
        for (prices, expected_result) in self.test_cases:
            result = maximum_subarray.solve_for(prices)
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
