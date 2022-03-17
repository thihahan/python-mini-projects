def sum(li):
    if li == []:
        return 0
    return li[0] + sum(li[1:])

# print(sum([1, 4, 5, 2]))

res = [1680, 640]

def possible_square(tur):
    if tur[0] > tur[1]:
        high = tur[0]
        low = tur[1]
    else:
        high = tur[1]
        low = tur[0]
        
    x = high - low
    if high == low:
        return [high, low]
    else:
        return possible_square([x, low])
    
print(possible_square(res))