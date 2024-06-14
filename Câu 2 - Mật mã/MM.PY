# Expected result (MM.OUT): "3"

def int_count(secret):
    integers = set()
    current = ""
    for char in secret:
        if char.isdigit():
            current += char
        elif current:
            integers.add(int(current))
            current = ""
    if current:
        integers.add(int(current))

    return len(integers)

with open("MM.INP", "r") as f:
    secret = f.readline().strip()

with open("MM.OUT", "w") as f:
    f.write(str(int_count(secret)))
