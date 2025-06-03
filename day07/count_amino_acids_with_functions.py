from collections import defaultdict
import sys

def get_codon_table():
    return {
        'Phe': ['TTT', 'TTC'],
        'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
        'Ile': ['ATT', 'ATC', 'ATA'],
        'Met': ['ATG'],
        'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
        'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
        'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
        'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
        'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
        'Tyr': ['TAT', 'TAC'],
        'His': ['CAT', 'CAC'],
        'Gln': ['CAA', 'CAG'],
        'Asn': ['AAT', 'AAC'],
        'Lys': ['AAA', 'AAG'],
        'Asp': ['GAT', 'GAC'],
        'Glu': ['GAA', 'GAG'],
        'Cys': ['TGT', 'TGC'],
        'Trp': ['TGG'],
        'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
        'STOP': ['TAA', 'TAG', 'TGA']
    }

def build_reverse_codon_table(codon_table):
    reverse = {}
    for aa, codons in codon_table.items():
        for codon in codons:
            reverse[codon] = aa
    return reverse

def read_sequence_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    sequence = ''
    for line in lines:
        if not line.startswith('>'):
            sequence += line.strip().upper()
    return sequence

def count_amino_acids(sequence, reverse_codon_table):
    counts = defaultdict(int)
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        aa = reverse_codon_table.get(codon)
        if aa:
            counts[aa] += 1
    return counts

def print_amino_acid_counts(counts):
    print("Amino Acid Counts:")
    for aa in sorted(counts):
        print(f"{aa:5}: {counts[aa]}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python count_amino_acids_with_functions.py <filename>")
        return

    filename = sys.argv[1]
    codon_table = get_codon_table()
    reverse_codon_table = build_reverse_codon_table(codon_table)
    sequence = read_sequence_from_file(filename)
    counts = count_amino_acids(sequence, reverse_codon_table)
    print_amino_acid_counts(counts)

if __name__ == "__main__":
    main()
