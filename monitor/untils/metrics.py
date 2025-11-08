import psutil
import requests,socket
import yaml
import time

config = yaml.safe_load(
    open(
        'D:/PythonProject/monitor/config.yaml', 'r',encoding='utf-8'
    ))
interval=config["interval"]
net1 = psutil.net_io_counters()

def collect_system_metrics():
    return {
        "CPU使用率:": psutil.cpu_percent(interval),
        "内存使用率:": psutil.virtual_memory().percent,
        "磁盘使用率:": psutil.disk_usage("/").percent,
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

def check_net_speed(interval):
    time.sleep(interval)
    net2 = psutil.net_io_counters()

    sent_speed = (net2.bytes_sent - net1.bytes_sent) / 1024 / 1024  # KB/S
    recv_speed = (net2.bytes_recv - net1.bytes_recv) / 1024 / 1024 # KB/S

    return {
        "上传速率": str(round(sent_speed/interval, 2))+"Mb/s",
        "下载速率": str(round(recv_speed/interval, 2))+"Mb/s",
    }