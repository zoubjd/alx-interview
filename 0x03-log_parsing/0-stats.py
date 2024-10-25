#!/usr/bin/python3
"""Log parsing script that reads from standard input and computes statistics."""
import sys


# Initialize the total file size and a dictionary to count occurrences of each status code
total_file_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

def print_stats():
    """
    Print the current statistics: total file size and count of each status code.

    Only non-zero status code counts are displayed.
    """
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_codes_count.items()):
        if count > 0:
            print(f"{code}: {count}")

# Initialize a counter for the number of lines processed
line_count = 0

try:
    # Read from standard input line by line
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Attempt to extract the file size (last part of the log line)
        try:
            file_size = int(parts[-1])
            total_file_size += file_size
        except (IndexError, ValueError):
            # In case of a malformed log line or invalid file size, skip the line
            continue

        # Attempt to extract the status code (second-to-last part of the log line)
        try:
            status_code = parts[-2]
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
        except IndexError:
            # Skip the line if the format is incorrect
            continue

        # Print statistics after every 10 lines processed
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # If the script is interrupted, print the final statistics before exiting "just configed git and needed to push" 
    print_stats()
    raise
