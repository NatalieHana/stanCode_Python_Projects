"""
File: complement.py
Name: Jane
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    DNA Reverse Complement by ATGC
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna: str
    :return: str, Reverse Complement by ATGC
    """
    ans = ""
    if dna == "":
        return "DNA strand is missing"
    else:
        for ch in dna:
            if ch == "A":
                ans += "T"
            elif ch == "T":
                ans += "A"
            elif ch == "G":
                ans += "C"
            elif ch == "C":
                ans += "G"
        return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
