# Methodology and Assumptions

## Overview
This document outlines the theoretical background and methodological assumptions underlying the IncQ‑ARG characterization workflow.

## 1. IncQ Plasmid Identification
**IncQ plasmids** are small, broad‑host‑range plasmids that often carry antibiotic resistance genes. They are defined by a specific replicon sequence (`rep` gene) that can be used for identification.

- **Replicon database:** A curated set of IncQ replicon sequences (e.g., from PlasmidFinder or NCBI) serves as the reference.
- **Detection method:** Sequence similarity search (BLAST or minimap2) is used to find matches between contigs and the replicon database.
- **Thresholds:** Typical criteria include ≥90% identity over ≥80% of the replicon length. Hits are filtered by e‑value (e.g., <1e‑10).

## 2. Antibiotic Resistance Gene Detection
**ARGs** are identified using publicly available reference databases.

- **Common databases:**
  - **CARD** (Comprehensive Antibiotic Resistance Database): provides curated sequences and HMM profiles.
  - **ResFinder:** focuses on acquired resistance genes.
  - **NCBI’s Bacterial Antimicrobial Resistance Reference Gene Database**.
- **Search tools:** BLAST (blastn, blastx), DIAMOND (fast protein search), or HMMER (profile HMMs).
- **Parameters:** Default cut‑offs are ≥90% nucleotide identity and ≥80% coverage, or an e‑value <1e‑5 for protein searches.

## 3. Mobile Genetic Element Context Analysis
**Transfer potential** of an ARG is assessed by examining its genetic neighborhood for signatures of mobility.

- **Mobile genetic elements (MGEs)** include:
  - **Transposases** (e.g., Tn3, IS26)
  - **Integrases** (e.g., class‑1 integrons)
  - **Insertion sequences (IS)**
  - **Plasmid‑specific genes** (e.g., relaxase, conjugative transfer genes)
- **Detection:** HMM profiles (e.g., from MobileElementFinder) or BLAST against a custom MGE database.
- **Window size:** A flanking region of 5 kb upstream and downstream of each ARG is typically scanned.
- **Interpretation:** The presence of multiple MGEs in close proximity to an ARG suggests a high likelihood of horizontal transfer.

## 4. Workflow Assumptions
1. **Contig quality:** Input contigs are assumed to be derived from a gut metagenome assembly of sufficient quality (N50 > 10 kb, low contamination).
2. **Reference databases:** The user must supply appropriate reference files (FASTA for replicons/ARGs, HMM for MGEs). The placeholder scripts expect these files to be present in `data/`.
3. **Tool availability:** The actual implementation requires external binaries (BLAST+, DIAMOND, HMMER, etc.) to be installed and accessible in the PATH.
4. **Parallelism:** The workflow is designed to be run on a single machine; scaling to large datasets would require parallelization (e.g., via Snakemake or Nextflow).

## 5. Limitations
- **False positives/negatives:** Similarity‑based searches may miss divergent sequences or produce spurious matches.
- **Database bias:** The results are only as good as the reference databases used.
- **Context boundaries:** The chosen window size may miss distant regulatory elements that still influence transferability.
- **Plasmid completeness:** The workflow does not attempt to reconstruct full plasmid sequences; it only flags contigs that contain IncQ replicons.

## 6. Future Directions
- Integration with **long‑read metagenomics** to recover complete plasmids.
- **Machine‑learning** approaches to predict transferability from sequence features.
- **Pan‑genome** analysis to track ARG spread across bacterial lineages.

## References
- Carattoli, A. et al. (2014). *PlasmidFinder and pMLST: in silico detection and typing of plasmids*. Antimicrobial Agents and Chemotherapy.
- Alcock, B.P. et al. (2020). *CARD 2020: antibiotic resistome surveillance with the Comprehensive Antibiotic Resistance Database*. Nucleic Acids Research.
- Bortolaia, V. et al. (2020). *ResFinder 4.0 for predictions of phenotypes from genotypes*. Journal of Antimicrobial Chemotherapy.
- Johansson, M.H.K. et al. (2021). *MobileElementFinder: a tool for the detection of mobile genetic elements in assembled sequences*. Microbial Genomics.