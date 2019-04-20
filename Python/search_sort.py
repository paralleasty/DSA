# 顺序查找
def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found


def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos += 1

    return found

# 二分查找
# def binarySearch(alist, item):
#     first = 0
#     last = len(alist)
#     found = False

#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if alist[midpoint] == item:
#             found = True
#         elif item < alist[midpoint]:
#             last = midpoint-1
#         else:
#             first = midpoint+1
#     return found


def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binarySearch(alist[:mid], item)
        else:
            return binarySearch(alist[mid+1:], item)


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        elif self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace old value
        else:
            nextslot = self.rehash(hashvalue, len(self.slots))
            while self.slots[nextslot] is not None and \
                self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, len(self.slots))
            if self.slots[nextslot] is None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


# testlist = [0, 1, 2, 8, 13, 17, 19, 21, 31, 40]
# print(orderedSequentialSearch(testlist, 10))
# print(orderedSequentialSearch(testlist, 31))

# h = HashTable()
# h[54] = 'cat'
# h[26] = 'dog'
# h[93] = 'lion'
# h[17] = 'tiger'
# h[77] = 'bird'
# h[31] = 'cow'
# h[44] = 'goat'
# h[55] = 'pig'
# h[20] = 'chicken'
# print(h.slots)
# print(h.data)


# 冒泡排序需要多次遍历列表，它比较相邻的项并交换那些无序的项
# 每次遍历列表将下一个最大的值放在其正确的位置
def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                # alist[i], alist[i+1] = alist[i+1], alist[i]

# alist = [34, 18, 19, 9, 53, 20, 55, 13]
# bubbleSort(alist)
# print(alist)


# 冒泡排序可以识别排序列表和停止
# 短冒泡排序
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum = passnum - 1

# alist = [1, 5, 3, 8, 4, 7, 9, 11, 19]
# shortBubbleSort(alist)
# print(alist)


# 选择排序
def selectionSort(alist):
    for i in range(len(alist)-1, 0, -1):
        max = 0
        for p in range(1, i+1):
            if alist[p] > alist[max]:
                max = p
        alist[i], alist[max] = alist[max], alist[i]

# alist = [54,26,93,17,77,31,44,55,20]
# selectionSort(alist)
# print(alist)


# 插入排序
def insertionSort(alist):
    for i in range(1, len(alist)):
        k = alist[i]
        j = i
        while j > 0 and alist[j-1] > k:
            alist[j] = alist[j-1]
            j = j - 1
        alist[j] = k

# alist = [54,26,93,17,77,31,44,55,20]
# insertionSort(alist)
# print(alist)


# 希尔排序: 减少插入排序的比较（或移位）
def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for start in range(sublistcount):
            gapInsertionSort(alist, start, sublistcount)
        print("After increments of size", sublistcount,
                "The list is", alist)
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        current = alist[i]
        position = i
        while position >= gap and alist[position-gap] > current:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = current

# alist = [54,26,93,17,77,31,44,55,20]
# shellSort(alist)
# print(alist)


def mergeSort(alist):
    print('Splitting ', alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            alist[k] = right[j]
            k += 1
            j += 1
    print('Merging ', alist)

# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], \
                alist[leftmark]
    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
