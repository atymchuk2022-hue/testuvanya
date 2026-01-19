import unittest
from main import triangle_area


class TestTriangleArea(unittest.TestCase):

    def test_correct_formula(self):
        self.assertEqual(triangle_area(10, 5), 25)
        self.assertEqual(triangle_area(6, 4), 12)

    def test_zero_values(self):
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(5, 0), 0)
        self.assertEqual(triangle_area(0, 0), 0)

    def test_negative_values(self):
        self.assertEqual(triangle_area(-3, 5), 0)
        self.assertEqual(triangle_area(3, -5), 0)


if __name__ == "__main__":
    unittest.main()
