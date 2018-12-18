# #-*- coding:utf8 -*-
# from flask import Blueprint, request, render_template
# from app_frontend import app
# from matplotlib import pyplot as plt
# import cv2
# import numpy as np
#
#
# bp_auth = Blueprint('login', __name__, url_prefix='/login')
#
# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     print(1233456789)
#     return render_template('index.html')
#
# @app.route('/test/', methods=['GET', 'POST'])
# def test():
#     print('testtttttttttttttttttttt')
#     return render_template('test.html')
#
# #pc端
# @app.route('/takepic/', methods=['GET', 'POST'])
# def take_pic():
#
#     cv2.namedWindow("test")
#     cap = cv2.VideoCapture(0)
#     # cap = cv2.VideoCapture("output.avi")
#     success, frame = cap.read()
#     classifier = cv2.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
#
#     while success:
#         success, frame = cap.read()
#         size = frame.shape[:2]
#         image = np.zeros(size, dtype=np.float16)
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         plt.imshow(image)
#         plt.show()
#         cv2.equalizeHist(image, image)
#         divisor = 8
#         h, w = size
#         minSize = (w // divisor, h // divisor)
#         faceRects = classifier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)
#         if len(faceRects) > 0:
#             for faceRect in faceRects:
#                 x, y, w, h = faceRect
#                 cv2.rectangle(frame, (x, y), (x + h, y + w), (0, 255, 0), 2)
#                 # 锁定 眼和嘴巴
#                 # cv2.circle(frame, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8), (255, 0, 0))   # 左眼
#                 # cv2.circle(frame, (x + 3 * w //4, y + h // 4 + 30), min(w // 8, h // 8), (255, 0, 0))   #右眼
#                 # cv2.rectangle(frame, (x + 3 * w // 8, y + 3 * h // 4), (x + 5 * w // 8, y + 7 * h // 8), (255, 0, 0))   #嘴巴
#         cv2.imshow("test", frame)
#         key = cv2.waitKey(10)
#         c = chr(key & 255)
#         if c in ['q', 'Q', chr(27)]:
#             break
#         if c in ['t']:
#             cv2.imwrite('C:/Users/28674/Desktop/jj.jpg', frame)
#
#     cv2.destroyWindow("test")
#
#     return render_template('phone.html')
#
#
#
# #phone端
# @app.route('/phone/', methods=['GET', 'POST'])
# def take_pic_phone():
#
#     cv2.namedWindow("camera", 1)
#     video = "http://admin:admin@172.18.15.209:8081/" #安装ip摄像头
#     capture = cv2.VideoCapture(video)
#     num = 0
#     while True:
#         success, img = capture.read()
#         cv2.imshow("camera", img)
#         key = cv2.waitKey(10)
#         if key == 27:
#             print("esc break...")
#             break
#         if key == ord(' '):
#             # 保存一张图像
#             num = num + 1
#             filename = "frames_%s.jpg" % num
#             cv2.imwrite(filename, img)
#     capture.release()
#     cv2.destroyWindow("camera")
#-*- coding:utf8 -*-
from flask import Blueprint, request, render_template
from app_frontend import app
# from matplotlib import pyplot as plt
import cv2
import numpy as np


bp_auth = Blueprint('login', __name__, url_prefix='/login')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    print(1233456789)
    return render_template('index.html')

@app.route('/test/', methods=['GET', 'POST'])
def test():
    print('testtttttttttttttttttttt')
    return render_template('test.html')

#pc端
@app.route('/takepic/', methods=['GET', 'POST'])
def take_pic():

    cv2.namedWindow("test")
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture("output.avi")
    success, frame = cap.read()
    classifier = cv2.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

    while success:
        success, frame = cap.read()
        size = frame.shape[:2]
        image = np.zeros(size, dtype=np.float16)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        plt.imshow(image)
        plt.show()
        cv2.equalizeHist(image, image)
        divisor = 8
        h, w = size
        minSize = (w // divisor, h // divisor)
        faceRects = classifier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x, y), (x + h, y + w), (0, 255, 0), 2)
                # 锁定 眼和嘴巴
                # cv2.circle(frame, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8), (255, 0, 0))   # 左眼
                # cv2.circle(frame, (x + 3 * w //4, y + h // 4 + 30), min(w // 8, h // 8), (255, 0, 0))   #右眼
                # cv2.rectangle(frame, (x + 3 * w // 8, y + 3 * h // 4), (x + 5 * w // 8, y + 7 * h // 8), (255, 0, 0))   #嘴巴
        cv2.imshow("test", frame)
        key = cv2.waitKey(10)
        c = chr(key & 255)
        if c in ['q', 'Q', chr(27)]:
            break
        if c in ['t']:
            cv2.imwrite('C:/Users/28674/Desktop/jj.jpg', frame)

    cv2.destroyWindow("test")

    return render_template('phone.html')

def get_rot(input_shape):

    (w, h) = input_shape
    pad_x = 200
    pad_y = 100

    center_x = int(w/2)
    center_y = int(h/2)
    left_x = center_x - pad_x
    left_y = center_y - pad_y
    right_x = center_x + pad_x
    right_y = center_y + pad_y

    return [left_x, left_y, right_x, right_y]

def draw_rect(image, box):
    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)

@app.route('/phone/', methods=['GET', 'POST'])
def take_pic_phone():

    cv2.namedWindow("camera", 1)
    video = "http://admin:admin@172.18.15.29:8081/"

    capture = cv2.VideoCapture(video)
    ret, image = capture.read()
    roi = get_rot(image.shape)
    while ret:

        ret, image = capture.read()
        image = draw_rect(image, roi)
        cv2.imshow("camera", image)

        key = cv2.waitKey(10)
        if key == 27:
            print("esc break...")
            break
    capture.release()
    cv2.destroyWindow("camera")
