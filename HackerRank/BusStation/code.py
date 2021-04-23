def helper(arr, k):
    A = 0
    for i, a in enumerate(arr):
        A += a
        if A == k:
            A = 0
        elif A > k:
            return False
    return A == 0

def solve(arr):
    M = sum(arr)
    prefix_sum = 0
    results = []
    for i, a in enumerate(arr):
        prefix_sum += a
        if M % prefix_sum != 0:
            continue
        if helper(arr[i + 1:], prefix_sum):
            results.append(prefix_sum)
    return results


if __name__ == '__main__':
    input_fname = 'data/input07.txt'
    with open(input_fname, 'r') as handle:
        n = int(handle.readline().strip())
        arr = list(map(int, handle.readline().strip().split()))
    result = solve(arr)
    print(result)