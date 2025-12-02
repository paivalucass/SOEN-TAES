def dog_age(h_age):
    if not isinstance(h_age, (int, float)) or h_age < 0:
        raise ValueError("Invalid input. Please enter a valid age.")

    if h_age == 1:
        return 15
    elif h_age == 2:
        return 24
    else:
        return 24 + 4 * (h_age - 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()