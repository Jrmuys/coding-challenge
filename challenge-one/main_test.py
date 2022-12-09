import unittest
# Import the function to be tested
from main import is_prime


class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        # Test for prime numbers
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(11), True)

    def test_non_prime_numbers(self):
        # Test for non-prime numbers
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(8), False)


if __name__ == "__main__":
    unittest.main()
