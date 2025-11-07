#导入模块
import psutil
import time
import smtplib
import email.mime.multipart

#配置区域
CPU_use_percent = 80 #CPU使用率
MEM_use_percent = 80 #内存使用率
check_gap = 5 #检查时间间隔

#建立数据获取函数
def get_metrics():
    return{
        "CPU":psutil.cpu_percent(interval=1), #统计一秒内CPU占用率
        "memory":psutil.virtual_memory().percent, #统计一秒内内存使用率
        "disk":psutil.disk_usage("/").percent, #统计一秒内磁盘使用率
    }
#建立告警函数
def send_alert(message):
    print("[ALERT]",message)


#建立监控函数
def monitor():
    while True:
        metrics = get_metrics()
        print(metrics)

        if metrics["CPU"] > CPU_use_percent:
            send_alert(f"CPU占用率超出警告阈值{metrics['CPU']}%")
        if metrics["memory"] > MEM_use_percent:
            send_alert(f"内存使用率超出警告阈值{metrics['memory']}%")

        time.sleep(check_gap)


#自动执行
if __name__ == '__main__':
    monitor()



