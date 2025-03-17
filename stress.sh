#!/bin/bash

while true; do
        stress-ng --cpu 4 --timeout 30s        # stress the CPU every 30 seconds
        stress-ng --io  2 --timeout 20s        # stress the IO every 20 seconds
        stress-ng --vm  2 --timeout 40s        # stress the memory every 40 seconds
        stress-ng --hdd 2 --timeout 50s        # stress the disk every 50 seconds
        stress-ng --net 2 --timeout 25s        # stress the network every 25 seconds
done
