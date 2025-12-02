def get_difference(li1, li2):
    try:
        if not all(isinstance(x, int) for x in li1) or not all(isinstance(x, int) for x in li2):
            raise ValueError("Input lists must only contain integer elements")
        if not li1 or not li2:
            raise ValueError("Input lists cannot be empty")

        diff_list = [x for x in li1 if x not in li2]
        return diff_list
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]), [10, 20, 30, 15])

if __name__ == '__main__':
    unittest.main()