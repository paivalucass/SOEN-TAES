def remove_odd(l):
    if len(l) == 0:
        raise ValueError("Input list is empty")

    if all(num % 2 != 0 for num in l):
        raise ValueError("Input list does not contain any even numbers")

    numbers = [num for num in l if num % 2 == 0]
    return numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd([1,2,3]), [2])

if __name__ == '__main__':
    unittest.main()