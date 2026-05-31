import cv2
import time

def camera():
    """
    采集摄像头图像，并实时显示
    :return:
    """
    #加载人脸识别级联分类器
    face_detect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #1.打开摄像头
    # videoPath='video/10-1.mp4'
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('打开失败')
        return

    #2.循环读取画面
    while True:

        #读一帧图像
        ret, frame = cap.read()
        if ret==False:
            print('读取失败')
            break

        # 增加人脸检测
        # 1. 重新指定并加载模型路径（加在这里）
        face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        face_detect = cv2.CascadeClassifier(face_cascade_path)

        # 2. 转换为灰度图像（你原本的代码）
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detect.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=3, minSize=(200, 200),maxSize=(300, 300))

        #把人脸框出来
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        #增加时间显示
        time_str=time.strftime('%Y%m%d%H%M%S', time.localtime())
        cv2.putText(frame, time_str, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        #3.显示画面
        cv2.imshow('camera', frame)
        key = cv2.waitKey(30)
        if key==ord('q'):
            break
        elif key==ord('s'):
            #保存一帧画面
            filename=time.strftime('%Y%m%d%H%M%S', time.localtime())
            cv2.imwrite(f'phone/{filename}.jpg', frame)

    #释放资源
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera()
