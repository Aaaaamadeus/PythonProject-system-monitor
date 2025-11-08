
from untils.alert import *
from untils.metrics import *
from untils.logger import logger
import yaml,time

#定义变量
check_gap = 1
config = yaml.safe_load(open('D:/PythonProject/monitor/config.yaml', 'r',encoding='utf-8'))
cpu = config['cpu_threshold']
memory = config['mem_threshold']
disk = config['disk_threshold']
targets = config['target']

RED = "\033[91m"      # 错误
GREEN = "\033[92m"    # 成功
YELLOW = "\033[93m"   # 警告
BLUE = "\033[94m"     # 信息
RESET = "\033[0m"     # 还原颜色

for target in targets:
    global url, port, host
    if target["type"] == "http":
        url = target["url"]
        if check_http(url):
            print(f"{BLUE}[INFO]{BLUE}HTTP 可访问,网络服务正常")
        else:
            print(f"{RED}[ERROR]{RED}HTTP 不可访问")
    elif target["type"] == "port":
        port = target["port"]
        host = target["host"]
        if check_port(host,port):
            print(f"{BLUE}[INFO]{BLUE}端口开放：{host}:{port}")
        else:
            print(f"{BLUE}[INFO]{BLUE}端口不可用{host}:{port}")


def monitor():
    while True:
        collect_system_metrics()
        metrics = collect_system_metrics()
        net_check = check_net_speed(interval)

        logger.info(metrics)
        logger.info(net_check)


        time.sleep(check_gap)
def alert_monitor():
    while True:
        metrics = collect_system_metrics()
        if check_http(url):
            pass
        else:
            the_alert(f"{RED}[ERROR]{RED}网络连接出现问题")
            return False
        if metrics["CPU使用率:"] > cpu:
            the_alert(f"{YELLOW}[WARN]{YELLOW}cpu使用率超过警告阈值{cpu}%")
        if metrics["内存使用率:"] > memory:
            the_alert(f"{YELLOW}[WARN]{YELLOW}内存使用率超过警告阈值{memory}%")
        if metrics["磁盘使用率:"] > disk:
            the_alert(f"{YELLOW}[WARN]{YELLOW}磁盘使用率超过警告阈值{disk}%")


if __name__ == '__main__':
    logger.info("监控脚本启动")
    monitor()



