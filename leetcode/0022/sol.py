from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Examples:
        n = 1
        ["()"]

        n = 2
        ["()()", "(())"]

        n = 3
        ["()()()", "(()())", "()(())", "(())()", "((()))"]
        """
        res = []
        if n >= 1:
            self.sol(opens=n-1, closes=n, path='(', result=res)
        return res


    def sol(self, opens, closes, path, result):
        if closes == 0: # if no closes left, result can be added
            result.append(path)
        if closes > opens: # if you can close, try it
            self.sol(opens, closes-1, path + ')', result)
        if opens > 0: # if you can open, try it
            self.sol(opens-1, closes, path + '(', result)


if __name__ == "__main__":
    for i in range(1,9):
        print(len(Solution().generateParenthesis(i)))
