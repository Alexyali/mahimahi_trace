# mahimahi路径生成和可视化

## 路径生成

### 生成周期性波动的网络路径

`gen_period_trace.py`用于生成一段周期性波动的网络路径，其网络带宽在(MIN_RATE, MAX_RATE)之间波动，每次随机选择的带宽值的持续时长为(MIN_DURATION, MAX_DURATION)区间的随机数。该路径持续时间为TOTAL_TIME。

运行方法：

```shell
$ mkdir traces
$ python3 gen_period_trace.py
```

运行后生成2个文件：

- `period.trace`：适用于mm-link的网络路径
- `period_trace.log`：该路径对应的速率和持续时间的序列

### 生成突然中断的网络路径

`gen_break_trace.py`用于生成带宽突然下降的网络路径，其配置参数在`gen_period_trace.py`的基础上添加了：

- `BREAK_TIME`：带宽下降的时刻
- `BREAK_DURATION`：带宽下降持续的时间
- `DECR_STEP`：带宽下降的归一化步长，取值为(0, 1)
- `INCR_STEP`：带宽上升的归一化步长，取值为(0, 1)

运行方法：

```shell
$ python3 gen_break_trace.py
```

运行后生成2个文件：

- `break.trace`：适用于mm-link的网络路径
- `break_trace.log`：该路径对应的速率和持续时间的序列

## 网络路径可视化

`draw_trace.py`通过分析trace来提取带宽信息，并绘制真实的带宽变化图，运行方法：

```shell
$ python3 draw_trace.py --trace [trace path]  --time [total_time] --interval [sample interval] --output [output folder]
```