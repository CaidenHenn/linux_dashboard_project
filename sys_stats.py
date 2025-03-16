from flask import Flask, jsonify
import psutil
import subprocess
import json
app = Flask(__name__)


def get_max_cpu_usage():
    with open('/home/caidenhenn/top_process_pipe') as pipe:
        for line in pipe:
           parts=json.loads(line)
           pid=parts['pid']
           name=parts['name']
           cpu_usage=parts['cpu'] 
           print(parts)
    return [pid,cpu_usage,name]



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
