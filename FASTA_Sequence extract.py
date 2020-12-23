import fastaparser
folder = input("Please enter the folder path!: ")
file = input("Please enter the file name!: ")
f= open(folder + "/" + file + ".txt",'w')
with open(folder + "/" + file) as fasta_file:
        parser = fastaparser.Reader(fasta_file, parse_method='quick')
        for seq in parser:
            # seq is a namedtuple('Fasta', ['header', 'sequence'])
            f.write(seq.sequence)
f.close()