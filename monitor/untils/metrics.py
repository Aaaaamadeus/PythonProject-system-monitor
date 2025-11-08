import psutil
import requests,socket
import yaml

config = yaml.safe_load(
    open(
        'D:/PythonProject/monitor/config.yaml', 'r',encoding='utf-8'
    ))

def collect_system_metrics():
    return {
        "CPU使用率:": psutil.cpu_percent(interval=config["interval"]),
        "内存使用率:": psutil.virtual_memory().percent,
        "磁盘使用率": psutil.disk_usage("/").percent,
        }           #获取各项性能指标

def check_http(url):
    try:
        r = requests.get(url,timeout=5)
        return r.status_code
    except:
        return False   #测试网络连接

def check_port(host,port):
    s = socket.socket()
    s.settimeout(5)
    try:
        s.connect((host,port))
        return True
    except:
        return False
    finally:
        s.close()      #测试端口连接

