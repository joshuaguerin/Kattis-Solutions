(n, t) = list(map(int, input().split()))

times = list(map(int, input().split()))
time = 0
jobs = 0

for i in range(len(times)):
    if times[i]+time <= t:
        time += times[i]
        jobs += 1
    else:
        break;

print(jobs)
