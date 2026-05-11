import shutil       # for file management / disk usage
import psutil       # for cpu usage
      
du = shutil.disk_usage("/")
print(du)
print((du.free/du.total) * 100)

for _ in range(5):
    print(psutil.cpu_percent(interval=0.5, percpu=True))