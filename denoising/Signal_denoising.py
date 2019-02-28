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
        data_clean.append(signal.medfilt(data[i], 3))
    # print(len(data_clean))
    return data_clean


def draw_plot(data_raw,data_clean):
    # sns.set(style="whitegrid")
    # sns.pointplot(data=data_raw)
    # plt.show()
    # df = pd.DataFrame(data_raw)
    # sns.pointplot(data=df)
    # t = np.linspace(0, 3, 51)
    # plt.subplot(2, 1, 1)
    # test1 = data_raw[0]
    # test2 = data_raw[1]
    # test3 = data_raw[2]
    # fig, ax = plt.subplots()
    #
    # plt.xlabel('migration speed (MB/s)')
    # plt.ylabel('migration time (s); request delay (ms)')


    # plt.plot(t, test1)
    # plt.title('original_reading')
    # plt.xlabel('time')
    # plt.subplot(2, 1, 2)
    # plt.plot(t, data_clean[0], 'clean')
    # plt.title('filtered_reading')
    # plt.xlabel('time')
    # plt.show()
    pass


def write_csv(path,data):
    with open(path, 'a') as f:
        # df.to_csv(f, header=False)
        writer = csv.writer(f)
        writer.writerows(data_clean)


if __name__ == "__main__":

        # a = 650.91
        # b = -3222
        path = "sensor_read_scale2.csv"
        data_raw = read_csv(path)
        data_clean = noise_filter(data_raw)
        # draw_plot(data_raw, data_clean)
        write_csv(path, data_clean)

# y1 = sp.signal.medfilt(x, 21)  # add noise to the signal
