import sys


def main() -> None:
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    if not numbers:
        return

    count = numbers[0]
    distinct_numbers = set(numbers[1:count + 1])
    print(len(distinct_numbers))


if __name__ == "__main__":
    main()