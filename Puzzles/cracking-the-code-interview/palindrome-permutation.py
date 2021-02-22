inputs = ["taco cat", "whatever", "stuff", "yarp"]

def palinPerm(inp):
    cache = {}
    odds = 0
    for char in inp:
        if char != ' ':
            if char in cache:
                cache[char] += 1
            else:
                cache[char] = 1
            if cache[char] % 2 == 1:
                odds += 1
            else:
                odds -= 1
    print(inp, cache, odds)
    if odds < 2:
        return True
    return False

for inp in inputs:
    print(inp + ':', palinPerm(inp))