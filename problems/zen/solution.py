import this
import codecs
import re
from collections import defaultdict

def main():
    zen = codecs.decode(this.s, "rot13")
    positions = defaultdict(list)
    
    regex = re.compile(r"[a-zA-Z]+(?:'[a-zA-z]+)?")

    for row, line in enumerate(zen.splitlines(), start=1):
        for col, match in enumerate(regex.finditer(line), start=1):
            word = match.group(0)
            positions[word].append((row, col))
    
    print(dict(positions))

if __name__ == "__main__":
    main()