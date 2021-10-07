DNA_wt_raw = input("Enter shortened and aligned wildtype sequence: ")
DNA_mut_raw = input("Enter shortened and aligned mutant sequence: ")
def split(sequence):
    return [char for char in sequence]
DNA_wt = split(DNA_wt_raw)
DNA_mut = split(DNA_mut_raw)
result = []
if len(DNA_wt) == len(DNA_mut):
    seq_length = len(DNA_mut)
    for i, j in zip(DNA_wt, DNA_mut):
        if i != j:
            result.append(i)
wt_unmatched_by_mutation = len(result)
similarity = (seq_length - wt_unmatched_by_mutation)/seq_length
print(similarity)