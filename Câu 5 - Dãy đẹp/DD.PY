# Expected result (DD.OUT): "4"

def beautisub_count(n, A):
    result = 0
    count = 1
    for i in range(1, n):
        if A[i] > A[i - 1]:
            count += 1
        else:
            result += count * (count+1) // 2
            count = 1
    result += count * (count+1) // 2
    return result

with open('DD.INP', 'r') as f:
    n = int(f.readline().strip())
    A = list(map(int, f.readline().split()))

with open('DD.OUT', 'w') as f:
    f.write(str(beautisub_count(n, A)))