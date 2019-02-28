import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import csv


def mark_color(img):
    position = []
    mask = np.zeros([img.shape[0], img.shape[1], 3], np.uint8)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower_rec = {'blue': (90, 90, 70), 'pink': (150, 100, 120)}
    # upper_rec = {'blue': (115, 210, 175), 'pink': (190, 180, 240)}
    lower_rec = {'blue': (90, 90, 50), 'pink': (150, 100, 120)}
    upper_rec = {'blue': (115, 230, 210), 'pink': (190, 180, 240)}
    flag1 = False
    flag2 = False
    for key, value in lower_rec.items():
        kernel = np.ones((16, 16), np.uint8)
        mask = cv2.inRange(hsv_img, lower_rec[key], upper_rec[key])
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        for cnt in contours:
            epsilon = 0.1 * cv2.arcLength(cnt, True)
            if key == 'blue':
                cv2.drawContours(img, [cnt], 0, (0, 150, 000), 2)
                approx_rec_blue = cv2.approxPolyDP(cnt, epsilon, True)
                flag2 = True
                # plt.imshow(img)
                a, b, c, d = cv2.boundingRect(approx_rec_blue)
                cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 2)
                position.append([key,a,b,c,d])
                # print(key,a,b,c,d)
            if key == 'pink':
                cv2.drawContours(img, [cnt], 0, (0, 0, 150), 2)
                approx_rec_pink = cv2.approxPolyDP(cnt, epsilon, True)
                flag1 = True
                a, b, c, d = cv2.boundingRect(approx_rec_pink)
                cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 150), 2)
                # print(key,a,b,c,d)
                position.append([key, a, b, c, d])
            # cv2.imwrite("mask4.png", img)
            # cv2.imshow('hsv_img', hsv_img)
    if flag1 & flag2:
        print(position)
        if position[0][2] > position[1][2]:
            x = 4500*(position[0][2]-position[2][2])/(position[0][2]-position[1][2]-position[1][4])
            volume = x + 500
            print('volumn', volume)
            return volume


def read_all_images():
    root_dir1 = r'/Users/sixuanli/Desktop/swhw lab/smart_spirometor/calibration/test_new/test_new1'
    root_dir2 = r'/Users/sixuanli/Desktop/swhw lab/smart_spirometor/calibration/test_new/test_new2'
    root_dir3 = r'/Users/sixuanli/Desktop/swhw lab/smart_spirometor/calibration/test_new/test_new3'
    root_dir4 = r'/Users/sixuanli/Desktop/swhw lab/smart_spirometor/calibration/test_new/test_new4'
    root_dir5 = r'/Users/sixuanli/Desktop/swhw lab/smart_spirometor/calibration/test_new/test_new5'
    root_dir6 = r'/Users/sixuanli/Desktop/swhw lab/smart_spirometor/calibration/test_new/test_new6'
    volume_test1 = []
    for parent, dirnames, filenames in os.walk(root_dir1):  # 遍历每一张图片
        i = 0
        filenames.sort(key= lambda x:int(x[:-4]))
        for filename in filenames:
            i += 1
            print('parent is :' + parent)
            print('filename is :' + filename)
            current_path = os.path.join(parent, filename)
            print('the full name of the file is :' + current_path)
            if os.path.splitext(filename)[1] == '.jpg':
                img = cv2.imread(current_path)
                volume = mark_color(img)
                volume_test1.append(volume)
    print(volume_test1)
    volume_test2 = []
    for parent, dirnames, filenames in os.walk(root_dir2):  # 遍历每一张图片
        filenames.sort(key= lambda x:int(x[:-4]))
        for filename in filenames:
            i += 1
            print('parent is :' + parent)
            print('filename is :' + filename)
            current_path = os.path.join(parent, filename)
            print('the full name of the file is :' + current_path)
            if os.path.splitext(filename)[1] == '.jpg':
                img = cv2.imread(current_path)
                volume = mark_color(img)
                volume_test2.append(volume)
    volume_test3 = []
    for parent, dirnames, filenames in os.walk(root_dir3):  # 遍历每一张图片
        filenames.sort(key= lambda x:int(x[:-4]))
        for filename in filenames:
            i += 1
            print('parent is :' + parent)
            print('filename is :' + filename)
            current_path = os.path.join(parent, filename)
            print('the full name of the file is :' + current_path)
            if os.path.splitext(filename)[1] == '.jpg':
                img = cv2.imread(current_path)
                volume = mark_color(img)
                volume_test3.append(volume)
    volume_test4 = []
    for parent, dirnames, filenames in os.walk(root_dir4):  # 遍历每一张图片
        filenames.sort(key= lambda x:int(x[:-4]))
        for filename in filenames:
            i += 1
            print('parent is :' + parent)
            print('filename is :' + filename)
            current_path = os.path.join(parent, filename)
            print('the full name of the file is :' + current_path)
            if os.path.splitext(filename)[1] == '.jpg':
                img = cv2.imread(current_path)
                volume = mark_color(img)
                volume_test4.append(volume)
    volume_test5 = []
    for parent, dirnames, filenames in os.walk(root_dir5):  # 遍历每一张图片
        filenames.sort(key= lambda x:int(x[:-4]))
        for filename in filenames:
            i += 1
            print('parent is :' + parent)
            print('filename is :' + filename)
            current_path = os.path.join(parent, filename)
            print('the full name of the file is :' + current_path)
            if os.path.splitext(filename)[1] == '.jpg':
                img = cv2.imread(current_path)
                volume = mark_color(img)
                volume_test5.append(volume)
    volume_test6 = []
    for parent, dirnames, filenames in os.walk(root_dir6):  # 遍历每一张图片
        filenames.sort(key= lambda x:int(x[:-4]))
        for filename in filenames:
            i += 1
            print('parent is :' + parent)
            print('filename is :' + filename)
            current_path = os.path.join(parent, filename)
            print('the full name of the file is :' + current_path)
            if os.path.splitext(filename)[1] == '.jpg':
                img = cv2.imread(current_path)
                volume = mark_color(img)
                volume_test6.append(volume)
    volume_record = [volume_test1]+[volume_test2]+[volume_test3]+[volume_test4]+[volume_test5]+[volume_test6]
    print (volume_record)
    with open('volume.csv', 'a') as f:
        # df.to_csv(f, header=False)
        writer = csv.writer(f)
        writer.writerows(volume_record)


def record_all_volume(test_volume):
    pass


if __name__ == "__main__":
    # a = 650.91
    # b = -3222
    # img = mpimg.imread('10.jpg')
    read_all_images()
