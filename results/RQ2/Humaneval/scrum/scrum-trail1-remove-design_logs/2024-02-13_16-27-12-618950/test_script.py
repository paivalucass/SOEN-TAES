def find_planets_between(planet1, planet2):
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    planet1_index = planet_order.index(planet1)
    planet2_index = planet_order.index(planet2)
    if planet1_index < planet2_index:
        return tuple(planet_order[planet1_index+1:planet2_index])
    else:
        return tuple(planet_order[planet2_index+1:planet1_index])

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bf('Jupiter', 'Neptune'), ('Saturn', 'Uranus'))
        self.assertEqual(bf('Earth', 'Mercury'), ('Venus'))
        self.assertEqual(bf('Mercury', 'Uranus'), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'))

if __name__ == '__main':
    unittest.main()