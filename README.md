# mahimahi路径生成和可视化

## 路径生成

### 生成周期性波动的网络路径

`gen_period_trace.py`用于生成一段周期性波动的网络路径，其网络带宽在(MIN_RATE, MAX_RATE)之间波动，每次随机选择的带宽值的持续时长为(MIN_DURATION, MAX_DURATION)区间的随机数。该路径持续时间为TOTAL_TIME。

注意：MAX_RATE需要小于12mbps，目前程序无法生成大于12mbps的路径

运行方法：

```shell
$ mkdir traces
$ python3 gen_period_trace.py
```

运行后生成3个文件：

- `period.trace`：用于mm-link使用的路径文件
- `period_trace.log`：该路径对应的速率和持续时间的序列
- `period_trace.png`：该网络路径带宽随时间变化的曲线

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

运行后生成的文件同`gen_break_trace.py`

## 网络路径可视化

虽然调用`gen_period_trace.py`和`gen_break_trace.py`会自动生成网络带宽变化图，但是这并不准确，因为在生成路径的过程中涉及取整等计算。

`draw_trace.py`直接通过分析trace文件来提取带宽信息，并绘制真实的带宽变化图，运行方法：

```shell
$ python3 draw_trace.py --trace [trace path]  --time [total_time] --interval [sample interval] --output [output folder]
```