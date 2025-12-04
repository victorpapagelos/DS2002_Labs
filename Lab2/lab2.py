import random
from time import perf_counter


class BubbleSort:
#Repeatedly swap elements by comparing
    def __init__(self, lis):
        self.lis = lis

    def sort(self, lis):
        return self.bubble_sort(lis)

    def bubble_sort(self, lis):
        n = len(lis)
        comparisons = 0
        for i in range (n):                 #<--
            for j in range(0, n - i - 1):   #<-- Base Case - Complexity: O(n²)
                comparisons +=1
                if lis[j] > lis[j + 1]:
                    lis[j], lis[j + 1] = lis[j +1], lis[j]
        return lis, comparisons
    

class PythonSort:
#Built in function
    def sort(self, lis):
        return self.python_sort(lis)

    def python_sort(self, lis):
        lis.sort()
        return lis
    
class MergeSort:
#Splits lists in halves, recursively sorts halves
    def sort(self, lis):
        return self.merge_split(lis) 

    def merge_split(self, lis):
        n = len(lis)

        if n <= 1:          #<--
            return lis, 1   #<-- Base Case - Complexity: O(n log n)
        
        mid = n//2

        left = lis[:mid]

        right = lis[mid:]

        split_left, recursions_left = self.merge_split(left)

        split_right, recursions_right = self.merge_split(right)

        recursions = 1 + recursions_right + recursions_left

        return self.merge(split_left, split_right), recursions
#Returns recursion count
    
    def merge(self, left, right):
#Merges sorted halves into a list
        sorted = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                sorted.append(left[left_index])
                left_index += 1
            else:
                sorted.append(right[right_index])
                right_index += 1
        sorted.extend(left[left_index:])
        sorted.extend(right[right_index:])
        return sorted
#Returns Sorted list

class BinarySearch:
#Search for a value in already sorted list using recursion
    def search(self, lis, target):
        return self.binary_search(lis, target, 0, len(lis) - 1)

    def binary_search(self, lis, val, low, high):
        if (low > high):    #<--
            return None     #<-- Base Case - Complexity: O(log n)
        else:
            mid = (low + high) // 2
            if val > lis[mid]:
                return self.binary_search(lis, val, mid + 1, high)
            elif val < lis[mid]:
                return self.binary_search(lis, val, low, mid - 1)
            else:
                return mid

class Timer:
#Measures execution time
    def __init__(self):
        self.start = None
        self.stop = None

    def timer_start(self):
        self.start = perf_counter()
       
    def timer_stop(self):
         if self.start is None:
            raise ValueError("Timer not started")
         self.stop = perf_counter()
         return self.stop - self.start
    
#Calculates average time for a sorting algorithm
    def average_time(self, function, runs):
        times = []
        for i in range(runs):
            self.timer_start()
            function(lis.copy())
            times.append(self.timer_stop())
        return sum(times) / len(times)
            

lis = random.sample(range(1, 100), 10)         

#MergeSort + Timer
merge_timer = Timer()
merge_timer.timer_start()
merge = MergeSort()
merge_sorted, recursions = merge.sort(lis.copy())
#print(sorted)
elapsedmerge = merge_timer.timer_stop()
print(f"Time elapsed for mergesort: {elapsedmerge}\nRecursions: {recursions}")
print(f"Sorted list: {merge_sorted}\n")

#BubbleSort + Timer
bubble_timer = Timer()
bubble_timer.timer_start()
bubble = BubbleSort(lis.copy())
bubble_list, comparisons = bubble.sort(lis.copy())
#print(bubble_list)
elapsedbubble = bubble_timer.timer_stop()
print(f"Time elapsed for bubblesort: {elapsedbubble}\nComparisons {comparisons}")
print(f"Sorted list: {bubble_list}\n")

#PythonSort + Timer
python_timer = Timer()
python_timer.timer_start()
sort = PythonSort()
py_sorted = sort.sort(lis.copy())
elapsedpytsort = python_timer.timer_stop()
print(f"Time elapsed for pythonsort: {elapsedpytsort}")
print(f"Sorted list: {py_sorted}\n")

print(f"time comparison in one run (seconds):\nMerge: {elapsedmerge}\nBubble: {elapsedbubble}\nPythonSort: {elapsedpytsort}")

#Average Time For Sorting Per Method
timer = Timer()

merge_avg = timer.average_time(merge.sort, 50)
bubble_avg = timer.average_time(bubble.sort, 50)
python_avg = timer.average_time(sort.sort, 50)
print(f"\ntime average comparison (seconds):\nMerge: {merge_avg}\nBubble: {bubble_avg}\nPythonSort: {python_avg}")

#Recursive Binary Search
sorted = [14, 19, 33, 36, 62, 68, 83, 126, 173, 220, 251, 257, 
               283, 286, 300, 304, 347, 372, 382, 416, 424, 447, 498, 
               508, 521, 549, 589, 637, 664, 671, 677, 697, 707, 715, 725, 
               731, 740, 757, 769, 777, 810, 818, 836, 882, 894, 941, 985, 
               1007, 1011, 1019, 1041, 1056, 1074, 1084, 1092, 1108, 1111, 
               1113, 1126, 1132, 1155, 1187, 1194, 1203, 1252, 1260, 1277, 
               1319, 1355, 1362, 1373, 1374, 1375, 1378, 1380, 1393, 1463, 
               1513, 1518, 1530, 1531, 1547, 1560, 1562, 1577, 1581, 1616, 
               1625, 1631, 1639, 1641, 1670, 1701, 1707, 1714, 1723, 1727, 
               1737, 1780, 1819, 1870, 1871, 1879, 1894, 1930, 1933, 1935]
        
binary = BinarySearch()
result = binary.search(sorted, 173)
print(f"\nIndex for target number by binary search: {result}\n")

print(f"unsorted list: {lis}")
