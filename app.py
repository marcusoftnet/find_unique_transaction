import json
from collections import defaultdict
import argparse
import csv


def find_related_transactions(transactions, min_length, min_matches):
    substring_matches = defaultdict(int)

    for transaction1 in transactions:
        substrings = get_substrings(transaction1, min_length)
        for substring in substrings:
            matching_transactions_count = sum(1 for t in transactions if substring in t)
            if matching_transactions_count >= min_matches:
                substring_matches[substring] += 1

    return substring_matches


def get_substrings(text, min_length):
    substrings = set()
    n = len(text)
    for j in range(
        min_length, n + 1
    ):  # Minimum length of substring is specified by min_length
        substrings.add(text[:j])
    return substrings


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find related substrings in transaction texts"
    )
    parser.add_argument(
        "file_path", type=str, help="Path to the JSON file containing transaction texts"
    )
    parser.add_argument(
        "--min_length",
        type=int,
        default=3,
        help="Minimum length of substring to consider (default: 3)",
    )
    parser.add_argument(
        "--min_matches",
        type=int,
        default=3,
        help="Minimum number of matches for a substring (default: 3)",
    )
    args = parser.parse_args()

    # Load transactions from JSON file
    with open(args.file_path, "r") as file:
        transactions = [line.strip() for line in file]

    substring_matches = find_related_transactions(
        transactions, args.min_length, args.min_matches
    )

    # Print results in CSV format
    with open("substring_matches.csv", "w", newline="") as csvfile:
        fieldnames = ["Substring", "Number of matches"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for substring, matches in substring_matches.items():
            writer.writerow({"Substring": substring, "Number of matches": matches})

    print("CSV file 'substring_matches.csv' has been created with the results.")
