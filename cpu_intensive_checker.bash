if ps aux | grep '[c]pu_intensive.bash' >/dev/null; then
    exit
else
    ./cpu_intensive.bash &
fi