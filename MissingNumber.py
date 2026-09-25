import sys


def main() -> None:
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    if not numbers:
        return

    count = numbers[0]
    missing = count
    for number in range(1, count):
        missing ^= number
        missing ^= numbers[number]

    print(missing)


if __name__ == "__main__":
    main()