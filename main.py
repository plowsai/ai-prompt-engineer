import argparse
from convert_to_xlxs import convert_to_xlxs
from instruct_to_base import instruct_to_base

def main():
    parser = argparse.ArgumentParser(description='Convert system prompts.')
    parser.add_argument('--xlxs', action='store_true', help='Convert to XLSX')
    parser.add_argument('--instructtobase', action='store_true', help='Convert to Base')
    args = parser.parse_args()

    if args.xlxs:
        result = convert_to_xlxs("Input data for XLSX conversion")
        print(result)
    elif args.instructtobase:
        result = instruct_to_base("Input data for Base conversion")
        print(result)
    else:
        print("Please specify a conversion type.")

if __name__ == "__main__":
    main()
