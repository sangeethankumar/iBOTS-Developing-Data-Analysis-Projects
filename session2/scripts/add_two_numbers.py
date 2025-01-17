import argparse

parser = argparse.ArgumentParser(description='add two numbers')
parser.add_argument('num1', type=float, help='Number 1')
parser.add_argument('num2', type=float, help='Number 2')
parser.add_argument('--scale', type=float, default=1.0, help='Scale')

args = parser.parse_args()

print(f"{(args.num1 + args.num2)*args.scale}")