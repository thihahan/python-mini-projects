
def multiplicationTable(arr):
    new_arr = []
    for i in arr:
        for x in arr:
            new_arr.append(i * x)
    return new_arr
    
arr = [1, 2, 4, 5]
print(multiplicationTable(arr))
