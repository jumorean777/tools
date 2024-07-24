#!/usr/bin/env python3

import pandas
import argparse
import re
import matplotlib.pyplot as plt

def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-d', '--duration')
    parser.add_argument('--csv')
    parser.add_argument('-t', '--title')
    parser.add_argument('-x')
    parser.add_argument('-y')
    return parser.parse_args()


ms_per_second = 1000


def main():
    args = getArguments()
    data = pandas.read_csv(args.csv)
    x = args.x
    y = args.y
    duration = args.duration.split(',')
    start = int(duration[0])
    end = int(duration[1])
    fig, ax = plt.subplots()
    ax.stem((data[x] - start)/ms_per_second, data[y])
    fig.set_size_inches(16, 9)
    plt.xlim(0, (end-start)/ms_per_second)
    plt.title(args.title)
    plt.xlabel('Time[ms]')
    plt.grid(True)
    plt.ticklabel_format(style='plain', axis='both', useLocale=False)
    plt.savefig(args.output)

if __name__ == '__main__':
    main()

