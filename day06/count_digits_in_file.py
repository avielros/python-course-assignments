import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

digit_count = {str(d): 0 for d in range(10)}

with open(filename, 'r') as fh:
    for line in fh:
        for char in line:
            if char.isdigit():
                digit_count[char] += 1

with open("report.txt", 'w') as out_fh:
    for digit in sorted(digit_count.keys()):
        out_fh.write(f"{digit} {digit_count[digit]}\n")
