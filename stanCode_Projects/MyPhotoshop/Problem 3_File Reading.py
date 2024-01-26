"""
File: final test problem 3
Name: Jane
"""
FILEPATH = "images/FN_Problem3.txt"  # filepath


def main():
    count = 0
    with open(FILEPATH, "r") as f:
        for line in f:  # file裡面讀出來都是string
            if line != "Nan\n":
                score = float(line)
                count += 1
                if count == 1:  # 第一筆資料 OBOB
                    max_score = score
                    min_score = score
                    total = score
                else:
                    if score > max_score:
                        max_score = score
                    if score < min_score:
                        min_score = score
                    total += score
        if count == 0:
            print("No data in this file")
        else:
            print("Max: " + str(max_score))
            print("Min: " + str(min_score))
            print("Avg: " + str(total/count))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
