from pathlib import Path
from Bio import SeqIO

#  Comparing protein sequences
mc1R_dark_allele = Path("data/processed_sequences/mc1R_dark_allele_protein_seq.txt").read_text().strip()
mc1R_light_allele = Path("data/processed_sequences/mc1R_light_allele_protein_seq.txt").read_text().strip()
mutations = []

for amino_acid in range(len(mc1R_dark_allele)):
    if mc1R_dark_allele[amino_acid] != mc1R_light_allele[amino_acid]:
        mutation_info = (
            f"At position {amino_acid + 1}, amino acid changed from {mc1R_dark_allele[amino_acid]} to {mc1R_light_allele[amino_acid]}" 
            )
        mutations.append(mutation_info)
for m in mutations:
    print(m)
