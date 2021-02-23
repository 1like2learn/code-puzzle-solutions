inputs = [["pale","ple"],["pales","pale"],["pale","bale"],["pale","bake"],["whatever", "watevers"]]

def oneAway(one, two):
    differences = 0
    if len(one) > len(two):
        i = 0
        j = 0
        while j < len(two):
            if one[i] != two[j]:
                differences += 1
                i += 1
            else:
                i += 1
                j += 1
            if differences > 1:
                return False

    elif len(one) < len(two):
        i = 0
        j = 0
        while i < len(one):
            if one[i] != two[j]:
                differences += 1
                i += 1
            else:
                i += 1
                j += 1
            if differences > 1:
                return False
    else:
        i = 0
        j = 0
        while i < len(one):
            if one[i] != two[j]:
                differences += 1
            i += 1
            j += 1
            if differences > 1:
                return False
    
    return True

for inp in inputs:
    print(f"{inp}:", oneAway(inp[0], inp[1]))