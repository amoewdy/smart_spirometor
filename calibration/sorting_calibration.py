import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import csv
from scipy import signal


def read_sensor():
    with open('/Users/sixuanli/Desktop/swhw lab/smart_spirometor/denoising/sensor_read_cleaner.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    # print(rows)
    data_sensor = np.array(rows)
    # print(data_sensor)
    data_sensor_float = data_sensor.astype(np.float)
    # print(data_sensor_float)
    data_flat = []
    for i in range(len(data_sensor_float)):
        for j in range(len(data_sensor_float[i])):
            data_flat.append(data_sensor_float[i][j])
    data_flat.sort()
    print(data_flat)
    return data_flat

def read_img():
    with open('/Users/sixuanli/Desktop/swhw lab/smart_spirometor/calibration/volume.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    # print(rows)
    data_img = np.array(rows)
    # print(data_sensor)
    data_img_float = data_img.astype(np.float)
    data_flat = []
    for i in range(len(data_sensor_float)):
        for j in range(len(data_sensor_float[i])):
            data_flat.append(data_sensor_float[i][j])
    data_flat.sort()
    print(data_flat)
    # print(data_img_float)
    # data_img_all = []
    # for i in range(len(data_img_float)):
    #     data_img_clean = []
    #     for j in range(len(data_img_float[i])):
    #         data_img_clean.append(signal.medfilt(data_img_float[i][j], 15))
    #     data_img_all.append(data_img_clean)
    return data_flat


def sorting():
    sensor_data = read_sensor()
    # print(sensor_data)
    img_data = read_img()
    # print(img_data)
    # all_data = []
    # for i in range(len(sensor_data)):
    #     for j in range(len(sensor_data[i])):
    #         all_data.append([sensor_data[i][j], img_data[i][j]])
    # print(all_data)
    # data_sorted = sorted(all_data, key=lambda x: x[0])
    # print(data_sorted)
    data_csv = []
    data_csv.append(sensor_data)
    data_csv.append(img_data)
    # data_csv1 = []
    # data_csv2 = []
    # # for i in range(len(data_sorted)):
    # #     data_csv1.append(data_sorted[i][0])
    # #     data_csv2.append(data_sorted[i][1])
    # for i in range(len(all_data)):
    #     data_csv1.append(all_data[i][0])
    #     data_csv2.append(all_data[i][1])
    # data_csv.append(data_csv1)
    # data_csv.append(data_csv2)
    # print(data_csv)

    with open('sorted_both_clean.csv', 'a') as f:
        # df.to_csv(f, header=False)
        writer = csv.writer(f)
        writer.writerows(data_csv)


sorting()
