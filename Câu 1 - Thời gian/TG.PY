# Expected result (TG.OUT): "08:05 \n 08:10 \n 09:05"

def end_times(n, Times):
    max = 100       # max time
    start = 8 * 60  # 8AM => minutes
    end = []
    for time in Times:
        end_time = min(start+time, start+max)
        end.append(f"{end_time//60:02d}:{end_time%60:02d}") # Format time
        start_time = max(start_time + 10, end_time)         # Update start time
    return end

with open("TG.INP", "r") as f:
    n = int(f.readline().strip())
    Times = [int(f.readline().strip()) for _ in range(n)]

result = end_times(n, Times)
with open("TG.OUT", "w") as f:
    for time in result:
        f.write(time + "\n")
