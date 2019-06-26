#!/usr/bin/env python

import sys
import random

_, total_size, number_of_groups = sys.argv

total_size = int(total_size)
number_of_groups = int(number_of_groups)

with open("input.data", "w") as f:
    for i in range(total_size):
        group = random.randint(0, number_of_groups -1)
        number = random.random() * 10000 * random.random()
        f.write("{},{}\n".format(group, number))

        if i % 10000 == 0:
            print(i)
print("Done!")
