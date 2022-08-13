def numWaysToMakeChange(coinset, amount):
    memo = [None]*(amount+1)
    memo[0] = 1

    def dp(amount):
        if amount < 0:
            return 0
        if memo[amount] is None:
            memo[amount] = sum(dp(amount-coin) for coin in coinset)
        return memo[amount]

    result = dp(amount)
    return result

def smallestNumberOfCoins(coinset, amount):

    memo = [None]*(amount+1)
    memo[0] = 0

    def dp(amount):
        if memo[amount] is None:
            memo[amount] = 1 + min(dp(amount-coin) for coin in coinset if amount-coin >= 0)
        return memo[amount]

    return dp(amount)

if __name__ == "__main__":
    coinset = [1, 5, 10, 25]
    amount = 26

    print(numWaysToMakeChange(coinset, amount))
    print(smallestNumberOfCoins(coinset, amount))
