from flask import Flask, jsonify
import psutil

app = Flask(__name__)


def get_max_cpu_usage():
    max_process_pid= None
    max_process_name=None
    max_usage=0

    for proc in psutil.process_iter():
        cpu_usage = proc.cpu_percent()
        if cpu_usage > max_usage:
            max_usage=cpu_usage
            max_process_pid=proc.pid
            max_process_name=proc.name()
    return [max_process_pid,max_usage,max_process_name]



def get_stats():
    max_cpu=get_max_cpu_usage()
    stats = {
            "CPU": psutil.cpu_percent(),
            "IO": psutil.disk_io_counters()._asdict(),
            "Memory": psutil.virtual_memory().percent,
            "HDD (Disk)": psutil.disk_usage('/').percent,
            "Network": psutil.net_io_counters()._asdict(),
            "Uptime(s)": psutil.boot_time(),
            "Max_Process_PID": max_cpu[0],
            "Max_Process_Name":max_cpu[2],
            "Max_Process_Usage":max_cpu[1]
            }
    return stats

@app.route('/stats', methods=['GET'])
def stats():
    return jsonify(get_stats())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
