# Expected result (TPS.OUT): "498"

def min_range(n, locations, k):
    locations.sort()
    def can_place(range):
        count = 1
        last = locations[0]
        for i in range(1, n):
            if locations[i] - last > range * 2:
                count += 1
                last = locations[i]
        return count <= k

    low, high = 0, 10**6
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if can_place(mid):
            result, high = mid, mid-1
        else:
            low = mid + 1
    return result

with open("TPS.INP", "r") as f:
    n = int(f.readline().strip())
    locations = [int(f.readline().strip()) for _ in range(n)]
    k = int(f.readline().strip())

with open("TPS.OUT", "w") as f:
    f.write(str(min_range(n, locations, k)))
