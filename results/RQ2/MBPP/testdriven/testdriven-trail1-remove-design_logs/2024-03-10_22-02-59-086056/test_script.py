def dog_age(h_age):
    age_conversion = {
        0: 0,
        1: 10,
    }
    for i in range(2, h_age + 1):
        age_conversion[i] = 21 + (i - 2) * 4

    if h_age < 0:
        return "Error"
    else:
        return age_conversion[h_age] if h_age in age_conversion else 10.5 * h_age
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()