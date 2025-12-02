def dog_age(h_age):
    if isinstance(h_age, int) and 0 < h_age < 150:
        if h_age == 1:
            return 7
        elif h_age < 15:
            return h_age * 5 + 2
        else:
            return h_age * 7
    else:
        return "Invalid input, please provide a valid age"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()