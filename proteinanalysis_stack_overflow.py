import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# set pandas display option
pd.set_option('display.max_columns', None)

# input selections were removed for testing
filename = input("Please enter the full path of the amino acid sequence file! ")
pH_input = input("At which pH should the analysis be conducted? ")
flexibility_ynu = input("Do you wish a flexibility analysis?\n   (1) Yes\n   (0) No\n")

if pH_input == "":
    pH= 7.4
elif pH_input != "":
    pH = pH_input

for record in SeqIO.parse(filename, 'fasta'):
    # get each record id to be used for unique file names
    record_id = record.id.split('|')[1]
    print(record)
    # open the file and use the record id as part of the name, so there will be a unique file for each id
    with open(f"{filename}_{record_id}_analysis.txt","w+") as f:

        X = ProteinAnalysis(str(record.seq))
        print("ANALYSIS OF", record, "\n ----------- \n -----------", file=f)
        #
        pd_count_amino_acids = pd.DataFrame(X.count_amino_acids(), index=[1])
        print(pd_count_amino_acids)  # display is for jupyter notebook, otherwise use print
        print("number of amino acids: \n",pd_count_amino_acids , file=f)
        plt_acc = pd_count_amino_acids.T.plot.bar(legend=False, figsize=(7, 5))
        plt.title(f'Number of Amino Acids for {record_id} in {filename}')
        plt.xticks(rotation=0)
        # add the record id as part of the file name
        plt.savefig(f'{filename}_{record_id}_count_amino_acids_plot.pdf')
        #
        pd_get_amino_acids_percent = pd.DataFrame(X.get_amino_acids_percent(), index=[1])
        print(pd_get_amino_acids_percent.round(2))  # display is for jupyter notebook, otherwise use print
        print("\n percentage of amino acids: \n", pd_get_amino_acids_percent, file=f)
        plt_acp = pd_get_amino_acids_percent.T.plot.bar(legend=False, figsize=(7, 5))
        plt.title(f'Percentage of Amino Acids for {record_id} in {filename}')
        plt.xticks(rotation=0)
        # add the record id as part of the file name
        plt.savefig(f'{filename}_{record_id}_amino_acids_percent_plot.pdf')
        #
        print("\n molecular weight: {:.2f}".format(X.molecular_weight()), file=f)
        print("\n aromaticity: {:.2f}".format(X.aromaticity()), file=f)
        print("\n instability index: {:.2f}".format(X.instability_index()), file=f)

        if flexibility_ynu == "1":
            print("\n flexibility: ", X.flexibility(), file=f)

        print("\n IEP: ", X.isoelectric_point(), file=f)
        print("therefore its charge at pH = ",pH," is {:.2f}".format(X.charge_at_pH(pH)), file=f)
        print("secondary structure fraction: (Helix, Turn, Sheet): ", X.secondary_structure_fraction(), "\n\n\n", file=f)
        print('\n')