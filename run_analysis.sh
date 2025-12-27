#!/bin/bash
# Main workflow script for IncQ-ARG characterization
# This script orchestrates the three core steps:
# 1. Identify IncQ replicons
# 2. Detect ARGs
# 3. Analyze MGE context

set -euo pipefail

# Configuration
INPUT_FASTA="data/mock_contigs.fasta"
INCQ_DB="data/incQ_replicon.fasta"
ARG_DB="data/card.fasta"
MGE_DB="data/mge_profiles.hmm"
OUTPUT_DIR="results"
mkdir -p "$OUTPUT_DIR"

echo "=== IncQ-ARG Characterization Workflow ==="
echo "Input contigs: $INPUT_FASTA"
echo "Output directory: $OUTPUT_DIR"

# Step 1: Find IncQ replicons
echo "Step 1: Identifying IncQ replicons..."
python scripts/find_incQ.py \
    -i "$INPUT_FASTA" \
    --database "$INCQ_DB" \
    -o "$OUTPUT_DIR/incQ_hits.tsv"

# Step 2: Identify ARGs
echo "Step 2: Identifying ARGs..."
python scripts/identify_args.py \
    -i "$INPUT_FASTA" \
    --database "$ARG_DB" \
    -o "$OUTPUT_DIR/arg_hits.tsv"

# Step 3: Analyze MGE context around ARGs
echo "Step 3: Analyzing MGE context..."
python scripts/analyze_context.py \
    -i "$INPUT_FASTA" \
    -a "$OUTPUT_DIR/arg_hits.tsv" \
    --mge_db "$MGE_DB" \
    -o "$OUTPUT_DIR/mge_context.tsv"

echo "Workflow completed successfully!"
echo "Results saved in $OUTPUT_DIR/"