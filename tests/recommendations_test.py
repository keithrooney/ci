import unittest

from ci import recommendations


class TestMath(unittest.TestCase):

    def test_euclidean_distance(self):
        self.assertEqual(0.894427191, round(recommendations.euclidean_distance((4.5, 1), (4, 2)), 9))

    def test_pearsons_correlation(self):
        self.assertEqual(0.162918477, round(recommendations.pearsons_correlation([4.1, 3, 5], [1, 2, 5]), 9))
