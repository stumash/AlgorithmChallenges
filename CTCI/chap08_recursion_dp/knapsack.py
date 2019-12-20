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
            all(count[i] < 1 for i in elements)
    """
    memo = [ [None]*len(values) for _ in range(capacity+1) ]
    memo[0] = [0]*len(values)

    def dp(item, cap):
        pass

    def backtrack():
        pass

    # maxVal = dp(len(values)-1, capacity)
    # itemCounts = backtrack()
    # return maxVal, itemCounts

def knapsack(values, weights, capacity):
    """
    knapsack problem:
    Given elements (i for i in range(N))
        maximize sum(value[i]*count[i] for i in elements)
        subject to constraints
            sum(weights[i]*count[i] for i in elements) < capacity
    """
    pass

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
