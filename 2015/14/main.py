import sys
import re




def main():
    """
    Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
    """
    regex_pattern = re.compile(r"([A-Za-z]*) (can fly) ([0-9]*) (km/s for) ([0-9]*) (seconds, but then must rest for) ([0-9]*) (seconds).")
    lines = sys.stdin.readlines()
    for l in lines:
        result = regex_pattern.search(l.strip())
        print(result.group(1), result.group(3), result.group(5), result.group(7))



if __name__ == '__main__':
    main()