def multiply(a, b):
    try:
        result = int(str(a)[-1]) * int(str(b)[-1])
        return str(result)
    except ValueError as ve:
        return 'Input numbers are not integers'
    except Exception as e:
        return str(e)

import unittest

class Test(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)

if __name__ == '__main__':
    unittest.main()