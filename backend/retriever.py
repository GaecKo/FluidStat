import psutil
import time
from math import *

from colorama import Fore, Style, init
init(autoreset=True)




# python script showing battery details
import psutil

# function returning time in hh:mm:ss
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

class Monitor:
    def get_cpu_usage():
        
        return psutil.cpu_percent()
    



while True:

    print("==========================")
    cores_percent = psutil.cpu_percent(percpu=True)
    general_percent = psutil.cpu_percent(percpu=False)

    charged = ceil(general_percent // 2)
    free = 50 - charged
    charged_vis = '-' * charged
    free_vis = '-' * free

    per = f"{Fore.RED + charged_vis + Style.RESET_ALL}{Fore.GREEN + free_vis + Style.RESET_ALL}"
    cp_percents = f"General percent: {general_percent} {per}\n\n"

    for i in range(len(cores_percent)):
        charged = ceil(cores_percent[i] // 2)
        free = 50 - charged
        charged_vis = '-' * charged
        free_vis = '-' * free

        per = f"{Fore.RED + charged_vis + Style.RESET_ALL}{Fore.GREEN + free_vis + Style.RESET_ALL}"

        cp_percents += f"CPU{i+1}: {cores_percent[i]}% {per}\n"

    print(cp_percents)

    print("The ram usage is: %", psutil.virtual_memory()[2])

    # returns a tuple
    battery = psutil.sensors_battery()

    print("Battery percentage : ", battery.percent)
    print("Power plugged in : ", battery.power_plugged)

    # converting seconds to hh:mm:ss
    print("Battery left : ", convertTime(battery.secsleft))
    print("==========================\n\n")
    time.sleep(5)
