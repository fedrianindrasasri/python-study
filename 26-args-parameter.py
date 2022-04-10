# *args = parameter yang akan mengemas semua argumen kedalam tuple
#

def add(*aaaa):
    sum = 0
    for i in aaaa:
        sum += i
    return sum


print(add(1, 2, 3))
 