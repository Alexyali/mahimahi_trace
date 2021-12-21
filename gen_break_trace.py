import random
import matplotlib.pyplot as plt

MTU_SIZE = 1500         # byte

MAX_RATE = 1100*1000    # bps
MIN_RATE = 900*1000     # bps

MIN_DURATION = 200      # ms
MAX_DURATION = 400      # ms

BREAK_TIME = 28*1000  # ms
BREAK_DURATION = 1*1000 # ms

TOTAL_TIME = 60*1000   # ms


with open("traces/break.trace", "w") as f:
    f.close()

fp = open("traces/break_trace.log", "w")

now_time = 0
drop_c = 1
rate_t = []
time_t = []
with open("traces/break.trace", "a") as f:
    while(now_time < TOTAL_TIME):

        if now_time < BREAK_TIME:
            random_rate = random.randint(MIN_RATE, MAX_RATE)
        elif now_time < BREAK_TIME+BREAK_DURATION:
            drop_c -= 0.2
            if drop_c < 0.1:
                drop_c = 0.1
            random_rate = random.randint(int(MIN_RATE*drop_c), int(MAX_RATE*drop_c))
            assert random_rate>0
        else:
            if drop_c < 1:
                drop_c += 0.1
                random_rate = random.randint(int(MIN_RATE*drop_c), int(MAX_RATE*drop_c))
            else:
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
plt.savefig("traces/break_trace.png",dpi=300)