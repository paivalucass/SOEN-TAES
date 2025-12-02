def dog_age(h_age):
    if h_age <= 0:
        return 'Invalid input'
    elif h_age == 1:
        return 15
    elif h_age == 2:
        return 24
    else:
        return (h_age - 2) * 4 + 24
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()