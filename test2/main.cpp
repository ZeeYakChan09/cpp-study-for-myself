#include <iostream>
#include<opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main(int argc, char *argv[])
{
    //这是一个“隐身术”的红布抠图方法

    //1.显示两张图片
    Mat hideImg = imread("C:/Users/ZeeYak Chan/Desktop/hide.jpeg");
    Mat backImg = imread("C:/Users/ZeeYak Chan/Desktop/background.jpeg");
    imshow("back",backImg);
    imshow("hide",hideImg);

    //2.图片转换hsv
    Mat hsv;
    cvtColor(hideImg,hsv,COLOR_BGR2HSV);
    imshow("hsv",hsv);

    //3.识别出红色区域
    Mat mask,mask1;
    inRange(hsv,Scalar(0,120,100),Scalar(10,255,255),mask);
    inRange(hsv,Scalar(170,120,100),Scalar(180,255,255),mask1);
    //imshow("mask",mask);
    //imshow("mask1",mask1);
    mask = mask + mask1;
    imshow("mask",mask);

    //4.取反操作
    Mat uMask;//红布区域意外的抠图模板
    bitwise_not(mask,uMask);
    imshow("uMask",uMask);

    //5.开始进行抠图 背景图片用
    Mat bkMask;
    bitwise_and(backImg,backImg,bkMask,mask);
    imshow("bkMask",bkMask);

    Mat bkUmask;
    bitwise_and(hideImg,hideImg,bkUmask,uMask);
    //imshow("bkUmask",bkUmask);

    bkUmask = bkUmask + bkMask;
    imshow("bkUmask",bkUmask);


    waitKey(0);

    return 0;
}
