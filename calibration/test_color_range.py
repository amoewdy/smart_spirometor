import numpy as np
import cv2
import matplotlib.pyplot as plt
import os



def read_image(img):
    position = []
    mask = np.zeros([img.shape[0], img.shape[1], 3], np.uint8)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
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
                position.append([key, a, b, c, d])
                # print(key,a,b,c,d)
            if key == 'pink':
                cv2.drawContours(img, [cnt], 0, (0, 0, 150), 2)
                approx_rec_pink = cv2.approxPolyDP(cnt, epsilon, True)
                flag1 = True
                a, b, c, d = cv2.boundingRect(approx_rec_pink)
                cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 150), 2)
                # print(key,a,b,c,d)
                position.append([key, a, b, c, d])
            cv2.imwrite("test_color.png", img)
            # cv2.imshow('hsv_img', hsv_img)
    if flag1 & flag2:
        print(position)
        if position[0][2] > position[1][2]:
            x = 4500 * (position[0][2] - position[2][2]) / (position[0][2] - position[1][2] - position[1][4])
            volume = x + 500
            print('volumn', volume)


img = cv2.imread('/Users/sixuanli/Desktop/swhw lab/smart_spirometor/calibration/test_new/test_new1/50.jpg')
read_image(img)
