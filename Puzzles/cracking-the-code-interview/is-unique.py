inputs = ["whatever", "abc", "stuff", "dunno", "yarp", "uh", "y", "ugh","abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz0123456789.,/';][=-`ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+}{:?><~~"]
correctSolutions = [False, True, False, False, True, True, True, True]
def isUnique(string):
    i = 0
    while i < len(string):
        j = len(string) - 1
        while j > i:
            if string[j] == string[i]:
                return False
            j -= 1
        i += 1
    return True

for inp in inputs:
    print(isUnique(inp))