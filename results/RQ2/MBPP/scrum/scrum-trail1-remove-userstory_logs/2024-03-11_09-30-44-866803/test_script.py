def multiply_num(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    product = 1
    for num in numbers:
        product *= num

    result = product / len(numbers)
    return result
import unittest

class Test(unittest.TestCase):
    def test_multiply_num(self):
        self.assertAlmostEqual(multiply_num((8, 2, 3, -1, 7)), -67.2, delta=0.001)

if __name__ == '__main__':
    unittest.main()