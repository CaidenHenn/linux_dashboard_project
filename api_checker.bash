#!/bin/bash
if ps aux | grep '[a]pi_script.py' >/dev/null; then
    exit
else
    set -e
    source "./venv/bin/activate"
    python3 sys_stats.py &
fi