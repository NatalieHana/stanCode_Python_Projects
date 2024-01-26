"""
File: name_sq.py (extension)
Name: Jane
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main() :
    """
    print a name in a square pattern
    """
    print("This program prints a name in a square pattern!")
    name = input("Name: ")
    length = len(name)

    # 第一行
    print(name)

    # 中間行
    for i in range(1, length-1):
        ans = ""
        for j in range(length):
            if j == 0:
                ans += name[i]
            elif j == length-1:
                ans += name[length-1-i]
            else:
                ans += " "
        print(ans)

    # 最後一行
    for i in range(length-1, length):
        ans = ""
        for j in range(length):
            ans = name[j]+ans
        print(ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
