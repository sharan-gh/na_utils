def rna(seq):
    """Convert DNA sequence to RNA."""
    #convert to uppercase
    seq = seq.upper()
    return seq.replace('T','U')
