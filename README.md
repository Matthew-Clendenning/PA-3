# Pantheon of Congestion Control Assignment

## Requirements
- Ubuntu 18.04
- Python 2.7
- Pantheon setup (see [Pantheon GitHub](https://github.com/StanfordSNR/pantheon/))

## How to Reproduce My Experiments

1. Clone this repo
2. Install dependencies `tools/install_deps.sh

## Enter Pantheon directory
```bash
cd pantheon/
```

## How to run low latency experiments
```bash
src/experiments/test.py local --schemes "cubic bbr vivace" -t 60 --run-time 5 --data-dir results/low_latency --prepend-mm-cmds "mm-delay 5" --uplink-trace src/experiments/50mbps_10ms.trace --downlink-trace src/experiments 50mbps_10ms.trace --extra-mm-link-args "--uplink-queue=droptail --uplink-queue-args=bytes=6250000"
```

## How to run high latency experiments
```bash
src/experiments/test.py local --schemes "cubic bbr vivace" -t 60 --run-times 5 --data-dir results/high_latency --prepend-mm-cmds "mm-delay 100" --uplink-trace src/experiments/1mbps_200ms.trace --downlink-trace src/experiments/1mbps_200ms.trace --extra-mm-link-args "--uplink-queue=droptail --uplink-queue-args=bytes=625000"
```

## After running experiments, enter
```bash
src/analysis/analyze.py --data-dir results/low_latency
src/analysis/analyze.py --data-dir results/high_latency
```