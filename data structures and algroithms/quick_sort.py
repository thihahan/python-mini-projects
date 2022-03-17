def quicksort(arr):
    if len(arr) < 2:
        return arr
    li = arr
    pivot = li[0]
    less = [i for i in li[1:] if i<=pivot]
    greater = [i for i in li[1:] if i>pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

arr = [4, 7, 2, 8, 1]
print(quicksort(arr))
    