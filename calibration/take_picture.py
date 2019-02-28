import time
import serial
import csv
from picamera import PiCamera
camera = PiCamera()


ser = serial.Serial(
    port='/dev/cu.usbmodem14401',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)


def calculate_distance(num):
    a = 1
    b = 0
    return num * a + b


def take_picture(num):
    camera.capture("/home/pi/Desktop/test1/" + num + ".jpg")


def recording():
    camera.start_preview(alpha=230)
    received = []
    flag = True
    max_time = 20
    while flag:
        data = ''
        while ser.inWaiting() > 0 and max_time <= 10:
            data = ser.readline()
            if data != '' and data != "\r\n":
                data_new = data.decode('utf-8')
                data_number = float(data_new[0:(len(data_new) - 2)])
                volume = calculate_distance(data_number)
                take_picture(max_time)
                received.append(volume)
                max_time += 1
        flag = False
    camera.stop_preview()
    print(received)


if __name__ == "__main__":

        # a = 650.91
        # b = -3222
        recording()





