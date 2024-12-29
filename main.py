import argparse
from scripts.reader import read_file
from scripts.processor import filter_data
from scripts.writer import save_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process CSV/Excel files.")
    parser.add_argument("input", help="Input file (CSV or Excel).")
    parser.add_argument("output", help="Output file (CSV or Excel
