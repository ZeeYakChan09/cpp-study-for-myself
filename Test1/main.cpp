#include <iostream>
#include<opencv2/opencv.hpp>

using namespace std;
using namespace cv;//命名空间

//opencv机器视觉库，c/c++语言编写出来的

int main(int argc, char *argv[])
{
    //This is a way to 换证件照背景图
    //1.显示图片
    Mat image=imread("C:/Users/ZeeYak Chan/Desktop/13422552447084349.png");
    imshow("1",image);

    //2.转换成hsv格式
    Mat hsv;
    cvtColor(image,hsv,COLOR_BGR2HSV);
    imshow("hsv",hsv);

    //3.截取颜色区域的范围 inRange 在蓝色的hsv取值范围内呈现白色的抠图模板，不在范围内呈黑色的抠图模板
    Mat mask;
    inRange(hsv,Scalar(100,43,46),Scalar(124,255,255),mask);
    imshow("3",mask);

    //4.现在可以蓝色背景表示出来了，但是实际上想抠人物
    //取反操作
    bitwise_not(mask,mask);
    imshow("4",mask);

    //5.生成一张红色背景图 (参照原始图片)
    //::是cpp作用域分解运算符 调用Mat对象里面的xxx函数
    //zeros创建一个指定行数列数类型的矩阵，像素都为0
    Mat redBack = Mat::zeros(image.size(),image.type());
    redBack = Scalar(40,40,240);//括号填红绿蓝
    imshow("5",redBack);

    //6.实现图片的拷贝操作
    image.copyTo(redBack,mask);
    imshow("6",redBack);

    waitKey(0);

    return 0;
}
/*This is a way to make a picture to Binary.
//1.显示一张图片，先找后显示
Mat img=imread("C:/Users/ZeeYak Chan/Desktop/13422552433942526.jpeg");
//Mat类型--图片（容器）对象类型
imshow("title",img);//显示图片

//2.图片转模糊图片 车牌识别 人脸识别
Mat blurImg;//模糊照片
blur(img,blurImg,Size(50,50));//模糊处理方法，左数字为横向模糊尺寸，右为纵向模糊尺寸
imshow("blur",blurImg);

//3.图片灰度处理-数据量减少三倍（业务开发跟颜色无关先灰度处理）
Mat grayImg;
cvtColor(img,grayImg,COLOR_BGR2GRAY);//颜色处理函数
imshow("gray",grayImg);

//4.图片二值化处理
Mat threImg;//二值化图片
threshold(grayImg,threImg,150,255,THRESH_BINARY);
imshow("thre",threImg);


waitKey(0);//等待用户按下任意键
return 0;
*/
