import random
from time import perf_counter

lis = random.sample(range(1, 10000), 500)

class Sort:
    def __init__(self, lis):
        self.lis = lis

    def bubble_sort(self, lis):
        n = len(lis)
        for i in range (n):
            for j in range(0, n - i - 1):
                if lis[j] > lis[j + 1]:
                    lis[j], lis[j + 1] = lis[j +1], lis[j]
        return lis
    
    def python_sort(self, lis):
        lis.sort()
        return lis
    
    def merge_split(self, lis):
        n = len(lis)

        if n <= 1:
            return lis
        
        mid = n//2

        left = lis[:mid]

        right = lis[mid:]

        split_left = self.merge_split(left)

        split_right = self.merge_split(right)

        return self.merge(split_left, split_right)
    
    def merge(self, left, right):
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

class Timer:
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
    
    def average_time(self, function, runs):
        times = []
        for i in range(runs):
            lis = random.sample(range(1, 10000), 500)
            self.timer_start()
            function(lis.copy())
            times.append(self.timer_stop())
        return sum(times) / len(times)
            

         

#MergeSort + Timer
merge_timer = Timer()
merge_timer.timer_start()
merge = Sort(lis)
sorted = merge.merge_split(lis)
print(sorted)
elapsedmerge = merge_timer.timer_stop()
print(f"Time elapsed for mergesort: {elapsedmerge}\n")

#BubbleSort + Timer
bubble_timer = Timer()
bubble_timer.timer_start()
bubble = Sort(lis)
bubble_list = bubble.bubble_sort(lis)
print(bubble_list)
elapsedbubble = bubble_timer.timer_stop()
print(f"Time elapsed for bubblesort: {elapsedbubble}\n")

#PythonSort + Timer
python_timer = Timer()
python_timer.timer_start()
sort = Sort(lis)
pytsort = sort.python_sort(lis)
print(pytsort)
elapsedpytsort = python_timer.timer_stop()
print(f"Time elapsed for pythonsort: {elapsedpytsort}\n")

print(f"time comparison in one run (seconds):\nMerge: {elapsedmerge}\nBubble: {elapsedbubble}\nPythonSort: {elapsedpytsort}")

#Average Time For Sorting Per Method
timer = Timer()
sorter = Sort(lis)

merge_avg = timer.average_time(sorter.merge_split, 50)
bubble_avg = timer.average_time(sorter.bubble_sort, 50)
python_avg = timer.average_time(sorter.python_sort, 50)
print(f"\ntime average comparison (seconds):\nMerge: {merge_avg}\nBubble: {bubble_avg}\nPythonSort: {python_avg}")
