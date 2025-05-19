import sys

sequence = sys.argv[1]

parts = sequence.split('X')
print(parts)

valid_parts = []

for part in parts:
    if part != "":
        is_valid = True
        for c in part:
            if c not in "ACTG":
                is_valid = False 
                break
        if is_valid:
            valid_parts.append(part)

valid_parts.sort(key=len, reverse=True)
print(valid_parts)
