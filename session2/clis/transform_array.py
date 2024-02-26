import argparse
import numpy as np

# Command-line inputs
parser = argparse.ArgumentParser('CSV I/O Path')
parser.add_argument('input_array_path', type=str, help='Path to input npy file')
parser.add_argument('output_array_path', type=str, help='Path to output npy file')
parser.add_argument('transform', type=str, choices=["norm", "std"], help='Normalize (norm) or standardize (std)')
args = parser.parse_args()

if args.transform == 'norm':
    output_array_path = args.output_array_path + 'norm_array.npy'
    input_array = np.load(args.input_array_path)
    output_array = input_array - np.min(input_array)
    output_array = output_array / np.max(output_array)

if args.transform == 'std':
    output_array_path = args.output_array_path + 'std_array.npy'
    input_array = np.load(args.input_array_path)
    output_array = (input_array - np.mean(input_array)) / np.std(input_array)
    np.save(output_array_path, output_array)    

np.save(output_array_path, output_array)