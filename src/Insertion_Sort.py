def insertion_sort(arr):
    #定义函数
    for i in range(1, len(arr)):
        #循环数组
        v = arr[i]
        j = i - 1
        # 遍历找到合适的插入位置
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v
