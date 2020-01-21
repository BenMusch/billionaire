import re

DATA_FILE = "data/quotes.txt"

def clean_line(line):
    first_line = line.split("\n")[0]
    stripped = first_line.strip().strip('"')
    return stripped

with open(DATA_FILE, "r") as f:
    data = f.read().split("\n")

data = list(set(map(clean_line, data)))

with open(DATA_FILE, "w") as f:
    f.write("\n".join(data))