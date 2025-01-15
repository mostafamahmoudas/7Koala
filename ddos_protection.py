import subprocess
import time
from scapy.all import sniff, IP
import psutil
import logging

# إعداد السجلات
logging.basicConfig(filename="ddos_logs.txt", level=logging.INFO)

# قائمة لحظر العناوين المهاجمة
attacked_ips = []

# دالة لتحليل الحزم
def packet_handler(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        if ip_src != ip_dst:
            print(f"حزمة واردة من {ip_src} إلى {ip_dst}")
            if ip_src not in attacked_ips:
                attacked_ips.append(ip_src)
                block_ip(ip_src)

# حظر الـ IP المهاجم
def block_ip(ip):
    print(f"حظر IP: {ip}")
    logging.info(f"تم حظر IP: {ip} في {time.strftime('%Y-%m-%d %H:%M:%S')}")
    subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])

# دالة لقياس استخدام CPU
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 80:
        print(f"استخدام CPU مرتفع: {cpu_usage}%")
        return True
    return False

# دالة لقياس استخدام الذاكرة
def check_memory_usage():
    memory = psutil.virtual_memory()
    if memory.percent > 80:
        print(f"استخدام الذاكرة مرتفع: {memory.percent}%")
        return True
    return False

# مراقبة النظام واكتشاف الهجمات
def monitor_system():
    while True:
        if check_cpu_usage() or check_memory_usage():
            print("كشف هجوم محتمل، تحليل الحزم...")
            # يمكن هنا استخدام تحليل Scapy لربط الـ IP المهاجم بالحمل الزائد
            # إذا كان هناك حمل زائد، يمكن فرض حظر مؤقت على الـ IPs المهاجمة
        time.sleep(5)

# بدء المراقبة
def start_sniffing():
    sniff(prn=packet_handler, store=0)

if __name__ == "__main__":
    start_sniffing()
    monitor_system()
