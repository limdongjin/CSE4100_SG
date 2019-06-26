#!/usr/bin/env python

# Use the sys module
import sys
# 'file' in this case is STDIN

def read_input(file):
    # Split each line into words
    for line in file:
        yield line.split()

def main(separator=','):
    # Read the data using read_input
    data = read_input(sys.stdin)
    # Process each word returned from read_input

    for words in data:
        # Process each word
        for word in words:
            # Write to STDOUT
            print('%s' % (word))

if __name__ == "__main__":
    main()
