import this
import codecs
import re
from collections import defaultdict

def parse_zen():
    zen = codecs.decode(this.s, "rot13")
    positions = defaultdict(list)
    
    regex = re.compile(r"[a-zA-Z]+(?:'[a-zA-Z]+)?")

    for row, line in enumerate(zen.splitlines(), start=1):
        for col, match in enumerate(regex.finditer(line), start=1):
            word = match.group(0)
            positions[word].append((row, col))
    
    return dict(positions)

def main():
    print(parse_zen())

if __name__ == "__main__":
    main()