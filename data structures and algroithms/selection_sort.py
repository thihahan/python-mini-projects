
def find_greatest(arr):
    hightest = 0
    hightest_index = 0
    for index, i in enumerate(arr):
        if i > hightest:
            hightest = i
            hightest_index = index
    return hightest_index

li = [10, 5, 7, 8, 15, 28, 2, 9]

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        greatest = arr.pop(find_greatest(arr))
        new_arr.append(greatest)
        print(arr)
    return new_arr

        

print(selection_sort(li))