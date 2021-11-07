import unittest
from lecture_3.static_typing import sum_


class StaticTypeTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_(3, 2), 5)


if __name__ == '__main__':
    unittest.main()