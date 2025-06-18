import sys
from codon_utils import get_codon_table, build_reverse_codon_table, read_sequence_from_file, count_amino_acids

def print_amino_acid_counts(counts):
    print("Amino Acid Counts:")
    for aa in sorted(counts):
        print(f"{aa:5}: {counts[aa]}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        return

    filename = sys.argv[1]
    codon_table = get_codon_table()
    reverse_codon_table = build_reverse_codon_table(codon_table)
    sequence = read_sequence_from_file(filename)
    counts = count_amino_acids(sequence, reverse_codon_table)
    print_amino_acid_counts(counts)

if __name__ == "__main__":
    main()
