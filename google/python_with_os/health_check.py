#!/usr/bin/env python

import shutil, psutil

free = None
usage = None

def disk_check(disk):
    global free
    du = shutil.disk_usage(disk)
    free = (du.free/du.total) * 100
    return free > 20

def cpu_check():
    global usage
    usage = psutil.cpu_percent(1)
    return usage < 75

if  not disk_check("/") or not cpu_check():
    print("ERROR!", "Everything is not OK", sep="\n")
else:
    print(f"Everything is OK! disk: {free:.2f}, cpu: {usage}") 