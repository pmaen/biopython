from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import fastaparser
filename = input("Please enter the full path of the amino acid sequence file!: ")
type = input("Do you intend a sequence-by-sequence or full analysis (only basic features)?\n     (1) sequence-by-sequence\n     (2) full\n")
if type == "1":
    f = open(filename + "_analysis.txt","w+")
    for record in SeqIO.parse(filename, 'fasta'):
        X = ProteinAnalysis(str(record.seq))
        print('\n### Results for record: {} ###'.format(record.id))
        print("G: ", X.count_amino_acids()['G'], file=f)
        print("A: ",X.count_amino_acids()['A'], file=f)
        print("L: ",X.count_amino_acids()['L'], file=f)
        print("M: ",X.count_amino_acids()['M'], file=f)
        print("F: ",X.count_amino_acids()['F'], file=f)
        print("W: ",X.count_amino_acids()['W'], file=f)
        print("K: ",X.count_amino_acids()['K'], file=f)
        print("Q: ",X.count_amino_acids()['Q'], file=f)
        print("E: ",X.count_amino_acids()['E'], file=f)
        print("S: ",X.count_amino_acids()['S'], file=f)
        print("P: ",X.count_amino_acids()['P'], file=f)
        print("V: ",X.count_amino_acids()['V'], file=f)
        print("I: ",X.count_amino_acids()['I'], file=f)
        print("C: ",X.count_amino_acids()['C'], file=f)
        print("Y: ",X.count_amino_acids()['Y'], file=f)
        print("H: ",X.count_amino_acids()['H'], file=f)
        print("R: ",X.count_amino_acids()['R'], file=f)
        print("N: ",X.count_amino_acids()['N'], file=f)
        print("D: ",X.count_amino_acids()['D'], file=f)
        print("T: ",X.count_amino_acids()['T'], file=f)
        #print("B: ",X.count_amino_acids()['B'], file=f)
        #print("J: ",X.count_amino_acids()['J'], file=f)
        #print("O: ",X.count_amino_acids()['O'], file=f)
        #print("U: ",X.count_amino_acids()['U'], file=f)
        #print("Z: ",X.count_amino_acids()['Z'], file=f)
        print("G%: ","%0.2f" % X.get_amino_acids_percent()['G'], file=f)
        print("A%: ","%0.2f" % X.get_amino_acids_percent()['A'], file=f)
        print("L%: ","%0.2f" % X.get_amino_acids_percent()['L'], file=f)
        print("M%: ","%0.2f" % X.get_amino_acids_percent()['M'], file=f)
        print("F%: ","%0.2f" % X.get_amino_acids_percent()['F'], file=f)
        print("W%: ","%0.2f" % X.get_amino_acids_percent()['W'], file=f)
        print("K%: ","%0.2f" % X.get_amino_acids_percent()['K'], file=f)
        print("Q%: ","%0.2f" % X.get_amino_acids_percent()['Q'], file=f)
        print("E%: ","%0.2f" % X.get_amino_acids_percent()['E'], file=f)
        print("S%: ","%0.2f" % X.get_amino_acids_percent()['S'], file=f)
        print("P%: ","%0.2f" % X.get_amino_acids_percent()['P'], file=f)
        print("V%: ","%0.2f" % X.get_amino_acids_percent()['V'], file=f)
        print("I%: ","%0.2f" % X.get_amino_acids_percent()['I'], file=f)
        print("C%: ","%0.2f" % X.get_amino_acids_percent()['C'], file=f)
        print("Y%: ","%0.2f" % X.get_amino_acids_percent()['Y'], file=f)
        print("H%: ","%0.2f" % X.get_amino_acids_percent()['H'], file=f)
        print("R%: ","%0.2f" % X.get_amino_acids_percent()['R'], file=f)
        print("N%: ","%0.2f" % X.get_amino_acids_percent()['N'], file=f)
        print("D%: ","%0.2f" % X.get_amino_acids_percent()['D'], file=f)
        print("T%: ","%0.2f" % X.get_amino_acids_percent()['T'], file=f)
        #print("B: ","%0.2f" % X.get_amino_acids_percent()['B'], file=f)
        #print("J: ","%0.2f" % X.get_amino_acids_percent()['J'], file=f)
        #print("O: ","%0.2f" % X.get_amino_acids_percent()['O'], file=f)
        #print("U: ","%0.2f" % X.get_amino_acids_percent()['U'], file=f)
        #print("Z: ","%0.2f" % X.get_amino_acids_percent()['Z'], file=f)
        print("molceular weight: ","%0.2f" % X.molecular_weight(), file=f)
        print("araomaticity: ","%0.2f" % X.aromaticity(), file=f)
        print("instability index: ","%0.2f" % X.instability_index(), file=f)
        print("isoelectric point: ","%0.2f" % X.isoelectric_point(), file=f)
        sec_struc = X.secondary_structure_fraction()
        print("secondary structure fraction: ","%0.2f" % sec_struc[0], file=f)
        epsilon_prot = X.molar_extinction_coefficient()
        print("molar extinction coefficient (0): ",epsilon_prot[0], file=f)
        print("molar extinction coefficient (1): ",epsilon_prot[1], file=f)
    f.close()
if type == "2":
    f2= open(filename + ".txt",'w')
    with open(filename) as fasta_file:
        parser = fastaparser.Reader(fasta_file, parse_method='quick')
        for seq in parser:
            # seq is a namedtuple('Fasta', ['header', 'sequence'])
            f2.write(seq.sequence)
    f2.close()
    ffull= open(filename + "_analysis_full.txt","w+")
    seqsource = open(filename + ".txt")
    seq = seqsource.read()
    G_count = 0
    A_count = 0
    L_count = 0
    M_count = 0
    F_count = 0
    W_count = 0
    K_count = 0
    Q_count = 0
    E_count = 0
    S_count = 0
    P_count = 0
    V_count = 0
    I_count = 0
    C_count = 0
    Y_count = 0
    H_count = 0
    R_count = 0
    N_count = 0
    D_count = 0
    T_count = 0
    B_count = 0
    J_count = 0
    O_count = 0
    U_count = 0
    Z_count = 0

    for b in seq:
        if b == 'G':
            G_count += 1
        elif b == 'A':
            A_count +=1
        elif b == 'L':
            L_count +=1
        elif b == 'M':
            M_count +=1
        elif b == 'F':
            F_count +=1
        elif b == 'W':
            W_count +=1
        elif b == 'K':
            K_count +=1
        elif b == 'Q':
            Q_count +=1
        elif b == 'E':
            E_count +=1
        elif b == 'S':
            S_count +=1
        elif b == 'P':
            P_count +=1
        elif b == 'V':
            V_count +=1
        elif b == 'I':
            I_count +=1
        elif b == 'C':
            C_count +=1
        elif b == 'Y':
            Y_count +=1
        elif b == 'H':
            H_count +=1
        elif b == 'R':
            R_count +=1
        elif b == 'N':
            N_count +=1
        elif b == 'D':
            D_count +=1
        elif b == 'T':
            T_count +=1
        elif b == 'B':
            B_count +=1
        elif b == 'J':
            J_count +=1
        elif b == 'O':
            O_count +=1
        elif b == 'U':
            U_count +=1
        elif b == 'Z':
            Z_count +=1

    seq_lenght = len(seq)
    #print("Analysis of ", , "amino acids finished.", file=ffull)
    print("GLYCINE\n     number of Glycines: ", int(G_count) , "\n     Glycine quota: ", "{:.2f}".format(round((float(G_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("ALANINE\n     number of Alanines: ", int(A_count) , "\n     Alanine quota: ", "{:.2f}".format(round((float(A_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("LEUCINE\n     number of Leucines: ", int(L_count) , "\n     Leucine quota: ", "{:.2f}".format(round((float(L_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("METHIONINE\n     number of Methionines: ", int(M_count) , "\n     Methionine quota: ", "{:.2f}".format(round((float(M_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("PHENYLALANINE\n     number of Phenylalanines: ", int(F_count) , "\n     Phenylalanine quota: ", "{:.2f}".format(round((float(F_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("TRYPTOPHAN\n     number of Tryptophans: ", int(W_count) , "\n     Tryptophan quota: ", "{:.2f}".format(round((float(W_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("LYSINE\n     number of Lysines: ", int(K_count) , "\n     Lysine quota: ", "{:.2f}".format(round((float(K_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("GLUTAMINE\n     number of Glutamines: ", int(Q_count) , "\n     Glutamine quota: ", "{:.2f}".format(round((float(Q_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("GLUTAMIC ACID\n     number of Glutamic Acids: ", int(E_count) , "\n     Glutamic Acid quota: ", "{:.2f}".format(round((float(E_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("SERINE\n     number of Serines: ", int(S_count) , "\n     Serine quota: ", "{:.2f}".format(round((float(S_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("PROLINE\n     number of Prolines: ", int(P_count) , "\n     Proline quota: ", "{:.2f}".format(round((float(P_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("VALINE\n     number of Valines: ", int(V_count) , "\n     Valine quota: ", "{:.2f}".format(round((float(V_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("ISOLEUCINE\n     number of Isoleucines: ", int(I_count) , "\n     Isoleucine quota: ", "{:.2f}".format(round((float(I_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("CYSTEINE\n     number of Cysteines: ", int(C_count) , "\n     Cysteine quota: ", "{:.2f}".format(round((float(C_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("TYROSINE\n     number of Tyrosines: ", int(Y_count) , "\n     Tyrosine quota: ", "{:.2f}".format(round((float(Y_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("HISTIDINE\n     number of Histidines: ", int(H_count) , "\n     Histidine quota: ", "{:.2f}".format(round((float(H_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("ARGININE\n     number of Arginines: ", int(R_count) , "\n     Arginine quota: ", "{:.2f}".format(round((float(R_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("ASPARAGINE\n     number of Asparagines: ", int(N_count) , "\n     Asparagine quota: ", "{:.2f}".format(round((float(N_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("ASPARTIC ACID\n     number of Aspartic Acids: ", int(D_count) , "\n     Aspartic Acid quota: ", "{:.2f}".format(round((float(D_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("THREONINE\n     number of Threonines: ", int(T_count) , "\n     Threonine quota: ", "{:.2f}".format(round((float(T_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("ASPARTIC ACID OR ASPARAGINE\n     number of Aspartic Acids or Asparagines: ", int(B_count) , "\n     Aspartic Acid or Asparagine quota: ", "{:.2f}".format(round((float(B_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("LEUCINE OR ISOLEUCINE\n     number of Leucines or Isoleucines: ", int(J_count) , "\n     Leucine or Isoleucine quota: ", "{:.2f}".format(round((float(J_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("PYRROLYSINE\n     number of Pyrrolysines: ", int(O_count) , "\n     Pyrrolysine quota: ", "{:.2f}".format(round((float(O_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("SELENOCYSTEINE\n     number of Selenocysteines: ", int(U_count) , "\n     Selenocysteine quota: ", "{:.2f}".format(round((float(U_count)/seq_lenght)*100, 2)), " %", file=ffull)
    print("GLUTAMIC ACID OR GLUTAMINE\n     number of Glutamic Acids or Glutamines: ", int(Z_count) , "\n     Glutamic Acid or Glutamine quota: ", "{:.2f}".format(round((float(Z_count)/seq_lenght)*100, 2)), " %", file=ffull)
    ffull.close()