"""Use csv.reader to review a CSV file."""

import argparse
import csv
from collections import defaultdict
from pathlib import Path

from rich.pretty import pprint

TWO = 2  # just shutting up ruff about magic numbers


def main():
    parser = argparse.ArgumentParser(description="Assess an input CSV file.")

    # Add an argument for the input file
    parser.add_argument(
        "-i",
        "--input",
        type=str,  # The type of the argument (string for file path)
        required=True,  # Make this argument mandatory
        help="Path to the input CSV file to be assessed.",
    )

    args = parser.parse_args()

    # Access the input file path
    input_file_path = args.input

    pprint(f"Assessing CSV file: {input_file_path}")

    # assuming we have enough memory to read the whole file
    print("\n\n")
    pprint("============== BEGINNING READLINES ASSESSMENT ==============")
    pprint("Opening the file with file.readlines()")
    try:
        with Path.open(input_file_path, "r", newline="", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        pprint(f"Error: Input file '{input_file_path}' not found.")
    except OSError as e:
        pprint(f"An error occurred while reading the file: {e}")

    pprint(
        "Was able to open the file using newline = '' and encoding = 'utf-8'",
    )

    first_line = lines[0].strip()

    pprint("Read in all raw lines from the file into a list of strings.")
    pprint("------------------ First line info - Begin --------------")
    pprint("Contains:")
    pprint(first_line)
    pprint(f"Type: {type(first_line)}")
    pprint(f"Length {len(first_line)}")
    sections = first_line.split(",")
    pprint("Sections using split by comma:")
    pprint(sections)
    pprint(f"Number of sections: {len(sections)}")
    pprint("------------------ First line info - End --------------")
    num_lines = sum(1 for _ in lines)
    pprint(f"Total number of lines in the file: {num_lines}")

    # create a func_tools defautldict to hold the counts of each section
    section_counts = defaultdict(int)
    for line in lines:
        section_count = len(line.strip().split(","))
        section_counts[section_count] += 1

    # Grab some examples of lines with different section counts
    example_lines = defaultdict(list)
    for line in lines:
        section_count = len(line.strip().split(","))
        if len(example_lines[section_count]) < TWO:
            example_lines[section_count].append(line.strip())

    pprint("Using raw string proccessing with split by comma to count sections.")
    pprint(
        "Raw string processing is not recommended for CSV files with commas in data because the columns likey won't be spit out correctly.",
    )
    pprint("Section counts:")
    for count, num_lines in section_counts.items():
        pprint(f"Lines with {count} sections: {num_lines}")

    pprint("Example lines for each section count:")
    for count, examples in example_lines.items():
        pprint(f"Lines with {count} sections:")
        for example in examples:
            pprint(f"{example}")

    pprint("============== ENDING READLINES ASSESSMENT ==============")
    print("\n\n")
    pprint("============== BEGINNING CSV READER ASSESSMENT ==============")
    pprint("Attempting to open the file with csv.reader()")
    try:
        with Path.open(input_file_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            pprint("First row using csv.reader():")
            pprint(next(reader))
            # for row in reader:
            #    pprint(row)
            reader_section_counts = defaultdict(int)
            reader_example_lines = defaultdict(list)
            for row in reader:
                reader_section_count = len(row)
                reader_section_counts[reader_section_count] += 1
                if len(reader_example_lines[reader_section_count]) < TWO:
                    reader_example_lines[reader_section_count].append(row)

            pprint("Reader section counts:")
            for count, num_lines in reader_section_counts.items():
                pprint(f"Lines with {count} sections: {num_lines}")

            pprint("Example lines for each reader section count:")
            for count, examples in reader_example_lines.items():
                pprint(f"Rows with {count} sections:")
                for example in examples:
                    pprint(f"{example}")

    except OSError as e:
        pprint(f"An error occurred while opening the file with csv.reader(): {e}")

    pprint(
        "Apparently there were no exceptions while processing the file with csv.reader()",
    )

    pprint("============== ENDING CSV READER ASSESSMENT ==============")
    print("\n\n")
    pprint("============== BEGINNING CSV DICT-READER ASSESSMENT ==============")
    pprint("Attempting to open the file with csv.DictReader()")
    try:
        with Path.open(input_file_path, "r", newline="", encoding="utf-8") as f:
            dict_reader = csv.DictReader(f)
            dict_reader_fieldnames = dict_reader.fieldnames or []
            pprint("dict_reader.fieldnames:")
            pprint(dict_reader_fieldnames)
            dict_reader_section_counts = defaultdict(int)
            dict_reader_example_lines = defaultdict(list)
            for row in dict_reader:
                dict_reader_section_count = len(row)
                dict_reader_section_counts[dict_reader_section_count] += 1
                if len(dict_reader_example_lines[dict_reader_section_count]) < TWO:
                    dict_reader_example_lines[dict_reader_section_count].append(row)

            pprint("DictReader section counts:")
            for count, num_lines in dict_reader_section_counts.items():
                pprint(f"Lines with {count} sections: {num_lines}")

            pprint("Example lines for each DictReader section count:")
            for count, examples in dict_reader_example_lines.items():
                pprint(f"Rows with {count} sections:")
                for example in examples:
                    pprint(f"{example}")
    except OSError as e:
        pprint(f"An error occurred while opening the file with csv.DictReader(): {e}")

    pprint("============== ENDING CSV DICT-READER ASSESSMENT ==============")


if __name__ == "__main__":
    main()
