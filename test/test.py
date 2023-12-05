import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Insertion_Sort import insertion_sort
#导入路径和包

#测试
class TestInsertionSort(unittest.TestCase):
    #测试空数组
    def test_empty_list(self):
        arr = []
        insertion_sort(arr)
        self.assertEqual(arr, [])
    #测试单个数组
    def test_single_element_list(self):
        arr = [1]
        insertion_sort(arr)
        self.assertEqual(arr, [1])
    #测试算法是否保持已排序列表的顺序
    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
    #测试算法是否正确对逆序列表进行排序
    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
    #测试算法是否能正确排序随机顺序的列表
    def test_random_list(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()
