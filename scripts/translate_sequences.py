from Bio import SeqIO
from Bio.Seq import Seq

for record in SeqIO.parse("data/raw_sequences/mc1R_dark_allele.fasta", "fasta"):
 mc1R_dark_seq = record.seq

for record in SeqIO.parse("data/raw_sequences/mc1R_light_allele.fasta", "fasta"):
 mc1R_light_seq = record.seq

# This is the recommended way to translate the dna sequence
light_pigment = mc1R_light_seq.translate()
dark_pigment = mc1R_dark_seq.translate()

# custom code to translate amino acid
def translate(dna_seq):
 codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
  }
 protein_seq = ""
 codon = 3
 for nucleotide in range(0, len(dna_seq) - codon + 1, codon):
  window = dna_seq[nucleotide: nucleotide + codon]
  if window in codon_table:
   protein_seq += codon_table[window]
 return protein_seq  


# with open("data/processed_sequences/mc1R_dark_allele_protein_seq.txt", "w") as dark_pigment:
#  dark_pigment.write(translate(mc1R_dark_seq))

# with open("data/processed_sequences/mc1R_light_allele_protein_seq.txt", "w") as light_pigment:
#  light_pigment.write(translate(mc1R_light_seq))


