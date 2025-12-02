def convert(numbers):
    try:
        if type(numbers) == int or type(numbers) == float:
            return (abs(numbers), 0.0)
        elif type(numbers) == complex:
            return (abs(numbers), cmath.phase(numbers))
        else:
            raise ValueError('Input should be a complex number or an array of complex numbers')
    except Exception as e:
        print(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert(1), (1.0, 0.0))

if __name__ == '__main__':
    unittest.main()