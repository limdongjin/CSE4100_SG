#!/usr/bin/env python

# import modules
from itertools import groupby
from operator import itemgetter
import sys
# 'file' in this case is STDIN
def read_mapper_output(file, separator=','):
# Go through each line
    for line in file:
        # Strip out the separator character
        yield line.rstrip().split(separator)
def main(separator=','):
    # Read the data using read_mapper_output
    data = read_mapper_output(sys.stdin, separator=separator)
    # Group words and counts into 'group'
    # Since MapReduce is a distributed process, each word
    # may have multiple counts. 'group' will have all counts
    # which can be retrieved using the word as the key.
    for current_group, group in groupby(data, itemgetter(0)):
        try:
            max_value = max(float(value1) for current_group, value1 in group)

            print("%s\t%f" % (current_group, max_value))
        except ValueError:
            # Count was not a number, so do nothing
            pass
if __name__ == "__main__":
    main()
