sequence = input("Enter a DNA sequence: ")


valid_parts = []
current_part = ""

for c in sequence:
    if c in "ACTG":
        current_part += c
    else:
        if current_part != "":
            valid_parts.append(current_part)
            current_part = ""

if current_part != "":
    valid_parts.append(current_part)

valid_parts.sort(key=len, reverse=True)
print(valid_parts)
