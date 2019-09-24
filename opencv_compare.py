#实时截图进行对比
import cv2
import numpy as py


# 图像的放大或者缩小
def resize(yysclien, image):
    #读入模板
    a_img = image
    #yys客户端当前的尺寸
    h = yysclien.shape[0]
    w = yysclien.shape[1]
    print('当前客户端的高和宽：',h,w)
    print('模板的大小',a_img.shape[0],a_img.shape[1])
    #判断是放大还是缩小
    if h <= 514:#如果高度小于514，则表示当前客户端大小小于截图客户端的大小，则模板图片应该缩小
        size = (int(a_img.shape[0]*(h/514)), int(a_img.shape[1] * (w/859)))
        print('缩放的倍数：', size[0], size[1])
        shrink = cv2.resize(a_img, size, interpolation=cv2.INTER_AREA)
        return shrink
    else:#放大
        size = (int(a_img.shape[0]*(h/514)), int(a_img.shape[1]*(w/859)))
        print('放大的倍数：',size[0],size[1],'比例分别是',h/514, w/859)
        enlarge = cv2.resize(a_img, (0, 0), fx=h/514, fy=w/859, interpolation=cv2.cv2.INTER_CUBIC)
        return enlarge






    #使用cv2.matchTemplate()实现模板匹配
def template_matching(imga, imgb):
    img_gray = cv2.cvtColor(imga, cv2.COLOR_BGR2GRAY)
    # print(img_gray.shape[0], img_gray.shape[1])
    #由于每次客户端的大小不一样所以为了提高模板匹配的准确率我们将模板的大小随客户端等比放大或者缩小
    template = resize(imga, imgb)
    h, w = template.shape[0], template.shape[1]  # rows->h, cols->w 这里可以相应放大（缩小）倍数
    print(h,w)
    # 相关系数匹配方法：cv2.TM_CCOEFF
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    left_top = max_loc  # 左上角
    right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
    cv2.rectangle(imga, left_top, right_bottom, 255, 2)  # 画出矩形位置
    cv2.imshow('imagea',imga)
    cv2.waitKey()
    #返回点击坐标位置
    xy  = (int(left_top[0] + w/2), int(left_top[1]+ h/2))
    return xy

#因为截图是使用PIL所以要将PIL.iamge的图片类型转换到opencv的图片类型
def PIL_opencv(PIL_image):
    image = PIL_image
    img = cv2.cvtColor(py.asarray(image),cv2.TM_CCOEFF)
    #cv2.imshow("opencv",img)
    cv2.waitKey()
    return img

# cv2.imshow("opencv",yysclient)

# #读取图标
# yuling_pic = cv2.imread('pic/yuling.png',0)
# yuhun_pic = cv2.imread('pic/yuhun.png',0)
# yuhundashe_pic = cv2.imread('pic/yuhundashe.png', 0)
# print(type(yuhundashe_pic))
# yuhuntiaozhan_pic = cv2.imread('pic/yuhuntiaozhan.png', 0)
# yuhun_jieshu_pic = cv2.imread('pic/jieshu.png', 0)
#
# yuhun_jieshu_pic_s = cv2.imread('pic/jieshu.png')
# # cv2.imshow("opencv",yuling_pic)
# # cv2.imshow("opencv",yuhun_pic)
# # cv2.waitKey()
#
# #进行比对并标点
# #选择御魂图标并点击
# yysclient = opencvjietu.yys_client()
# #yysclient.show()
# yysclient = PIL_opencv(yysclient)
# yuhun_xy = template_matching(yysclient,yuhun_pic)
# mousedianji.mouse_click(yuhun_xy[0], yuhun_xy[1],3)
#
# #选择御魂-八岐大蛇
# yuhunclient = opencvjietu.yys_client()
# yuhunclient = PIL_opencv(yuhunclient)
# dasheyyh_xy = template_matching(yuhunclient, yuhundashe_pic)
# mousedianji.mouse_click(dasheyyh_xy[0], dasheyyh_xy[1],0)
#
# #选择挑战图标
# yysclient = opencvjietu.yys_client()
# yysclient = PIL_opencv(yysclient)
# yuhuntiaozhan_xy = template_matching(yysclient, yuhuntiaozhan_pic)
# mousedianji.mouse_click(yuhuntiaozhan_xy[0], yuhuntiaozhan_xy[1],0)
#
# #其实可以写成函数的
#
# s = 10
#
# while s >= 5:
#     yysclient_jieshu = opencvjietu.jieshu()
#     yysclient_jieshu = PIL_opencv(yysclient_jieshu)
#     s = similarity.classify_aHash(yuhun_jieshu_pic_s, yysclient_jieshu)
#     print(s)
#     if s<=5:
#         yysclient = opencvjietu.yys_client()
#         yysclient = PIL_opencv(yysclient)
#         a = template_matching(yysclient, yuhun_jieshu_pic)
#     time.sleep(2)
# mousedianji.mouse_click(a[0], a[1], 0)

