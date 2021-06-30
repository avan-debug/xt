import subprocess
import shlex
import time
import matplotlib.pyplot as plt
import numpy as np

cpu_utl = []


def top():
    command = "top -b -n 1"
    args = shlex.split(command)
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    i = 0
    sum = 0
    while p.poll() is None:
        line = p.stdout.readline().decode("utf-8")
        line = line.strip()
        if line:
            if i > 5:
                str = line.split()
                # print(str[8])
                sum += float(str[8])
            i += 1
            # if i != 0 and  i % 2 == 0:
            #         str = line.split()
            #         cpu_uti.append(str[2])
            # i += 1
            # if i >= 200:
            #         break
    # print(cpu_uti)
    # print(len(cpu_uti))
    cpu_utl.append(sum)


def command(times):
    for i in range(times):
        top()
        time.sleep(0.01)
    print(cpu_utl)
    print(len(cpu_utl))
    x = np.linspace(0, times, times)
    plt.xlabel("timestamp")
    plt.ylabel("utilization of cpu%")
    plt.plot(x, cpu_utl)
    plt.show()


if __name__ == "__main__":
    command(100)
