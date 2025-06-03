

import sys
from collections import defaultdict


codon_table = {
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


reverse_codon_table = {}
for aa, codons in codon_table.items():
    for codon in codons:
        reverse_codon_table[codon] = aa

def read_sequence(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    
    sequence = ''
    for line in lines:
        if line.startswith('>'):
            continue
        sequence += line.strip().upper()

    return sequence

def count_amino_acids(sequence):
    amino_acid_counts = defaultdict(int)

    
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon in reverse_codon_table:
            aa = reverse_codon_table[codon]
            amino_acid_counts[aa] += 1
        else:
            print(f"Warning: Unknown codon '{codon}' – ignored.")

    return amino_acid_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python count_amino_acids.py <filename>")
        return

    filename = sys.argv[1]
    sequence = read_sequence(filename)
    counts = count_amino_acids(sequence)

    print("Amino Acid Counts:")
    for aa in sorted(counts):
        print(f"{aa:5}: {counts[aa]}")

if __name__ == "__main__":
    main()
