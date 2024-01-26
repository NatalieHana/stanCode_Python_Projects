"""
File: final test problem 4
Name: Jane
"""
import random
NUM_ROLLS = 15


def main():
    # OBOB
    count = 0
    run_1 = random.randrange(1, 7)
    is_in_row = False  # 機械開關(boolean), 決定是否計算次數
    for i in range(NUM_ROLLS-1):
        run_2 = random.randrange(1, 7)
        if run_1 == run_2:
            if not is_in_row:
                count += 1
                is_in_row = True
        else:
            is_in_row = False
        run_1 = run_2

    print("Number of runs: " + str(count))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()