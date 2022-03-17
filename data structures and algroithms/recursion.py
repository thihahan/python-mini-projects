import time

main_box = ['cookies', ['clothes', 'shoes', ['phone', 'charger', ['power bank', 'mouse'], 'laptop', ['key'], 'ddw'], 'aa', 'ee'], 'adga', ['wiee', 'ieag']]


def look_for_key(box):
    for item in box:
        if isinstance(item, list):
            print("looking for key...")
            look_for_key(item)
        elif item == 'key':
            print("Found the key")
            break


# look_for_key(main_box)

# base case and recursive case

seconds_now = 10


def count_down(seconds):
    stop = False

    while stop is not True:
        # base case
        time.sleep(1)
        if seconds == 1:
            print("Happy New year")
            stop = True
        # recursive case
        else:
            seconds = seconds - 1
            print(seconds)

#count_down(seconds_now)

# call stack

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
    
print(fact(4))