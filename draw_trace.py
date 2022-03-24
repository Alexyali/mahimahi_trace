#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

MTU_SIZE = 1500 * 8 # bit

def get_data(trace_path, time, interval):

    data = []
    total_time = time*1000
    sample_interval = interval
    trace_name = os.path.basename(trace_path)
    with open(trace_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            data.append(int(line))

    rate_list = []
    timestamp_list = []
    last_time = 0
    last_index = -1

    for i, element in enumerate(data):
        if element > total_time:
            break
        if element-last_time >= sample_interval:
            rate_t = (i-last_index)*MTU_SIZE/(element-last_time) # kbps
            rate_list.append(rate_t/1000) # mbps
            timestamp_list.append(element/1000) # sec
            last_time = element
            last_index = i

    max_rate = max(rate_list)
    min_rate = min(rate_list)
    average_rate = np.mean(rate_list)
    std_rate = np.std(rate_list)
    print("trace: %s Max rate: %.3f Mbps, Min rate: %.3f Mbps, Average rate: %.3f Mbps, Std rate: %.3f Mbps"
            %(trace_name, max_rate, min_rate ,average_rate, std_rate))

    return timestamp_list, rate_list, trace_name

def draw_rate(time_list, rate_list, trace_name, output_folder):
    plt.figure(figsize=(12,5))
    plt.step(time_list, rate_list)
    plt.grid()
    plt.ylim(bottom=0)
    plt.ylabel("rate/Mbps", fontsize=16)
    plt.xlabel("time/s", fontsize=16)
    plt.tick_params(labelsize=15)
    plt.savefig(output_folder+trace_name+".png",dpi=300)

def init_args():
    parser = argparse.ArgumentParser()
    drive_trace = "/usr/share/mahimahi/traces/ATT-LTE-driving-2016.down"
    walk_trace = "/home/alex/DeepCC.v1.0/deepcc.v1.0/traces/trace-1553189663-ts-walking"
    parser.add_argument("--trace", type=str, default=drive_trace, help="the network trace path")
    parser.add_argument("--time", type=int, default=60, help="total time(s)")
    parser.add_argument("--interval", type=int, default=400, help="bandwidth sample interval(ms)")
    parser.add_argument("--output", type=str, default=None, help="output folder")

    return parser

if __name__ == "__main__":
    parser = init_args()
    args = parser.parse_args()
    time_t, rate_t, trace_n = get_data(args.trace, args.time, args.interval)
    if args.output:
        draw_rate(time_t, rate_t, trace_n, args.output)