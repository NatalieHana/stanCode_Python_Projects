"""
File: similarity.py (extension)
Name: Jane
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    find most similar DNA pattern
    """
    search = input("Please give me a DNA sequence to search: ").upper()
    match = input("What DNA sequence would you like to match? ").upper()
    count = 0
    count_max = count
    mapping_max = ""

    for i in range(len(search)-(len(match)-1)):
        ans = ""
        count = 0
        mapping = search[i:i + len(match)]
        for j in range(len(match)):
            if mapping[j] == match[j]:
                ans += mapping[j]
                count += 1
            else:
                ans += mapping[j]
        if count > count_max:
            count_max = count
            mapping_max = ans

    print("The best match is " + str(mapping_max))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
