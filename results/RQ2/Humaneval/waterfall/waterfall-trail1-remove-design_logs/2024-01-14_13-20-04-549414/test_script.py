def compare_one(a, b):
    if is_number(a) and is_number(b):
        return compare_numbers(a, b)
    elif is_number(a) and is_string(b):
        return compare_number_and_string(a, b)
    elif is_string(a) and is_number(b):
        return compare_string_and_number(a, b)
    elif is_string(a) and is_string(b):
        return compare_strings(a, b)
    else:
        return None


def is_number(val):
    return isinstance(val, (int, float))


def is_string(val):
    return isinstance(val, str)


def compare_numbers(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None


def compare_number_and_string(a, b):
    try:
        b_num = float(b.replace(',', '.'))
        if a > b_num:
            return a
        elif b_num > a:
            return b
        else:
            return None
    except ValueError:
        return b


def compare_string_and_number(a, b):
    try:
        a_num = float(a.replace(',', '.'))
        if a_num > b:
            return a
        elif b > a_num:
            return b
        else:
            return None
    except ValueError:
        return a


def compare_strings(a, b):
    try:
        a_num = float(a.replace(',', '.'))
        b_num = float(b.replace(',', '.'))
        if a_num > b_num:
            return a
        elif b_num > a_num:
            return b
        else:
            return None
    except ValueError:
        return b

import unittest

class Test(unittest.TestCase):
    def test_compare_one(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertIsNone(compare_one("1", 1))

if __name__ == '__main__':
    unittest.main()