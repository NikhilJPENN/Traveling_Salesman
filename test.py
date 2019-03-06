import unittest
from cities import *

road_map=[('California','Sacramento',38.555605,-121.468926),('Illinois','Springfield',39.78325,-89.650373),
          ('Mississippi','Jackson',32.32,-90.207), ('California','Sacramento',38.555605,-121.468926)]

road_map1=[('California','Sacramento',38.555605,-121.468926),('Illinois','Springfield',39.78325,-89.650373),
          ('Mississippi','Jackson',32.32,-90.207), ('California','Sacramento',38.555605,-121.468926)]

road_map_swap=[('Illinois','Springfield',39.78325,-89.650373),('California','Sacramento',38.555605,-121.468926),
          ('Mississippi','Jackson',32.32,-90.207), ('Illinois','Springfield',39.78325,-89.650373),]

class CITIES(unittest.TestCase):

    def test_compute_total_distance(self):
        self.assertAlmostEqual(compute_total_distance(road_map),71.2039531)
        self.assertNotAlmostEqual(compute_total_distance(road_map),129)

    def test_swap_cities(self):
        self.assertEqual(swap_cities(road_map,0,1)[0],road_map_swap)
        
        self.assertNotEqual(swap_cities(road_map,0,1)[1],122)


unittest.main()
