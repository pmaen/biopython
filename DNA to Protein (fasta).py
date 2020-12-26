import fastaparser
choice = input("Please note that this tool is only functional for FASTA files!")
filename = input("Please enter the full path of the DNA sequence file!: ")
fasta_raw = open(filename, 'r')
f= open(filename + ".temp",'w')
with open(filename) as fasta_file:
    parser = fastaparser.Reader(fasta_file, parse_method='quick')
    for seq in parser:
        # seq is a namedtuple('Fasta', ['header', 'sequence'])
        f.write(seq.sequence)
f.close()
f1 = open(filename + ".temp", mode='r')
dna_raw = f1.read()
dna_raw = dna_raw.replace("\n", "")
dna_raw = dna_raw.replace("\r", "")
dna = dna_raw.upper()


choice = input("Please choose between FASTA compatible output and readable one:\n    (1) FASTA\n    (2) readable\n")
# DNA codon table
if choice == "1":
    fc1=open(filename + "translation_fasta.txt", 'w')
    protein1 = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
               "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
               "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
               "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
               "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
               "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
               "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
               "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
               "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
               "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
               "TAA" : " *", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
               "TAG" : " *", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
               "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
               "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
               "TGA" : " *", "CGA" : "R", "AGA" : "R", "GGA" : "G",
               "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"
               }

    protein_sequence1 = ""

    # Generate protein sequence
    for i in range(0, len(dna)-(3+len(dna)%3), 3):
        #if protein[dna[i:i+3]] == "STOP" :
            #break
        protein_sequence1 += protein1[dna[i:i+3]]

    # Print the protein sequence
    print(protein_sequence1, file=fc1)
    f1.close()
    fc1.close()



if choice == "2":
    fc2=open(filename + "translation_readable.txt", 'w')
    protein2 = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
               "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
               "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
               "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
               "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
               "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
               "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
               "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
               "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
               "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
               "TAA" : " stop\n", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
               "TAG" : " stop\n", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
               "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
               "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
               "TGA" : " stop\n", "CGA" : "R", "AGA" : "R", "GGA" : "G",
               "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"
               }

    protein_sequence2 = ""

    # Generate protein sequence
    for i in range(0, len(dna)-(3+len(dna)%3), 3):
        #if protein[dna[i:i+3]] == "STOP" :
            #break
        protein_sequence2 += protein2[dna[i:i+3]]

    # Print the protein sequence
    print("Protein Sequence: ", protein_sequence2, file=fc2)
    f1.close()
    fc2.close()