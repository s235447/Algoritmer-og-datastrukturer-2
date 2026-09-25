import sys


MOD = 1_000_000_007


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    size = int(tokens[0])
    grid = [token.decode() for token in tokens[1:size + 1]]
    paths = [[0] * size for _ in range(size)]

    for row in range(size):
        for column in range(size):
            if grid[row][column] == "*":
                continue
            if row == 0 and column == 0:
                paths[row][column] = 1
            else:
                from_above = paths[row - 1][column] if row > 0 else 0
                from_left = paths[row][column - 1] if column > 0 else 0
                paths[row][column] = (from_above + from_left) % MOD

    print(paths[size - 1][size - 1])


if __name__ == "__main__":
    main()