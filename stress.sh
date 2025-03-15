#!/bin/bash

while true; do
        stress-ng --cpu 4 --timeout 30s
        stress-ng --io  2 --timeout 20s
        stress-ng --vm  2 --timeout 40s
        stress-ng --hdd 2 --timeout 50s
        stress-ng --net 2 --timeout 25s
done
