from Bio import SeqIO
from Bio.Seq import Seq

#  Comparing protein sequences
mc1R_dark_nucleotide = SeqIO.read("data/raw_sequences/mc1R_dark_allele.fasta", format = "fasta")
mc1R_light_nucleotide = SeqIO.read("data/raw_sequences/mc1R_light_allele.fasta", format = "fasta")

mc1R_dark = mc1R_dark_nucleotide.seq
mc1R_light = mc1R_light_nucleotide.seq
mutations = []

for nucleotide in range(len(mc1R_dark)):
    if mc1R_dark[nucleotide] != mc1R_light[nucleotide]:
        mutation_info = (
            f"At position {nucleotide + 1}, amino acid changed from {mc1R_dark_nucleotide[nucleotide]} to {mc1R_light_nucleotide[nucleotide]}"
            )
        mutations.append(nucleotide + 1)


for mutation in mutations:

    index = mutation - 1

    # Locate the beginning of the affected codon
    codon_start = (index // 3) * 3

    # Extract codons from both sequences
    dark_codon = mc1R_dark[codon_start:codon_start + 3]
    light_codon = mc1R_light[codon_start:codon_start + 3]

    # Translate the codons into amino acids
    dark_aa = Seq(str(dark_codon)).translate()
    light_aa = Seq(str(light_codon)).translate()

    print(f"\nNucleotide mutation: {mutation}")
    print(f"Dark codon: {dark_codon}")
    print(f"Light codon: {light_codon}")
    print(f"Dark amino acid: {dark_aa}")
    print(f"Light amino acid: {light_aa}")
