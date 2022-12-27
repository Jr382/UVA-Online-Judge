from sys import stdin as s


def main():
    strings = s.readline().split()
    while strings:
        print(subsequence(strings[0], strings[1]))
        strings = s.readline().split()


def subsequence(substring, string):
    i, j = 0, 0
    substring_size, string_size = len(substring), len(string)
    while i < substring_size and j < string_size:
        if substring[i] == string[j]:
            i += 1
        j += 1
    return "Yes" if i == len(substring) else "No"


main()
