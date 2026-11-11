# Results and Interpretation: MC1R Sequence Variation in Rock Pocket Mice

## 1. Overview

This project investigates sequence variation in the melanocortin-1 receptor (MC1R) gene of the rock pocket mouse (*Chaetodipus intermedius*), with particular interest in genetic variations associated with adaptive melanism (dark pigmentation).

The analysis uses Python and Biopython to retrieve, process, compare, and translate MC1R nucleotide sequences obtained from the National Center for Biotechnology Information (NCBI).

The primary scientific reference for this investigation is:

Nachman, M. W., Hoekstra, H. E., & D'Agostino, S. L. (2003). The genetic basis of adaptive melanism in pocket mice. *Proceedings of the National Academy of Sciences*, 100(9), 5268–5273. https://www.pnas.org/doi/full/10.1073/pnas.0431157100, https://pmc.ncbi.nlm.nih.gov/articles/PMC154334/

## 2. Sequence Retrieval and Comparison

Two MC1R nucleotide sequences were retrieved from the NCBI GenBank database:

- Dark sequence (working designation): AY247575.1
- Light sequence (working designation): AY258909.1
- Organism: *Chaetodipus intermedius*
- Gene: MC1R

The sequences were retrieved using NCBI Entrez and processed using Biopython.

Nucleotide-level comparison was performed to identify sequence differences between the two records. BLAST was also used to examine sequence similarity and support the sequence comparison.

The corresponding coding sequences were translated to investigate whether the identified nucleotide substitutions resulted in amino acid changes.

## 3. Observed Nucleotide and Amino Acid Variations

The sequence comparison identified six nucleotide differences between the two MC1R sequences examined.

Translation of the corresponding codons revealed five nonsynonymous substitutions, resulting in amino acid changes, and one synonymous substitution, which did not alter the encoded amino acid.

The observed variations are presented below.

| No. | Nucleotide position | DNA change (Dark → Light) | Dark codon | Light codon | Amino acid position | Amino acid change (Dark → Light) | Classification |
| 1 | 52 | C → T | CGC | TGC | 18 | Arg → Cys | Nonsynonymous |
| 2 | 313 | G → T | GCC | TCC | 105 | Ala → Ser | Nonsynonymous |
| 3 | 325 | C → T | CGG | TGG | 109 | Arg → Trp | Nonsynonymous |
| 4 | 478 | C → T | CGG | TGG | 160 | Arg → Trp | Nonsynonymous |
| 5 | 633 | T → C | CTT | CTC | 211 | Leu → Leu | Synonymous |
| 6 | 699 | A → C | CAA | CAC | 233 | Gln → His | Nonsynonymous |

*Note: Nucleotide positions are numbered relative to the MC1R coding sequence. Amino acid positions refer to the translated MC1R protein. Amino acid abbreviations follow the standard three-letter and one-letter conventions.*

## 4. Comparison with Published Findings

Nachman et al. (2003) investigated MC1R sequence variation in several populations of rock pocket mice, including the Pinacate lava flow in Arizona and the Pedro Armendaris lava flow in New Mexico.

Their study identified four amino acid polymorphisms associated with dark pigmentation in the Pinacate population.

The published differences between the light and dark MC1R alleles were:

| Amino acid position | Light allele (d) | Dark allele (D) |
| 18 | Cysteine (Cys) | Arginine (Arg) |
| 109 | Tryptophan (Trp) | Arginine (Arg) |
| 160 | Tryptophan (Trp) | Arginine (Arg) |
| 233 | Histidine (His) | Glutamine (Gln) |

The study also demonstrated that the dark MC1R allele (D) was dominant over the light allele (d) in the Pinacate population.

The observed genotype–phenotype associations were:

- DD: Dark pigmentation
- Dd: Dark pigmentation
- dd: Light pigmentation

The four amino acid substitutions were in complete linkage disequilibrium, meaning they were inherited together in the sampled Pinacate population.

### Comparison of the present findings with the published study

Four of the five amino acid substitutions identified in this investigation correspond to the four positions reported by Nachman et al. (2003).

These are:

1. Position 18: Cysteine ↔ Arginine.
2. Position 109: Tryptophan ↔ Arginine.
3. Position 160: Tryptophan ↔ Arginine.
4. Position 233: Histidine ↔ Glutamine.

An additional amino acid substitution was identified at position 105, involving Alanine and Serine. This substitution was not among the four amino acid differences specifically associated with dark pigmentation in the original study.

## 5. Interpretation of Observed Differences

The identification of six nucleotide differences and five amino acid substitutions demonstrates the importance of examining genetic variation at both nucleotide and protein levels.

### 5.1 Nonsynonymous substitutions

Five of the six nucleotide differences resulted in changes to the encoded amino acids.

Four correspond to the amino acid positions associated with dark pigmentation in the Pinacate population, as reported by Nachman et al. (2003).

The fifth substitution, Ala105Ser, represents an additional amino acid difference between the two sequences examined.

Although this substitution changes the encoded amino acid, its functional significance and relationship with pigmentation have not been established.

It should therefore be considered an observed sequence variation rather than a confirmed pigmentation-associated mutation.

### 5.2 Synonymous substitution

The nucleotide difference at position 633 involved a codon change from CTT to CTC.

Both codons encode Leucine (Leu), meaning the nucleotide substitution did not alter the resulting amino acid.

This is classified as a synonymous substitution.

Interestingly, Nachman et al. (2003) also discussed a silent polymorphic site at nucleotide position 633, which was in complete linkage disequilibrium with the amino acid substitutions associated with the dark haplotype in the Pinacate population.

This provides an additional point of comparison between the present observations and the published research.

### 5.3 Geographical variation and adaptive melanism

An important finding of Nachman et al. (2003) was that dark pigmentation in different populations of rock pocket mice did not necessarily have the same genetic basis.

While MC1R variation was strongly associated with dark pigmentation in the Pinacate population, the researchers did not find the same association in the Pedro Armendaris population.

This demonstrates that similar pigmentation phenotypes can evolve through different genetic mechanisms.

Consequently, the geographical origin and biological characteristics of the specimens are important when interpreting MC1R sequence variations.

## 6. Limitations

Although this investigation identified nucleotide and amino acid differences between the two MC1R sequences, several limitations should be considered:

1. Sequence similarity established through BLAST does not independently establish the pigmentation phenotype or geographical origin of a specimen.
2. The presence of an amino acid substitution does not automatically establish its functional effect on the MC1R protein.
3. The additional Ala105Ser substitution requires further investigation before any association with pigmentation can be proposed.
4. Sequence comparisons involving individual records cannot independently establish population-wide genetic associations.
5. The analysis does not experimentally establish the contribution of individual amino acid substitutions to MC1R receptor activity or pigmentation.

Further functional investigation would be required to establish the biological significance of the additional amino acid substitution.

## 7. Conclusion

This investigation demonstrates the application of Python and Biopython in examining genetic variation within the MC1R gene of rock pocket mice.

Six nucleotide differences were identified between the two sequences examined. Translation of the corresponding codons revealed five nonsynonymous amino acid substitutions and one synonymous substitution.

Four of the observed amino acid substitutions corresponded to the four MC1R amino acid differences associated with dark pigmentation in the Pinacate population, as reported by Nachman et al. (2003).

An additional Ala105Ser substitution was identified, alongside a synonymous variation at nucleotide position 633.

The findings demonstrate how nucleotide-level differences can translate into protein-level variation and how computational sequence analysis can be used to investigate established biological discoveries.

The investigation also highlights the importance of distinguishing observed genetic variation from experimentally established functional effects when interpreting the molecular basis of adaptive pigmentation.

## 8. References

For the complete list of scientific literature, database resources, and software references consulted during this investigation, see the [References page](references.md).