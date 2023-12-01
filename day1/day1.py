'''
Day 1 - Trebuchet?!
'''
from string import ascii_letters

# SAMPLE_INPUT = ["1abc2",
#                 "pqr3stu8vwx",
#                 "a1b2c3d4e5f",
#                 "treb7uchet"]


def calibrator(text):
    x = text.strip(ascii_letters)
    return int(x[0] + x[-1])


def main():
    with open('data.txt', 'r') as file:
        lines = [line.strip() for line in file]
        values = [calibrator(line) for line in lines]
        print(sum(values))


if __name__ == "__main__":
    main()
