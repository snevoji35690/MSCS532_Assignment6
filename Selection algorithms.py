# Deterministic algorithm
def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: Divide the list into sublists of 5 elements each
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    
    # Step 2: Find medians of all sublists
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]

    # Step 3: Find the pivot (median of medians)
    pivot = deterministic_select(medians, len(medians)//2)

    # Step 4: Partition the list
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    # Step 5: Recurse into the appropriate sublist
    if k < len(lows):
        return deterministic_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))

arr = [7, 10, 4, 3, 20, 15]
k = 2
print(deterministic_select(arr, k))

# Randomized Algorithm
import random

def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return randomized_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))
#  Test input
arr = [7, 10, 4, 3, 20, 15]
k = 2  # 3rd smallest element (0-based index)

#  Print output
print("Randomized Quickselect output:", randomized_select(arr, k))