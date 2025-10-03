# Тестирование скрипта merge_sorting в папке

import unittest
import sys
import os

# Получаем путь к текущему файлу тестов
current_file_path = os.path.abspath(__file__)
print(f"Текущий файл: {current_file_path}")

# Получаем папку, где лежит текущий файл (tests)
tests_dir = os.path.dirname(current_file_path)
print(f"Папка tests: {tests_dir}")

# Получаем родительскую папку (project)
project_dir = os.path.dirname(tests_dir)
print(f"Папка проекта: {project_dir}")

# Добавляем папку проекта в пути Python
sys.path.append(project_dir)

from sorting.merge_sorting import merge_sorting, get_merging_sorted_sequences


# Ваши функции merge_sorting и get_merging_sorted_sequences здесь...

class TestMergeSort(unittest.TestCase):
    
    def test_empty_list(self):
        """Тест пустого списка"""
        self.assertEqual(merge_sorting([]), [])
    
    def test_single_element(self):
        """Тест списка с одним элементом"""
        self.assertEqual(merge_sorting([5]), [5])
    
    def test_two_elements_sorted(self):
        """Тест двух элементов в правильном порядке"""
        self.assertEqual(merge_sorting([1, 2]), [1, 2])
    
    def test_two_elements_unsorted(self):
        """Тест двух элементов в неправильном порядке"""
        self.assertEqual(merge_sorting([2, 1]), [1, 2])
    
    def test_multiple_elements_sorted(self):
        """Тест уже отсортированного списка"""
        self.assertEqual(merge_sorting([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_multiple_elements_reverse_sorted(self):
        """Тест списка, отсортированного в обратном порядке"""
        self.assertEqual(merge_sorting([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_multiple_elements_random(self):
        """Тест случайного набора элементов"""
        self.assertEqual(merge_sorting([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])
    
    def test_duplicate_elements(self):
        """Тест списка с повторяющимися элементами"""
        self.assertEqual(merge_sorting([2, 2, 1, 1, 3, 3]), [1, 1, 2, 2, 3, 3])
    
    def test_negative_numbers(self):
        """Тест списка с отрицательными числами"""
        self.assertEqual(merge_sorting([-3, -1, -2, -5]), [-5, -3, -2, -1])
    
    def test_mixed_positive_negative(self):
        """Тест списка с положительными и отрицательными числами"""
        self.assertEqual(merge_sorting([3, -1, 0, -2, 5]), [-2, -1, 0, 3, 5])
    
    def test_large_list(self):
        """Тест большого списка"""
        large_list = list(range(1000, 0, -1))
        sorted_list = list(range(1, 1001))
        self.assertEqual(merge_sorting(large_list), sorted_list)


class TestMergeFunction(unittest.TestCase):
    """Тесты для вспомогательной функции слияния"""
    
    def test_merge_empty_lists(self):
        """Тест слияния двух пустых списков"""
        self.assertEqual(get_merging_sorted_sequences([], []), [])
    
    def test_merge_one_empty_list(self):
        """Тест слияния, когда один список пустой"""
        self.assertEqual(get_merging_sorted_sequences([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(get_merging_sorted_sequences([], [1, 2, 3]), [1, 2, 3])
    
    def test_merge_sorted_lists(self):
        """Тест слияния двух отсортированных списков"""
        self.assertEqual(get_merging_sorted_sequences([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
    
    def test_merge_lists_different_lengths(self):
        """Тест слияния списков разной длины"""
        self.assertEqual(get_merging_sorted_sequences([1, 3], [2, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(get_merging_sorted_sequences([1, 3, 5, 7], [2, 4]), [1, 2, 3, 4, 5, 7])


# Дополнительные тесты для edge cases
class TestEdgeCases(unittest.TestCase):
    
    def test_single_duplicate(self):
        """Тест списка с одним повторяющимся элементом"""
        self.assertEqual(merge_sorting([1, 1]), [1, 1])
    
    def test_all_same_elements(self):
        """Тест списка, где все элементы одинаковые"""
        self.assertEqual(merge_sorting([7, 7, 7, 7]), [7, 7, 7, 7])
    
    def test_floats(self):
        """Тест с числами с плавающей точкой"""
        self.assertEqual(merge_sorting([1.5, 1.1, 2.3, 0.5]), [0.5, 1.1, 1.5, 2.3])

if __name__ == '__main__':
    unittest.main()