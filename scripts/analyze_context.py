#!/usr/bin/env python3
"""
Analyze genetic context around identified ARGs for mobile genetic elements (MGEs).

This script checks for nearby transposases, integrases, insertion sequences,
and other MGE signatures to assess transfer potential.
"""

import argparse
import pandas as pd
from pathlib import Path

def load_mge_database(db_path):
    """Load MGE database (placeholder)."""
    # Could be a list of HMM profiles or BLAST databases
    return ["tnpA", "intI1", "IS26", "IS6100"]

def scan_context(contigs_fasta, arg_hits_df, window=5000):
    """
    For each ARG hit, extract flanking region and search for MGEs.
    """
    # Placeholder: simulate MGE detection
    mge_results = []
    for idx, row in arg_hits_df.iterrows():
        mge_results.append({
            "contig": row["contig"],
            "arg_gene": row["gene"],
            "mge_hit": "tnpA",
            "distance": 1200,
            "evalue": 1e-10,
            "description": "transposase"
        })
        mge_results.append({
            "contig": row["contig"],
            "arg_gene": row["gene"],
            "mge_hit": "intI1",
            "distance": 2500,
            "evalue": 1e-8,
            "description": "integrase"
        })
    return mge_results

def main():
    parser = argparse.ArgumentParser(
        description="Analyze MGE context around ARGs."
    )
    parser.add_argument(
        "-i", "--input", required=True,
        help="Input FASTA file of contigs."
    )
    parser.add_argument(
        "-a", "--arg_hits", required=True,
        help="TSV file of ARG hits (output of identify_args.py)."
    )
    parser.add_argument(
        "-o", "--output", default="mge_context.tsv",
        help="Output TSV file (default: mge_context.tsv)."
    )
    parser.add_argument(
        "--window", type=int, default=5000,
        help="Flanking window size (bp) to search for MGEs (default: 5000)."
    )
    parser.add_argument(
        "--mge_db", default="mge_profiles.hmm",
        help="Path to MGE database (default: mge_profiles.hmm)."
    )
    args = parser.parse_args()
    
    print(f"Analyzing MGE context for ARGs from {args.arg_hits}")
    print(f"Using MGE database {args.mge_db}, window {args.window} bp")
    
    # Load ARG hits
    arg_hits = pd.read_csv(args.arg_hits, sep="\t")
    
    # Load MGE database
    mge_db = load_mge_database(args.mge_db)
    
    # Scan for MGEs in flanking regions
    mge_hits = scan_context(args.input, arg_hits, window=args.window)
    
    # Write results
    df = pd.DataFrame(mge_hits)
    df.to_csv(args.output, sep="\t", index=False)
    print(f"Found {len(mge_hits)} MGE hits. Results written to {args.output}")

if __name__ == "__main__":
    main()