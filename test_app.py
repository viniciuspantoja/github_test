from math import pi
from unittest import TestCase, main

from app import circles


class PyramidTests(TestCase):

    def test_circle(self):
        # test cases where r >= 0
        self.assertEqual(circles(0), 0)
        self.assertEqual(circles(1), pi)
        self.assertEqual(circles(2), pi * (2 **2))

    def test_values(self):
        # Let's raise the error values where
        self.assertRaises(ValueError, circles, -2)

if __name__ == "__main__":
    main()
