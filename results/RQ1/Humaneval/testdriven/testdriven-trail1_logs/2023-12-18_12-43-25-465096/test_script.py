def planets_between(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets or planet2 not in planets:
        return ()

    start_index = min(planets.index(planet1), planets.index(planet2))
    end_index = max(planets.index(planet1), planets.index(planet2))

    planets_between = [planet for planet in planets[start_index+1:end_index]]
    return tuple(sorted(planets_between, key=lambda x: planets.index(x)))
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
    
    def test2(self):
        self.assertEqual(bf("Earth", "Mercury"), ("Venus"))
    
    def test3(self):
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

if __name__ == '__main__':
    unittest.main()