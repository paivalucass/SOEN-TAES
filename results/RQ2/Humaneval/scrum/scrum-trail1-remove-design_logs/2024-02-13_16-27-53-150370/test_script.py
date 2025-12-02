def Strongest_Extension(class_name, extensions):
    if not extensions:
        return "No extensions provided"
    
    strengths = {}
    for ext in extensions:
        cap_count = sum(1 for char in ext if char.isupper())
        sm_count = sum(1 for char in ext if char.islower())
        strength = cap_count - sm_count
        strengths[ext] = strength
    
    max_strength = max(strengths.values())
    strongest_ext = [ext for ext, strength in strengths.items() if strength == max_strength][0]
    
    return f"{class_name}.{strongest_ext}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()