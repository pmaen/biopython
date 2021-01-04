from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import fastaparser
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import os
import sys
import argparse
pd.set_option('display.max_columns', None)
# integrate check for existance
directory = input("Please enter the directory of the amino acid sequence file!: ")
filename_raw = input("Please enter the name of the amino acid sequence file without extension!: ")
ext = input("Please enter the file extension!: ")

filename = directory + "/" + filename_raw + "." + ext
pH_input = input("At which pH should the analysis be conducted? ")
flexibility_ynu = input("Do you wish a flexibility analysis?\n   (1) Yes\n   (0) No\n")

if pH_input == "":
    pH= 7.4
elif pH_input != "":
    pH = pH_input
    
#Parser
import os 
os.chdir(directory)
os.mkdir(directory + "/"+ filename_raw +"_split")
outfile = os.chdir(directory + "/"+ filename_raw +"_split")

import sys
infile = open(directory + "/" + filename_raw + "." + ext)
outfile = []

for line in infile:
    if line.startswith(">"):
        if (outfile != []): outfile.close()
        genename = line.strip().split('|')[1].split('[')[0].strip()
        filename_export = genename+".fasta"
        outfile = open(filename_export,'w')
        outfile.write(line)
    else:
        outfile.write(line)
outfile.close()
for idx, somefile in enumerate(os.listdir(directory + "/"+ filename_raw +"_split")):
    f = open(filename + "_analysis.txt","w+")
    for record in SeqIO.parse(somefile, 'fasta'):
        X = ProteinAnalysis(str(record.seq))
        print("ANALYSIS OF", record, "\n ----------- \n -----------", file=f)
        #
        pd_count_amino_acids = pd.DataFrame(X.count_amino_acids(), index=[1])
        print("number of amino acids: \n",pd_count_amino_acids , file=f)
        plt_acc = pd_count_amino_acids.plot.bar()
        plt.savefig(somefile + "_count_amino_acids_plot_" + str(idx) + ".pdf")
        #
        pd_get_amino_acids_percent = pd.DataFrame(X.get_amino_acids_percent(), index=[1])
        print("\n percentage of amino acids: \n", pd_get_amino_acids_percent, file=f)
        plt_acp = pd_get_amino_acids_percent.plot.bar()
        plt.savefig(somefile + "amino_acids_percent_plot_" + str(idx) + ".pdf")
        #
        print("\n molecular weight: {:.2f}".format(X.molecular_weight()), file=f)
        print("\n aromaticity: {:.2f}".format(X.aromaticity()), file=f)
        print("\n instability index: {:.2f}".format(X.instability_index()), file=f)
        if flexibility_ynu == "1":
            print("\n flexibility: ", X.flexibility(), file=f)
        print("\n IEP: ", X.isoelectric_point(), file=f)
        print("therefore its charge at pH = ",pH," is {:.2f}".format(X.charge_at_pH(pH)), file=f)
        print("secondary structure fraction: (Helix, Turn, Sheet): ", X.secondary_structure_fraction(), "\n\n\n", file=f)
    f.close()
    print("done")
