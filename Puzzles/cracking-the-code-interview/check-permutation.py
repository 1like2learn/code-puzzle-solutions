# abc acb bac bca cab cba
inputs = [["abc","acb"],["abc","bac"],["abc","bca"],["abc","cab"],["abc","cba"],["abcd","abc"],["tacocat","catastrophy"]]

def checkPerm(inp):
    cache = {}
    for char in inp[0]:
        if char in cache:
            cache[char] += 1
        else:
            cache[char] = 1
    for char in inp[1]:
        if char in cache:
            cache[char] -= 1
        else:
            return False
        if cache[char] == 0:
            cache.pop(char)
    if len(cache) > 0:
        return False
    return True
for inp in inputs:
    print(checkPerm(inp))