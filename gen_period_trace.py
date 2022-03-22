import random
import matplotlib.pyplot as plt

MTU_SIZE = 1500         # byte

MAX_RATE = 1500*1000    # bps, should below 12mbps
MIN_RATE = 800*1000     # bps

MIN_DURATION = 200      # ms
MAX_DURATION = 800      # ms

TOTAL_TIME = 60*1000   # ms

fp = open("traces/period_trace.log", "w")

now_time = 0
rate_t = []
time_t = []
with open("traces/period.trace", "w") as f:
    while(now_time < TOTAL_TIME):
        random_rate = random.randint(MIN_RATE, MAX_RATE)
        interval = int(MTU_SIZE*8*1000/random_rate)
        random_duration = random.randint(MIN_DURATION, MAX_DURATION)
        fp.write("rate: %d \t duration: %d \n" %(random_rate, random_duration))

        for i in range(now_time+interval, now_time+random_duration+interval, interval):
            f.write(str(i)+'\n')

        now_time = now_time+random_duration+interval
        rate_t.append(random_rate/1000)
        time_t.append(now_time/1000)

fp.close()

plt.figure(figsize=(12,5))
plt.step(time_t, rate_t)
plt.grid()
plt.ylim(0, MAX_RATE/1000)
plt.ylabel("rate/kbps", fontsize=16)
plt.xlabel("time/s", fontsize=16)
plt.tick_params(labelsize=15)
plt.savefig("traces/period_trace.png",dpi=300)
