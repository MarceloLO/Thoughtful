import unittest
from sort import sort


class TestSort(unittest.TestCase):
    def test_sort(self):
        standard_package = (10, 15, 20, 10)
        special_heavy_package = (100, 150, 200, 10)
        special_bulky_package_volume = (100, 120, 120, 10)
        special_bulky_package_dimension = (10, 15, 20, 50)
        rejected_package = (100, 120, 120, 50)

        sorted_standard_package = sort(*standard_package)
        sorted_special_heavy_package = sort(*special_heavy_package)
        sorted_special_bulky_package_volume = sort(*special_bulky_package_volume)
        sorted_special_bulky_package_dimension = sort(*special_bulky_package_dimension)
        sorted_rejected_package = sort(*rejected_package)

        self.assertEqual("STANDARD", sorted_standard_package)
        self.assertEqual("SPECIAL", sorted_special_heavy_package)
        self.assertEqual("SPECIAL", sorted_special_bulky_package_volume)
        self.assertEqual("SPECIAL", sorted_special_bulky_package_dimension)
        self.assertEqual("REJECTED", sorted_rejected_package)

        with self.assertRaises(ValueError) as context:
            sort(10, -2, 20, 0)
        self.assertEqual(context.exception.args[0], "Dimensions and mass must be greater then 0")
