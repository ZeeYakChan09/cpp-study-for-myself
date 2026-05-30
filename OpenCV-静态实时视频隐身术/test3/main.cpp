#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;

using namespace std;

int main(int argc, char *argv[])
{
   Mat frame;                              //实时图片
   Mat Background; //背景图片、

   VideoCapture capture(0); //调用摄像头

   if (!capture.isOpened()) {
           cout << "无法打开摄像头！" << endl;
           return -1;
       }

       for (int i = 0; i < 30; i++) {
           capture.read(frame);
           if (i == 29) {
               // 取第30帧作为最终背景
               frame.copyTo(Background);
           }
           waitKey(10);
       }
       cout << "背景捕捉完成！" << endl;



   while (capture.read(frame)) {
       imshow("Video",frame);
       //转换hsv图片格式
       Mat hsv;
      cvtColor(frame,hsv,COLOR_BGR2HSV);
      //imshow("HSV",hsv);
       //识别蓝色区域
      Mat mask;
      inRange(hsv,Scalar(100,31,46),Scalar(138,255,255),mask);
      //imshow("mask",mask);
       //取反操作
      Mat umask;
      bitwise_not(mask,umask);
      //imshow("umask",umask);

       //背景+模板
       Mat bkmask;
       bitwise_and(Background,Background,bkmask,mask);
       //imshow("bk",bkmask);

       Mat bumask;
       bitwise_and(frame,frame,bumask,umask);
       //imshow("bu",bumask);

       //像素融合
       Mat final;
       add(bkmask,bumask,frame);

       imshow("final",frame);
       waitKey(30);
   }

   waitKey(0);
   return 0;
}
