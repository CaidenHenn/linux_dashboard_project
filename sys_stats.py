from flask import Flask, jsonify
import psutil

app = Flask(__name__)

def get_stats():
    stats = {
            "CPU": psutil.cpu_percent(),
            "IO": psutil.disk_io_counters()._asdict(),
            "Memory": psutil.virtual_memory().percent,
            "HDD (Disk)": psutil.disk_usage('/').percent,
            "Network": psutil.net_io_counters()._asdict()
            }
    return stats

@app.route('/stats', methods=['GET'])
def stats():
    return jsonify(get_stats())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
