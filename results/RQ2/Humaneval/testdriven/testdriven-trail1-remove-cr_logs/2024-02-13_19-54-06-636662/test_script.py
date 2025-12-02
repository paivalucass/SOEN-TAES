def Strongest_Extension(class_name, extensions):
    # Input validation
    if not class_name or not extensions:
        return "Error: Invalid input"

    strength_dict = {}
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        strength_dict[ext] = strength
    
    strongest_ext = max(strength_dict, key=strength_dict.get)
    return f"{class_name}.{strongest_ext}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()