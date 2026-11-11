from Bio import SeqIO, Entrez
Entrez.email = "Isiekwenagbugoodness@gmail.com"

with Entrez.efetch(
    id = "AY247575.1",
    db = "nucleotide",
    rettype = "fasta",
    retmode = "text"
) as mc1R_dark:
    sequence_A = SeqIO.read(mc1R_dark, "fasta")
    SeqIO.write(sequence_A, "data/raw_sequences/mc1R_dark_allele.fasta", "fasta")

with Entrez.efetch(
    id = "AY258909.1",
    db = "nucleotide",
    rettype = "fasta",
    retmode = "text"
) as mc1R_light:
    sequence_B = SeqIO.read(mc1R_light, "fasta")
    SeqIO.write(sequence_B, "data/raw_sequences/mc1R_light_allele.fasta", "fasta")


