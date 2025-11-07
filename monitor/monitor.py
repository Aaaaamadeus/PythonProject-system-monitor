from untils.alert import *
from untils.metrics import *
import time

#定义变量
check_gap = 1
config = yaml.safe_load(open('D:/PythonProject/monitor/config.yaml', 'r',encoding='utf-8'))
cpu = config['cpu_threshold']
memory = config['mem_threshold']
targets = config['target']
for target in targets:
    if target["type"] == "http":
        url = target["url"]
        if check_http(url):
            print("HTTP 可访问")
        else:
            print("HTTP 不可访问")
    elif target["type"] == "port":
        port = target["port"]
        host = target["host"]
        if check_port(host,port):
            print(f"端口开放：{host}:{port}")
        else:
            print(f"端口不可用{host}:{port}")

def monitor():
    while True:
        collect_system_metrics()
        metrics = collect_system_metrics()
        print(metrics)
        if metrics['cpu'] > cpu:
            the_alert(f"cpu使用率超过警告阈值{cpu}%")
        if metrics['memory'] > memory:
            the_alert(f"内存使用率超过警告阈值{memory}%")

    time.sleep(check_gap)

if __name__ == '__main__':
    monitor()



