import psutil
import platform
import GPUtil
from PySide6.QtCore import QObject, Signal, Qt, QThread

class SystemInfo(QObject):
    cpu_usage_signal = Signal(float)
    memory_usage_signal = Signal(float)
    gpu_usage_signal = Signal(float)
    battery_info_signal = Signal(float)

    def __init__(self):
        super().__init__()
        self.cpu_usage_signal.connect(self.on_cpu_usage)
        self.memory_usage_signal.connect(self.on_memory_usage)
        self.gpu_usage_signal.connect(self.on_gpu_usage)
        self.battery_info_signal.connect(self.on_battery_info)

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        return psutil.virtual_memory().percent

    def get_gpu_usage(self):
        gpu_usage = 0.0
        for gpu in GPUtil.getGPUs():
            gpu_usage += gpu.load
        return gpu_usage / len(GPUtil.getGPUs())

    def get_battery_info(self):
        battery = psutil.sensors_battery()
        if battery:
            return battery.percent
        return None

    def on_cpu_usage(self, value):
        print(f"CPU usage: {value}%")

    def on_memory_usage(self, value):
        print(f"Memory usage: {value}%")

    def on_gpu_usage(self, value):
        print(f"GPU usage: {value}%")

    def on_battery_info(self, value):
        print(f"Battery info: {value}%")

    def run(self):
        while True:
            cpu_usage = self.get_cpu_usage()
            memory_usage = self.get_memory_usage()
            gpu_usage = self.get_gpu_usage()
            battery_info = self.get_battery_info()

            self.cpu_usage_signal.emit(cpu_usage)
            self.memory_usage_signal.emit(memory_usage)
            self.gpu_usage_signal.emit(gpu_usage)
            if battery_info is not None:
                self.battery_info_signal.emit(battery_info)

            QThread.msleep(1000) # Sleep for 1 second
