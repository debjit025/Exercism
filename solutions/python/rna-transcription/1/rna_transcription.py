def to_rna(dna_strand):
    complement = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    rna_strand = ''
    for nucleotides in dna_strand:
        if nucleotides in complement:
            rna_strand += complement[nucleotides]
    return rna_strand
