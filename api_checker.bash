#!/bin/bash

#check if pi_script.py is running
if ps aux | grep '[a]pi_script.py' >/dev/null; then
    exit #exit if running
else
    set -e
    source "./venv/bin/activate" #enter the vitural environment
    python3 sys_stats.py &  #run the API script in the background
fi