ex1, sum1 = [1, 2, 3, 9], 8

ex2, sum2 = [1, 2, 4, 4], 8

def sumIn(lst: list, sum: int) -> bool:
    """@pre: lst is a list where list[n] < list[n+1]
             sum is the sum we want to get from a pair of the list
        @post: True if there is a pair with a sum of 'sum', false if not
    """
    curSum = lst[0] + lst[1]
    for i in range(2, len(lst)): # [0, 1, 2 -> n]
        for j in range(i, len(lst)): # [0, 1, 2 -> n] [i, j] ?= sum
            curSum = lst[i] + lst[j]
            if curSum > sum:
                break
            if curSum == sum: return True
            else: continue
    return False

print(sumIn(ex2, sum2))
