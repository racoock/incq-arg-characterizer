# IncQ‑ARG Characterizer

A standardized bioinformatics workflow for identifying and characterizing transferrable Antibiotic Resistance Genes (ARGs) located on IncQ plasmids within gut metagenomic contigs.

## Overview

This repository provides a reproducible, version‑controlled pipeline to:
1. **Identify IncQ plasmid replicons** in assembled contigs using sequence similarity.
2. **Detect antibiotic resistance genes** using reference databases (CARD, ResFinder).
3. **Analyze the genetic context** of ARGs for nearby mobile genetic elements (MGEs) that indicate transfer potential.

The workflow is implemented as a set of modular Python scripts orchestrated by a Bash driver script. It is designed for educational purposes and as a template for similar metagenomic analyses.

## Repository Structure

```
incq-arg-characterizer/
├── data/                    # Example input data
│   └── mock_contigs.fasta  # Simulated gut metagenomic contigs
├── scripts/                 # Core analysis modules
│   ├── find_incQ.py        # Identify IncQ replicon sequences
│   ├── identify_args.py    # Detect ARGs via database search
│   └── analyze_context.py  # Scan for MGEs near ARGs
├── run_analysis.sh         # Main workflow driver
├── results/                # Output directory (created during run)
├── LICENSE                 # MIT License
└── README.md               # This file
```

## Quick Start

### Prerequisites
- Python 3.7+ with pandas (optional for placeholder scripts)
- BLAST+ or minimap2 (for actual replicon search)
- DIAMOND or HMMER (for ARG/MGE detection)
- Bash shell

### Running the Example Workflow
1. Clone the repository:
   ```bash
   git clone https://github.com/racoock/incq-arg-characterizer.git
   cd incq-arg-characterizer
   ```
2. Make the driver script executable:
   ```bash
   chmod +x run_analysis.sh
   ```
3. Execute the workflow:
   ```bash
   ./run_analysis.sh
   ```
   The script will run the three analysis steps and write results to the `results/` directory.

**Note:** The current scripts are **placeholders** that simulate the output. To perform real analyses, replace the placeholder logic with calls to appropriate tools (BLAST, DIAMOND, HMMER, etc.) and provide the required reference databases.

## Detailed Usage

### 1. Finding IncQ Replicons
```bash
python scripts/find_incQ.py -i <contigs.fasta> --database <incQ_replicon.fasta> -o <output.tsv>
```
The script searches for IncQ‑specific replicon sequences using BLAST or minimap2.

### 2. Identifying ARGs
```bash
python scripts/identify_args.py -i <contigs.fasta> --database <card.fasta> -o <arg_hits.tsv>
```
Uses a reference ARG database (e.g., CARD) and a similarity search tool to detect resistance genes.

### 3. Analyzing MGE Context
```bash
python scripts/analyze_context.py -i <contigs.fasta> -a <arg_hits.tsv> --mge_db <mge_profiles.hmm> -o <mge_context.tsv>
```
Examines flanking regions of each ARG hit for signatures of transposases, integrases, and other mobile elements.

## Project Management

- **Issues:** Used for tracking tasks and enhancements (see [Issues](https://github.com/racoock/incq-arg-characterizer/issues)).
- **Pull Requests:** All changes are reviewed via PRs before merging into `main`.
- **Releases:** Versioned releases (e.g., v1.0) capture stable states of the workflow.
- **Wiki:** Additional documentation on methodology, databases, and assumptions is maintained in the repository Wiki.

## Contributing

Contributions are welcome! Please open an issue to discuss proposed changes, then submit a pull request against the `main` branch.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Citation

If you use this workflow in teaching or as a template for your research, please cite this repository and acknowledge the original authors.

## Contact

For questions or suggestions, please open an issue on GitHub.