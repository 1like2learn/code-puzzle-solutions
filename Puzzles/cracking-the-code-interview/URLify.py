inputs = ["Mr John Smith   ", "   Stuff and things    "]

def urlIfy(inp):
    inp = inp.strip()
    output = ""
    for char in inp:
        if char == ' ':
            output += "%20"
        else:
            output += char
    return output

for inp in inputs:
    print(f"{inp}:", urlIfy(inp))