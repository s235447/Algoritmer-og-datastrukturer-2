WAGES = (
    (5, 40),
    (10, 10),
    (10, 30),
    (10, 50),
)


def compute_memorized_opt(index: int, dp: list[int]) -> int:
    if dp[index] != -1:
        return dp[index]

    if index == 0:
        dp[index] = max(WAGES[index][0], WAGES[index][1])
    elif index == 1:
        dp[index] = max(
            WAGES[index][0] + compute_memorized_opt(index - 1, dp),
            WAGES[index][1],
        )
    else:
        dp[index] = max(
            WAGES[index][0] + compute_memorized_opt(index - 1, dp),
            WAGES[index][1] + compute_memorized_opt(index - 2, dp),
        )

    return dp[index]


def main() -> None:
    dp = [-1] * len(WAGES)
    total_wages = compute_memorized_opt(len(WAGES) - 1, dp)
    print(f"Total Wages: {total_wages}")


if __name__ == "__main__":
    main()