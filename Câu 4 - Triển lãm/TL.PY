# Expected result (TL.OUT): "6"

def max_profit(n, p):
    p.sort(key=lambda x: x[0])  # Sắp xếp theo kích thước tăng dần
    min, max = p[0][0], p[0][0]
    S = p[0][1]
    H = 0
    for i in range(1, n):
        min = min(min, p[i][0])
        max = max(max, p[i][0])
        S += p[i][1]
        H = max(H, S-(max-min))
    return H
 
with open("TL.INP", "r") as f:
    n = int(f.readline().strip())
    paintings = [list(map(int, f.readline().split())) for _ in range(n)]

with open("TL.OUT", "w") as f:
    f.write(str(max_profit(n, paintings)))
