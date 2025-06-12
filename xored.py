label = "label"
result = ""

for c in label:
    xored = ord(c) ^ 13
    result += chr(xored)

print(f"crypto{{{result}}}")
