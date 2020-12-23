filename = input("Put in the full location of the sequence:   ")
f= open(filename + "_analysis.txt","w+")
seqsource = open(filename)
seq = seqsource.read()
adenine_count = 0
thymine_count = 0
guanine_count = 0
cytosine_count = 0

for b in seq:
    if b == 'A':
        adenine_count += 1
    elif b == 'C':
        cytosine_count += 1
    elif b == 'T':
        thymine_count +=1
    elif b == 'G':
        guanine_count += 1
seq_lenght = len(seq)
print("Analysis of ", int(adenine_count)+int(cytosine_count)+int(thymine_count)+int(guanine_count), "nucleotides finished.", file=f)
print("ADENINE\n     number of adenines: ", int(adenine_count) , file=f)
print("     adenine quota: ", "{:.2f}".format(round((float(adenine_count)/seq_lenght)*100, 2)), " %", file=f)
print("THYMINE\n     number of thymines: ", int(thymine_count) , file=f)
print("     thymine quota: ", "{:.2f}".format(round((float(thymine_count)/seq_lenght)*100, 2)), " %", file=f)
print("GUANINE\n     number of guanines: ", int(guanine_count) , file=f)
print("     guanine quota: ", "{:.2f}".format(round((float(guanine_count)/seq_lenght)*100, 2)), " %", file=f)
print("CYTOSINE\n     number of cytosines: ", int(cytosine_count) , file=f)
print("     cytosine quota: ", "{:.2f}".format(round((float(cytosine_count)/seq_lenght)*100, 2)), " %", file=f)
f.close()