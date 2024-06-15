import unittest
from src.fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_first_term(self):
        self.assertEqual(fibonacci(1), 0)

    def test_second_term(self):
        self.assertEqual(fibonacci(2), 1)

    def test_third_term(self):
        self.assertEqual(fibonacci(3), 1)

    def test_tenth_term(self):
        self.assertEqual(fibonacci(10), 34)

    def test_negative_term(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_zero_term(self):
        with self.assertRaises(ValueError):
            fibonacci(0)

    def test_large_term(self):
        self.assertEqual(fibonacci(50), 7778742049)


if __name__ == '__main__':
    unittest.main()
