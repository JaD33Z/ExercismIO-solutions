
# example dna_strand = "ACGTGGTCTTAA"


comp_dict = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}



# list comprehension solution

def to_rna(dna_strand):
    return ''.join([comp_dict[i] for i in dna_strand if i in comp_dict.keys()])



# standard for loop solution

def to_rna(dna_strand):
    ls =[]
    for i in dna_strand:
        if i in comp_dict.keys():
            ls.append(comp_dict[i])
    return ''.join(ls)



# example output:
#           'UGCACCAGAAUU'
























