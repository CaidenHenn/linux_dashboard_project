#!/bin/bash


while true; do
    top_process=$(ps -eo pid,cmd,%cpu --sort=-%mem | head -n 2 | tail -n 1)
    PID=$(echo "$top_process" | awk '{print $1}')
    NAME=$(echo "$top_process" | awk '{print $2}')
    CPU=$(echo "$top_process" | awk '{print $NF}')

    echo "{\"pid\": \"$PID\", \"name\": \"$NAME\", \"cpu\": \"$CPU\"}" > "top_process_pipe"
    sleep 1
done