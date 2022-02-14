from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp
from Bio.SeqUtils import GC
import random

seq = input("Please enter the DNA sequence (forward, 5'->3'):\n")
tmin = input("What is the minimal melting temperature you want your primers to have? (standard: 52)\n")
tmax = input("What is the maximal melting temperature you want your primers to have? (standard: 65)\n")
imax = input("How many primers do you want to be put out at max?")
jmax = 10000
if tmin == "":
    tmin = 52
if tmax == "":
    tmax = 65
if imax == "":
    imax = 10
imax = int(imax)
    
seq = Seq(seq)
seq_comp = seq.reverse_complement()

i = 0
j = 0
while (i < imax) and (j < jmax):
    start =  random.randint(0,len(seq))
    end = random.randint(start,len(seq))
    primer = seq[start:end]
    if 30 > len(primer) > 18:
        primer_last = primer[len(primer)-1]
        tm_primer = MeltingTemp.Tm_NN(primer)
        if ((primer[len(primer)-1] == primer[len(primer)-2]) and primer[len(primer)-1] != primer[len(primer)-3]) or (primer[len(primer)-1] != primer[len(primer)-2]):    
            if (tmin < tm_primer < tmax) and (primer_last == "G" or "C") and (40 < GC(primer) < 60):
                print(primer, "\t Tm = %.2f"% tm_primer, "\t GC-content = %.2f"% GC(primer))
                # hier fehlt noch das heraussuchen eines Primers auf dem Gegenstrang, bei dem der Overlap kleiner x ist.
                i +=1
            else:
                j += 1
        else:
            j += 1
if j >= jmax:
    print("No matching primers were found.")
else:
    print("finished")    
