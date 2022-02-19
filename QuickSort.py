###############################################################################
# Recursive implementation of QuickSort algorithm.
# Mark Barros - BID 013884117
# CS3310 - Design and Analysis of Algorithms
# Cal Poly Pomona: Spring 2021
###############################################################################

# These are imported modules. ------------------------------------------------
import time
import random

# These are global variables. ------------------------------------------------
n = 100000                  # n is the number of integers in an array.
start = 0                   # start is the "time" when an iteration of
                            # quickSort begins.
finish = 0                  # finish is the "time" when an iteration of
                            # quickSort ends.
period = 0                  # period is the amount of time, in seconds, that
                            # quickSort took to complete an iteration.

# This is my partitioning function. ------------------------------------------

def partition(array, low, high):

    # i is the index of smaller element.
    i = (low - 1)
    # pivot is the last element.
    pivot = array[high]       

    for j in range(low, high): 
  
        # This determines if the current element is
        # smaller than or equal to pivot.
        if array[j] <= pivot:
            i = i + 1  
            array[i], array[j] = array[j], array[i] 

    array[i + 1], array[high] = array[high], array[i+1]

    return (i + 1)

# This is the main function implementing QuickSort. --------------------------

def quickSort(array, low, high):
    if len(array) == 1: 
        return array 
    if low < high: 
  
        # array[p] is now in the right location.
        partioningIndex = partition(array, low, high) 
  
        # Separately sort elements before and 
        # after the partition.
        quickSort(array, low, partioningIndex - 1) 
        quickSort(array, partioningIndex + 1, high)


# This is the driver code. ---------------------------------------------------

if __name__ == '__main__':

    while n <= 2000000:
        integerList = random.sample(range(0, n), n)

        # Uncomment the following line to print an unsorted list.
        # print(integerList) 
        
        # This performs a quick sort and times the operation.
        start = time.perf_counter_ns()
        quickSort(integerList, 0, n-1)
        finish = time.perf_counter_ns()

        # This calculates the elapsed time in seconds.
        period = ((finish - start) * (10**-9))

        # This outputs to the screen the number of elements that were
        # sorted and the corresponding time it took to sort them.
        print("For n = ", f'{n:9,}', " t = ", f'{period:.3}')

        # Uncomment the following line to print a sorted list.
        # print(integerList)

        n += 100000
###############################################################################