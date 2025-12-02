def Strongest_Extension(class_name, extensions):
    def calculate_strength(ext):
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        return cap - sm

    strongest = extensions[0]
    max_strength = calculate_strength(extensions[0])

    for ext in extensions:
        strength = calculate_strength(ext)

        if strength > max_strength:
            max_strength = strength
            strongest = ext

    return f"{class_name}.{strongest}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()