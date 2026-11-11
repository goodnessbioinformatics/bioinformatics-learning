# MC1R Gene Sequence Analysis in Rock Pocket Mice

*A Python and Biopython project investigating genetic variation associated with adaptive pigmentation.*

## About the Project

Genetics has always been one of the areas of biology I find particularly fascinating. The idea that an organism's characteristics can be influenced by variations in its DNA, and that even a small change in a nucleotide sequence can potentially affect the resulting protein, is something I find incredibly interesting.

My academic background in Medical Biochemistry and Genetics further developed this interest, particularly in understanding how genetic information is stored, expressed, and translated into functional biological molecules.

As I continue developing my skills in Python and bioinformatics, I wanted to explore a biological question that would allow me to combine my interest in genetics with practical computational analysis.

While researching possible topics, I came across the rock pocket mouse (*Chaetodipus intermedius*) and the fascinating phenomenon of adaptive melanism.

These mice can have different coat colours depending on their environment. Researchers have investigated how genetic variations contribute to these differences, particularly in the melanocortin-1 receptor (MC1R) gene.

The work of Nachman, Hoekstra, and D'Agostino (2003), which investigated the genetic basis of adaptive melanism in pocket mice, particularly caught my attention.

I found the topic interesting because it demonstrates how genetic variation can be connected to observable biological characteristics and how evolutionary processes can shape populations over time.

This project became an opportunity to investigate some of those findings independently using Python and Biopython.

## Research Objective

The primary objective of this project was to investigate sequence variation in the MC1R gene by comparing two nucleotide sequences obtained from the NCBI GenBank database.

Specifically, I aimed to:

- Retrieve MC1R nucleotide sequences from NCBI using Entrez.
- Process and compare the sequences to identify nucleotide differences.
- Investigate the corresponding codon changes.
- Translate the coding sequences to identify resulting amino acid substitutions.
- Use BLAST to examine sequence similarity and support sequence verification.
- Compare my observations with the findings reported by Nachman et al. (2003).

## Tools and Technologies


- Python - Programming and sequence analysis 
- Biopython - Biological sequence processing and translation 
- NCBI Entrez - Retrieving nucleotide sequences 
- NCBI GenBank - Accessing biological sequence records 
- BLAST - Sequence similarity and verification 
- Git and GitHub - Version control and project documentation 

## Methodology

The investigation followed these main steps:

**1. Sequence Retrieval**

Two MC1R nucleotide records were retrieved from NCBI GenBank using their accession numbers:

- AY247575.1
- AY258909.1

NCBI Entrez and Biopython were used to retrieve and process the records.

**2. Sequence Processing and Comparison**

The retrieved sequences were extracted and processed in Python. Their nucleotide sequences were compared to identify differences between the two records.

**3. Codon Extraction and Translation**

The identified nucleotide differences were investigated at the codon level.

Biopython's sequence translation functionality was used to determine whether the nucleotide substitutions resulted in changes to the encoded amino acids.

**4. BLAST Verification**

BLAST was used to examine sequence similarity and support the verification of the retrieved sequences.

**5. Comparison with Published Research**

The observed nucleotide and amino acid variations were compared with the findings of Nachman et al. (2003), particularly the reported MC1R amino acid differences associated with dark pigmentation in the Pinacate population.

## Key Findings

The comparison identified six nucleotide differences between the two MC1R sequences examined.

Further investigation through codon translation revealed:

- **Five nonsynonymous substitutions:** Nucleotide changes that resulted in different amino acids.
- **One synonymous substitution:** A nucleotide change that did not alter the encoded amino acid.

Four of the five observed amino acid substitutions corresponded to the four amino acid positions reported by Nachman et al. (2003) in association with dark pigmentation in the Pinacate population.

An additional amino acid substitution, Alanine to Serine at position 105, was also observed.

The synonymous substitution at amino acid position 211 provided another interesting observation, demonstrating that nucleotide variation does not always result in a change to the encoded protein.

For the complete mutation table, comparison with published findings, and detailed interpretation, see results/results.md.

## What I Learned

This project was an important learning experience in my development as an aspiring bioinformatics professional.

Beyond writing Python code, it helped me appreciate the relationship between nucleotide variation, codons, amino acids, and protein sequences.

Some of the key concepts and practical skills I developed include:

- Retrieving biological sequences programmatically using NCBI Entrez.
- Working with FASTA records and Biopython SeqRecord objects.
- Extracting and manipulating nucleotide sequences in Python.
- Identifying nucleotide substitutions through sequence comparison.
- Understanding the relationship between codons and amino acids.
- Distinguishing synonymous and nonsynonymous substitutions.
- Using BLAST for sequence similarity analysis.
- Interpreting computational findings in the context of published biological research.
- Understanding the importance of scientific attribution and reproducibility.

One particularly interesting lesson was discovering that not every nucleotide substitution changes the resulting amino acid. This helped me better understand the genetic code and the different ways mutations can influence biological information.

The project also reinforced the importance of investigating published research rather than simply accepting computational results at face value.

## Scientific Considerations and Limitations

This project is an independent computational investigation based on two publicly available MC1R sequence records.

The observed sequence differences should not automatically be interpreted as mutations responsible for dark pigmentation.

Although four of the observed amino acid substitutions correspond to positions discussed in the published study, the functional significance of the additional substitution has not been established.

Furthermore, BLAST sequence similarity does not independently establish specimen identity, geographical origin, or pigmentation phenotype. These require verification against the original GenBank records and associated research.

No laboratory experiments or functional assays were performed as part of this investigation.

## References and Acknowledgements

This project was inspired by the published research of:

Nachman, M. W., Hoekstra, H. E., & D'Agostino, S. L. (2003). The genetic basis of adaptive melanism in pocket mice. Proceedings of the National Academy of Sciences, 100(9), 5268–5273.
https://pmc.ncbi.nlm.nih.gov/articles/PMC154334/ 

I acknowledge the original researchers for their contributions to understanding the genetic basis of adaptive melanism. Their published work provided the scientific foundation and reference point for this independent computational investigation.

I also acknowledge the National Center for Biotechnology Information (NCBI) for providing access to publicly available nucleotide sequence data and the Biopython development team for making valuable computational biology tools available to the research community.

For additional literature and software references, see references/references.md.
