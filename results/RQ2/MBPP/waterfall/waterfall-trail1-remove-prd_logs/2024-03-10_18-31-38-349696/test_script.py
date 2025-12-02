def even_bit_set_number(n):
    if n < 0 or n > 2147483647:
        raise ValueError("Input is out of range")

    binary_n = bin(n)[2:]

    modified_binary_n = ""
    for i in range(len(binary_n)):
        if i % 2 == 0:
            modified_binary_n += binary_n[i]
        else:
            modified_binary_n += '0'

    result = int(modified_binary_n, 2)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_bit_set_number(10), 10)

if __name__ == '__main__':
    unittest.main()