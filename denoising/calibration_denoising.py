import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy import signal
import seaborn as sns
import pandas as pd
import csv


def read_csv(path):
    tmp = np.loadtxt(path, dtype=np.str, delimiter=",")
    data = tmp[:, :].astype(np.float)
    # print(data)
    # print(len(data))
    return data


def noise_filter(data):
    # perform a median filter
    data_clean = []
    for i in range(len(data)):
        data_clean.append(signal.medfilt(data[i], 5))
    # print(len(data_clean))
    return data_clean


def write_csv(data):
    with open('sensor_read_cleaner.csv', 'a') as f:
        # df.to_csv(f, header=False)
        writer = csv.writer(f)
        writer.writerows(data_clean)


if __name__ == "__main__":

        # a = 650.91
        # b = -3222
        path = "sensor_read_raw.csv"
        data_raw = read_csv(path)
        data_clean = noise_filter(data_raw)
        # draw_plot(data_raw, data_clean)
        write_csv(data_clean)

# y1 = sp.signal.medfilt(x, 21)  # add noise to the signal
