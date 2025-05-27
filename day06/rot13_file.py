import sys
import codecs

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

with open(filename, 'r') as fh:
    text = fh.read()

rot_text = codecs.encode(text, 'rot_13')


with open(filename, 'w') as fh:
    fh.write(rot_text)
