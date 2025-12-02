def empty_dit(list1):
    if not all(isinstance(d, dict) for d in list1):
        raise TypeError("Input should be a list of dictionaries")

    for d in list1:
        if d:
            return False

    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_dit([{}, {}, {}]), True)

if __name__ == '__main__':
    unittest.main()