import subprocess
import shlex
import time
import matplotlib.pyplot as plt
import numpy as np
from multiprocessing.sharedctypes import RawArray
from functools import wraps

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


def test_lambda(a):
    x = np.arange(0, 10, 0.01)
    y = 1 + x ** 2
    plt.plot(x, y)
    plt.show()


class A:
    def __init__(self):
        self.dict = dict()

    def __getitem__(self, item):
        return self.dict[item]

    def __call__(self, param):
        print("a.call")
        register_name = param.__name__
        print(register_name)
        self.dict[register_name] = param
        return param


a = A()


@a
class B:
    def print_b(self):
        print("b")


if __name__ == "__main__":
    b = B()
    b.print_b()
    c = a["B"]()
    c.print_b()

