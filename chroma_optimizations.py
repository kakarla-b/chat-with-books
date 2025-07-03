"""
chroma_optimizations.py

Utility script for optimizing text before generating embeddings.
This reduces unnecessary tokens, improves embedding efficiency, and saves memory in vector storage.
"""

import re
import pandas as pd


def clean_text(text: str) -> str:
    """Basic text cleanup: remove special characters, extra whitespace, and lowercases."""
    text = re.sub(r"\s+", " ", text)  # remove extra whitespace
    text = re.sub(r"[^a-zA-Z0-9.,!? ]", "", text)  # remove non-alphanumeric
    return text.strip().lower()


def optimize_dataframe(csv_path: str, text_column: str = "text") -> pd.DataFrame:
    """
    Loads a CSV file and optimizes the text column for embedding.

    Parameters:
        csv_path (str): Path to the CSV file.
        text_column (str): Name of the column containing text.

    Returns:
        pd.DataFrame: Optimized DataFrame with a new 'cleaned_text' column.
    """
    df = pd.read_csv(csv_path)
    if text_column not in df.columns:
        raise ValueError(f"'{text_column}' column not found in CSV.")

    df["cleaned_text"] = df[text_column].astype(str).apply(clean_text)
    return df


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python chroma_optimizations.py <path_to_csv>")
    else:
        path = sys.argv[1]
        optimized_df = optimize_dataframe(path)
        output_path = path.replace(".csv", "_cleaned.csv")
        optimized_df.to_csv(output_path, index=False)
        print(f"Optimized CSV saved to: {output_path}")
