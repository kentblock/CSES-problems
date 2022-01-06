from sys import stdin

# good one to review, clever solution but fairly simple implementation

# O(nlog(n)) algorithm

# 1 pass over arr
# aux array contains each end candidate, index is length of subseq - 1
# at each element arr[i] 3 cases
# a) arr[i] smaller than all end candidates start new list
# b) arr[i] larger than all end candidates clone longest and append arr[i]
# c) arr[i] in between smallest and largest end candidates then clone and extend list with largest end that is less than arr[i], discard all other lists of same length

def lis(arr):
    aux = []
    for a in arr:
        if not aux or aux[-1] < a: # case c
            aux.append(a)
        elif a <= aux[0]:
            aux[0] = a
        elif a > aux[0] and a < aux[-1]:
            aux[find(aux, a)] = a
    return len(aux)

def find(arr, a):
    s, e = 0, len(arr) - 1
    while s < e:
        mid = -(-(s + e) // 2)
        if arr[mid] >= a:
            e = mid - 1
        else:
            s = mid
    return s + 1

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _ = read_num()
    print(lis(read_nums()))