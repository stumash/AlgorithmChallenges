from heapq import heapify, heappop, heappush

def main():
    n, m, calls, intervals, operators = None, None, None, None, None

    def readInput():
        nonlocal n, m, calls, intervals

        tokens = (int(token) for token in input().split(' '))
        n = next(tokens)
        m = next(tokens)

        if (n == 0 and m == 0):
            return False

        calls = []
        for i in range(n):
            tokens = list(map(lambda token: int(token), input().split(' ')))
            calls.append((tokens[2],tokens[2] + tokens[3]))

        intervals = []
        for i in range(m):
            tokens = [int(token) for token in input().split(' ')]
            intervals.append((tokens[0], tokens[1]))

        return True

    while (readInput()):
        operators = []
        pass

















if __name__ == "__main__":
    main()
