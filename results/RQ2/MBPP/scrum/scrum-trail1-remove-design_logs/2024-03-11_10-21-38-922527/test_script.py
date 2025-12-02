def dog_age(h_age):
    if not isinstance(h_age, int) or h_age <= 0:
        return "Invalid input"
    elif h_age <= 2:
        return h_age * 10.5
    else:
        return 21 + (h_age - 2) * 4

# Test cases
print(dog_age(0)) # Expected output: "Invalid input"
print(dog_age(1)) # Expected output: 10.5
print(dog_age(2)) # Expected output: 21.0
print(dog_age(12)) # Expected output: 61
print(dog_age('abc')) # Expected output: "Invalid input"
print(dog_age(-1)) # Expected output: "Invalid input"
print(dog_age(100)) # Expected output: 700
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()