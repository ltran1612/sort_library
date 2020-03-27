''' template
def bubble_sort(list, small_big):
    # smallest to biggest
    if small_big:
        pass
    # biggest to smallest
    else:
        pass
'''
SMALL_BIG = True
BIG_SMALL = False

def swap(list, one, two):
    temp = list[one]
    list[one] = list[two]
    list[two] = temp

# bubble sort
def bubble_sort(list, small_big):
    list_length = len(list)
    # smallest to biggest
    for i in range(0, list_length-1):
            for j in range(0, list_length-i-1):
                if list[j] > list[j+1]:
                    swap(list, j, j+1)
    # biggest to smallest
    else:
        for i in range(0, list_length-1):
            for j in range(0, list_length-i-1):
                if list[j] < list[j+1]:
                    swap(list, j, j+1)

# selection sort
def selection_sort(list, small_big):
    list_length = len(list)
    
    # smallest to biggest
    if small_big:
        for i in range(0, list_length-1):
            extreme_idx = i
            for j in range(i+1, list_length):
                if list[j] < list[extreme_idx]:
                    extreme_idx = j
            swap(list, i, extreme_idx)
    # biggest to smallest
    else:
        for i in range(0, list_length-1):
            extreme_idx = i
            for j in range(i+1, list_length):
                if list[j] > list[extreme_idx]:
                    extreme_idx = j
            swap(list, i, extreme_idx)

# insertion sort
def insertion_sort(list, small_big):
    list_length = len(list)

    # smallest to biggest
    if small_big:
        for i in range(1, list_length):
            for j in range(0, i):
                if list[i] < list[j]:
                    temp = list.pop(i)
                    list.insert(j, temp)
    # biggest to smallest
    else:
        for i in range(1, list_length):
            for j in range(0, i):
                if list[i] > list[j]:
                    temp = list.pop(i)
                    list.insert(j, temp)

# quick sort 
def quick_sort(list, small_big):
    list_length = len(list)

    # smallest to biggests
    if small_big:
        quicksort_smallbig(list, 0, list_length - 1)
    # biggest to smallest
    else:
        quicksort_bigsmall(list, 0, list_length - 1)

# quick sort small to big with a pivot
# inspired by geeksforgeek psuedo code
def quicksort_smallbig(list, low, high):
    if (high > low):
        pivot_idx = partition_smallbig(list, low, high)

        quicksort_smallbig(list, low, pivot_idx - 1)
        quicksort_smallbig(list, pivot_idx + 1, high)

# quick sort big to small with a pivot
# inspired by geeksforgeek psuedo code
def quicksort_bigsmall(list, low, high):
    # print(str(low) + " " + str(high) + " " + str(len(list)))
    if (high > low):
        pivot_idx = partition_bigsmall(list, low, high)

        quicksort_bigsmall(list, low, pivot_idx - 1)
        quicksort_bigsmall(list, pivot_idx + 1, high)


# partition with a right most pivot
# inspired by geeksforgeek psuedo code
def partition_smallbig(list, low, high):
    pivot = list[high]
    left = low - 1
    for right in range(low, high):
        if list[right] < pivot:
            left += 1
            swap(list, right, left)
    swap(list, left + 1, high)
    return left + 1

def partition_bigsmall(list, low, high):
    pivot = list[high]
    left = low - 1
    for right in range(low, high):
        if list[right] > pivot:
            left += 1
            swap(list, right, left)
    
    swap(list, left + 1, high)
    return left + 1

        


'''
test1 = [1, 2, 3, 4, 3, 6, 5, 5]
test2 = [1, 2, 3, 5, 6, 3, 4]
test3 = [1, 2, 6, 5, 3, 8, 4]

quicksort_bigsmall(test1, 0, 7)


print(test1)
print(test2)
print(test3)
'''
