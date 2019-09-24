import cv2
import opencvjietu
import opencv_compare
import mousedianji
a=1
jiacheng_pic = cv2.imread('pic/jiacheng.png',0)
def yuhunjiacheng():
    if a == 1:
        yuhunjiacheng_pic = cv2.imread('pic/yuhunjiacheng.png', 0)
        yysclient = opencvjietu.yys_client()
        #yysclient.show()
        yysclient = opencv_compare.PIL_opencv(yysclient)
        jiacheng_xy = opencv_compare.template_matching(yysclient,jiacheng_pic)
        mousedianji.mouse_click(jiacheng_xy[0], jiacheng_xy[1],3)
        yysclient = opencvjietu.yys_client()
        #yysclient.show()
        yysclient = opencv_compare.PIL_opencv(yysclient)
        jiacheng_xy = opencv_compare.template_matching(yysclient,yuhunjiacheng_pic)
        mousedianji.mouse_click(jiacheng_xy[0] + 250, jiacheng_xy[1],3)
        mousedianji.mouse_click(jiacheng_xy[0] + 400, jiacheng_xy[1], 3)
    else:
        print('没有选择开启加成')


def juexingjiacheng():
    print("还没写")

#yuhunjiacheng()