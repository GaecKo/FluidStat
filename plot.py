import plotext as plt
import os, psutil, time
from math import *
import argparse 


def cpu():
    while True:
        list_cores = psutil.cpu_percent(interval=1, percpu=True)
        cpu_usage = [ceil(sum(list_cores) / len(list_cores))] + [ceil(i) for i in list_cores]

        cpu_name = ["General:"] + [f"CPU{i+1}:" for i in range(len(cpu_usage))]

        rest = [100 - cpu_usage[i] for i in range(len(cpu_usage))]

        
        plt.cld()

        plt.simple_stacked_bar(cpu_name, [cpu_usage, rest], width=100, labels=["used", "free"], title="CPU Cores' usage", colors=["red", "white"])

        plt.sleep(0.01)
        os.system('cls' if os.name == 'nt' else 'clear')
        plt.show()

def ram():
    while True:
        ram = ceil(psutil.virtual_memory()[2])
        free = 100 - ram

        plt.cld()
        plt.simple_stacked_bar(["RAM:"], [[ram], [free]], title="RAM usage", labels=["used", "free"], colors=["red", "white"])
        plt.sleep(0.01)
        os.system('cls' if os.name == 'nt' else 'clear')
        plt.show()
        time.sleep(1)

def battery():
    def convertTime(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)
    while True:
        try:
            btry = psutil.sensors_battery()
            btry_percent = ceil(btry.percent)
            free = 100 - btry_percent
            plugged = btry.power_plugged
            time_left = convertTime(btry.secsleft)
            plt.cld()
            plt.simple_stacked_bar(["Battery:"], [[btry_percent], [free]], title="Battery Percentage", labels=["available", "used"], colors=["green", "white"])
            plt.sleep(0.01)
            os.system('cls' if os.name == 'nt' else 'clear')
            plt.show()
            print(f"Battery Plugged: {plugged}")
            print(f"Time left: {time_left if not plugged else 'N/A'}")
            time.sleep(1)
        except:
            print("We can´t access your battery sensors. Does your device have a battery?")

# def help():
#     print("List of usabla arguments:\n")
#     print("--help: get help")
#     print("-cpu: shows CPU cores' usage")
#     print("-ram: shows ram usage")
#     print("-battery (or -btry): shows battery informations")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple System Monitor')
    parser.add_argument('-cpu', action='store_true', help="Shows CPU cores' usage")
    parser.add_argument('-ram', action='store_true', help='Shows the RAM usage')
    parser.add_argument('-btry', action='store_true', help='Shows the battery usage')

    args = parser.parse_args()
    if args.cpu:
        cpu()
    if args.ram:
        ram()
    if args.btry:
        battery()