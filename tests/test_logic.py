from unittest import TestCase

from logic import unique_elements, list_simple_num_in_range, sorting_list_of_row, Point


class TestSomeFunctions(TestCase):
    def test_unique_elements(self):
        res_default = unique_elements([1, 2, 3, 3, 4, -5])
        res_empty = unique_elements([])
        res_one_element = unique_elements([3, 3, 3, 3, 3])
        self.assertEqual([1, 2, 3, 4, -5], res_default)
        self.assertEqual([], res_empty)
        self.assertEqual([3, ], res_one_element)

    def test_list_simple_num_in_range(self):
        res_raise = list_simple_num_in_range(100, 10)
        res_default = list_simple_num_in_range(1, 50)
        res_with_negative_num = list_simple_num_in_range(-100, 50)
        self.assertTrue(isinstance(res_raise, ValueError))
        self.assertEqual('Первое число не может быть больше второго!', res_raise.args[0])
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47], res_default)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47], res_with_negative_num)

    def test_sorting_list_of_row(self):
        res_default = sorting_list_of_row(['Ян', 'Аня', 'Коля', 'Витька'])
        res_with_not_str = sorting_list_of_row([1, 'Аня', 'Коля', False])
        self.assertEqual((['Ян', 'Аня', 'Коля', 'Витька'], ['Витька', 'Коля', 'Аня', 'Ян']), res_default)
        self.assertEqual((['1', 'Аня', 'Коля', 'False'], ['False', 'Коля', 'Аня', '1']), res_with_not_str)


class TestPointMethods(TestCase):
    def test_init_point(self):
        A = Point()
        B = Point(10, 20)
        self.assertTrue(isinstance(A, Point))
        self.assertTrue(isinstance(B, Point))

    def test_get_coordinates(self):
        A = Point(5, 10)
        self.assertEqual(5, A.x)
        self.assertEqual(10, A.y)
        self.assertEqual((5, 10), A.coordinates)

    def test_set_coordinates(self):
        A = Point()
        B = Point()
        C = Point()
        A.x = 5
        A.y = 10
        B.x = -13
        B.y = -22
        C.set_coordinates(12, 22)
        self.assertEqual((5, 10), A.coordinates)
        self.assertEqual((-13, -22), B.coordinates)
        self.assertEqual((12, 22), C.coordinates)

    def test_validate_value(self):
        A = Point()
        A.x = 1.2
        self.assertEqual(1.2, A.x)
        with self.assertRaises(ValueError):
            A.x = '5'

    def test_calculating_distance(self):
        A = Point(5, 10)
        B = Point(6, 14)
        res_point_to_coords = A.distance_point_to_coordinates(7, 20)
        res_point_to_point = A.distance_point_to_point(B)
        self.assertEqual(10.198, res_point_to_coords)
        self.assertEqual(4.123, res_point_to_point)
