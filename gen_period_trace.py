import json
import random
import matplotlib.pyplot as plt

MTU_SIZE = 1500          # byte

MAX_RATE = 1500*1000    # bps
MIN_RATE = 800*1000     # bps

MIN_DURATION = 200       # ms
MAX_DURATION = 800       # ms

TOTAL_TIME = 60*1000     # ms

def random_num_with_fix_total(maxValue, num)->list:
    '''
    生成总和固定的整数序列
    maxvalue: 序列总和
    num: 要生成的整数个数
    '''
    a = random.sample(range(1,maxValue), k=num-1)
    a.append(0)
    a.append(maxValue)
    a = sorted(a)
    b = [ a[i]-a[i-1] for i in range(1, len(a)) ]
    return b

trace_json = {}
trace_json["type"] = "video"
trace_json["downlink"] = {}
trace_json["uplink"] = {}
trace_json_path = "traces/period_trace.json"

fp = open("traces/period_trace.log", "w")

with open("traces/period.trace", "w") as f:

    now_time = 0
    trace_pattern = []
    while(now_time < TOTAL_TIME):
        random_rate = random.randint(MIN_RATE, MAX_RATE)
        random_duration = random.randint(MIN_DURATION, MAX_DURATION)
        fp.write("rate: %d \t duration: %d \n" %(random_rate, random_duration))

        net_para = {}
        net_para["duration"] = random_duration
        net_para["capacity"] = int(random_rate/1000)
        trace_pattern.append(net_para)

        interval = MTU_SIZE*8*1000/random_rate

        if interval >= 1:
            interval_list = random_num_with_fix_total(random_duration, int(random_duration/interval))
            data = now_time
            for i in interval_list:
                if interval <= 10:
                    data += i
                else:
                    data += int(interval)
                f.write(str(data)+'\n')
        else:
            if now_time == 0:
                now_time = 1

            cnt_list = random_num_with_fix_total(int(random_duration/interval), random_duration)
            for i in range(now_time, now_time+random_duration):
                max_cnt = 1/interval
                if max_cnt % 1 != 0:
                    max_cnt = cnt_list.pop()
                for j in range(max_cnt):
                    f.write(str(i)+'\n')

        now_time = now_time+random_duration

    trace_json["uplink"]["trace_pattern"] = trace_pattern

with open(trace_json_path, "w") as fp:
    json.dump(trace_json, fp, indent=4)
