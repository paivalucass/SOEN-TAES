def smallest_num(xs):
    if len(xs) == 0:
        raise ValueError("Error: Empty list provided")
    elif len(xs) == 1:
        return xs[0]
    else:
        try:
            int_list = [int(x) for x in xs]
            return min(int_list)
        except ValueError:
            raise ValueError("Error: Non-numeric values found in the input list")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

if __name__ == '__main__':
    unittest.main()