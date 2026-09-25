import sys

def OPT(n, budget, prices, pages):
    dp = [0] * (budget + 1)

    for price, page in zip(prices, pages):
       for current_budget in range (budget, price -1, -1):
        dp[current_budget] = max(
            dp[current_budget],
            dp[current_budget - price] + page
        )
    return dp[budget]
    



def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))

    n, budget = data[0], data[1]

    prices = data[2:2 + n]
    pages = data[2 + n:2 + 2*n]

    print(OPT(n,budget,prices,pages))

if __name__ == "__main__":
    main()