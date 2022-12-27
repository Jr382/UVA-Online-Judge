from sys import stdin as s


def main():
    lines = s.readlines()
    raw_input = "".join(lines)
    decoded = "".join([chr((ord(i) - 7) % 255) if i != "\n" else i for i in raw_input])
    print(decoded, end="")


main()
