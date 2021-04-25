# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/16.
"""
import socket
import psutil
import platform
import uuid

__author__ = 'Allen7D'


class Server(object):
    def __init__(self):
        pass

    @property
    def system(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
        mac = ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
        os = platform.system()
        return {
            'hostname': hostname, # 主机名称
            'ip': ip, # IP地址
            'mac': mac, # MAC地址
            'os': os, # 操作系统
         }

    @property
    def cpu(self):
        return {
            'count': psutil.cpu_count(logical=False),  # 查看cpu物理个数
            'percent': str(psutil.cpu_percent(interval=2, percpu=False)) + '%'  # CPU的使用率(interval是获取2s内的cpu使用率波动)
        }

    # 内存
    @property
    def memory(self):
        total = round(psutil.virtual_memory().total / (1024.0 * 1024.0 * 1024.0), 2)  # 总物理内存(DDR)
        free = round(psutil.virtual_memory().free / (1024.0 * 1024.0 * 1024.0), 2)  # 剩余物理内存(DDR)
        percent = round((total - free) / total, 2)  # 物理内存使用率(DDR)
        return {
            'free': str(free) + 'G',
            'total': str(total) + 'G',
            'percent': str(percent * 100) + '%'
        }

    # 硬盘
    @property
    def disk(self):
        disk_usage = psutil.disk_usage('/')
        free = round(disk_usage.free / (1024.0 * 1024.0 * 1024.0), 2)
        total = round(disk_usage.total / (1024.0 * 1024.0 * 1024.0), 2)
        percent = round((total - free) / total, 2)
        return {
            'free': str(free) + 'G',
            'total': str(total) + 'G',
            'percent': str(percent * 100) + '%'
        }
