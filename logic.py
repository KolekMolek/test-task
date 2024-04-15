from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self._x = self.validate_value(x)
        self._y = self.validate_value(y)

    def __str__(self):
        return f'Point at ({self._x}, {self._y})'

    @property
    def coordinates(self):
        """Метод для получения координат точки"""
        return self._x, self._y

    def set_coordinates(self, x, y):
        """Метод для изменения координат точки"""
        self._x = self.validate_value(x)
        self._y = self.validate_value(y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = self.validate_value(x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = self.validate_value(y)

    def distance_point_to_point(self, point):
        """Метод для вычисления расстояния до другой точки (объекта)"""
        return self.calculating_distance(self._x, self._y, point.x, point.y)

    def distance_point_to_coordinates(self, x, y):
        """Метод для вычисления расстояния до другой точки (координаты)"""
        x = self.validate_value(x)
        y = self.validate_value(y)
        return self.calculating_distance(self._x, self._y, x, y)

    @staticmethod
    def validate_value(num):
        if type(num) in (int, float):
            return num
        raise ValueError('Координаты нужно передавать в формате int или float!')

    @staticmethod
    def calculating_distance(x1, y1, x2, y2):
        """Возвращает результат, округлённый до сотых"""
        result = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return round(result, 3)


def unique_elements(num_list: list):
    """Функция принимает список целый чисел и возвращает новый список,
    содержащий только уникальные элементы из исходного списка"""
    return list(set(num_list))


def list_simple_num_in_range(range_min: int, range_max: int):
    """
    Принимает два целых числа, возвращает список простых чисел в этом диапазоне (включительно)
    """
    if range_min > range_max:
        return ValueError('Первое число не может быть больше второго!')
    simple_nums = list()
    for num in range(range_min, range_max + 1):
        if num < 2 or num % 2 == 0 and num != 2:
            continue
        is_simple = True
        for i in range(3, num // 2 + 1, 2):
            if num % i == 0:
                is_simple = False
                break
        if is_simple:
            simple_nums.append(num)
    return simple_nums


def sorting_list_of_row(row_list: list):
    """Сортирует список строк по длине, сначала по возрастанию, а затем по убыванию"""
    row_list = [str(row) for row in row_list]
    sorted_asc = sorted(row_list, key=len)
    sorted_desc = sorted(row_list, key=len, reverse=True)
    return sorted_asc, sorted_desc

