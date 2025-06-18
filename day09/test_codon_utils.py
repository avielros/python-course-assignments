from codon_utils import get_codon_table, build_reverse_codon_table, count_amino_acids

def test_build_reverse_codon_table():
    reverse = build_reverse_codon_table(get_codon_table())
    assert reverse['ATG'] == 'Met'
    assert reverse['TAA'] == 'STOP'
    assert reverse['TTT'] == 'Phe'

def test_count_amino_acids_simple():
    reverse = build_reverse_codon_table(get_codon_table())
    counts = count_amino_acids('ATGTTTATG', reverse)
    assert counts['Met'] == 2
    assert counts['Phe'] == 1

def test_count_amino_acids_with_unknown():
    reverse = build_reverse_codon_table(get_codon_table())
    counts = count_amino_acids('XXXATGTTT', reverse)
    assert counts['Met'] == 1
    assert counts['Phe'] == 1
