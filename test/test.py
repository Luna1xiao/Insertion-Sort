import random
import sys
sys.path.append('src/')
from Insertion_Sort import *

def main():
    len = 20
    arr = [random.randint(1, 100) for _ in range(len)]

    print("原始数组：", arr)

    insertion_sort(arr)

    print("排序后的数组：", arr)

if __name__ == "__main__":
    main()