# TODO:
# solve the 0-1 knapsack problem
# solve the non-(0-1) knapsack problem

def knapsack01(values, weights, capacity):
    """
    0-1 knapsack problem:
    Given elements (i for i in range(N))
        maximize sum(value[i]*count[i] for i in elements)
        subject to constraints
            sum(weights[i]*count[i] for i in elements) < capacity
            AND
            all(count[i] in [0,1] for i in elements)
    """
    memo = [ [None]*(len(values)+1) for _ in range(capacity+1) ]
    memo[0] = [0]*(len(values)+1)

    def dp(item, cap):
        if item < 0 or cap < 0:
            return None
        if memo[item][cap] is None:
            memo[item][cap] = max(filter(lambda x: x is not None, [
            ]))
        return memo[item][cap]

    def backtrack():
        return [] # TODO FIXME

    maxVal = dp(len(values), capacity)
    itemCounts = backtrack()
    return maxVal, itemCounts

def knapsack(values, weights, capacity):
    """
    knapsack problem:
    Given elements (i for i in range(N))
        maximize sum(value[i]*count[i] for i in elements)
        subject to constraints
            sum(weights[i]*count[i] for i in elements) < capacity
    """
    pass # TODO FIXME

def test():
    items = [
        (1, 2),
        (2, 3),
        (5, 4),
        (6, 5),
    ]
    (values, weights) = zip(*items)
    capacity = 4

    print(f"values:   {values}")
    print(f"weights:  {weights}")
    print(f"capacity: {capacity}")

    # assert(knapsack01(values, weights, capacity) == 8)
