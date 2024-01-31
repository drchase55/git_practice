#!/usr/bin/python
# turns 80character lines to a single string from a FASTA file[O
from collections import defaultdict

d = defaultdict(str)

with open('dna.example.fasta') as file1:
    for line in file1:
        if line[0] == '>': 
            key = line.strip('\n')
        else:
            d[key] += line.strip('\n')

print(d)
