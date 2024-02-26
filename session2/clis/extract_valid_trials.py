import argparse
import pandas as pd

parser = argparse.ArgumentParser('CSV I/O Path')
parser.add_argument('input_csv_path', type=str, help='Path to input CSV file')
parser.add_argument('output_csv_path', type=str, help='Path to output CSV file')
args = parser.parse_args()

# Load the csv file and extract active trials
df = pd.read_csv(args.input_csv_path)
df_valid = df[df.valid].copy()

# Save the new dataframe as a csv file
df_valid.to_csv(args.output_csv_path, index=False)