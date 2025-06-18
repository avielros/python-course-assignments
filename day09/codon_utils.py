from collections import defaultdict

def get_codon_table():
    """
    Returns the codon table mapping amino acids to their codons.
    
    >>> codon_table = get_codon_table()
    >>> 'Met' in codon_table and 'ATG' in codon_table['Met']
    True
    """
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
    """
    Builds a reverse codon table from codon to amino acid.
    
    >>> rev = build_reverse_codon_table(get_codon_table())
    >>> rev['ATG']
    'Met'
    """
    reverse = {}
    for aa, codons in codon_table.items():
        for codon in codons:
            reverse[codon] = aa
    return reverse

def read_sequence_from_file(filename):
    """
    Reads a DNA sequence from a FASTA-like file (ignores headers).
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    sequence = ''
    for line in lines:
        if not line.startswith('>'):
            sequence += line.strip().upper()
    return sequence

def count_amino_acids(sequence, reverse_codon_table):
    """
    Counts amino acids in the sequence using the codon table.

    >>> rev = build_reverse_codon_table(get_codon_table())
    >>> count_amino_acids('ATGTTTATG', rev)['Met']
    2
    """
    counts = defaultdict(int)
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        aa = reverse_codon_table.get(codon)
        if aa:
            counts[aa] += 1
    return counts

if __name__ == "__main__":
    import doctest
    doctest.testmod()
