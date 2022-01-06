from sys import stdin

def min_gondolas(num_children, max_weight, weights):
    weights.sort()
    i, j = 0, len(weights) - 1
    min_gondolas = 0
    while i < j:
        if weights[i] + weights[j] <= max_weight:
            i += 1
            j -= 1
        else:
            j -= 1
        min_gondolas += 1
    return min_gondolas if i != j else min_gondolas + 1

if __name__ == '__main__':
    num_children, max_weight = [int(num) for num in stdin.readline().split()]
    weights = [int(num) for num in stdin.readline().split()]
    print(
        min_gondolas(
            num_children,
            max_weight,
            weights
        )
    )