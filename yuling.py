import opencv_compare
import opencvjietu
import mousedianji
import similarity
import cv2
import time
import random
import queue


# 读取图标
# 读取御灵图标
yuling_pic = cv2.imread('pic/yuling.png', 0)
# 读取御御灵图标
yulingheibao_pic = cv2.imread('pic/yuling_heibao.png', 0)
yulingkongque_pic = cv2.imread('pic/yuling_kongque.png', 0)
# 读取开始图标
yulingtiaozhan_pic = cv2.imread('pic/tiaozhan.png', 0)
# 读取结束图标
yuling_jieshu_pic = cv2.imread('pic/jieshu.png', 0)
# 读取结束时的图标 判断是否结束
yuling_jieshu_pic_s = cv2.imread('pic/jieshu.png')
# 读取御灵失败时的图片
img_defeated = cv2.imread('pic/defeated.png')

#循环队列
def judge_queue(s):
    #队列长度：
    size = 3
    i=0
    a=[]
    q = queue.Queue(size)
    if q.qsize()<=size:
        q.put(s)
    elif q.full():
        while not q.empty():
            a[i]=q.get()
            i = i+1
        if a[0]==a[1]==a[2]:
            print("图片相同")
            return True
        else:
            for j in range(0,i):
                q.put(a[j+1])
                if j==i-1:
                    break
# 御魂失败
# def yuhundefeat(image_shibai,image, s):
#     if judge_queue(s)==1:
        #连续三次返回的都是相同的数字可以认为是失败了





# 验证是否正确找到目标
def checking(jietufun,imga):
    #作为验证函数 其参数为截图的方法，如截取当前阴阳师客户端全部，或者截取部分区域，另外参数imga是作为对照的图片
    #验证方法在sinularity.py中
    #返回两张图片的汉明距离
    image = imga
    s = 10 #汉明距离的初始值，小于5基本相似
    while s >= 5:
        yysclient_jieshu = jietufun()
        yysclient_jieshu = opencv_compare.PIL_opencv(yysclient_jieshu)
        s = similarity.classify_aHash(image, yysclient_jieshu)

    return s

# 截取当前图片，输入要标出的图片位置并返回坐标点
def feature_matching(imga):
    #参数是需要找出图片，原图片直接在函数中截取
    image = imga
    yysclient = opencvjietu.yys_client()
    yysclient = opencv_compare.PIL_opencv(yysclient)#截取图片
    result = opencv_compare.template_matching(yysclient, image)
    return result

# 进行比对并标点
# 选择御魂图标并点击
def yuhun_tubiao():
    yuhun_xy = feature_matching(yuling_pic)
    mousedianji.mouse_click(yuhun_xy[0], yuhun_xy[1], 3)

#选择八岐大蛇图标、
def yuhun_dashe_tubiao():
    # 选择御魂-八岐大蛇
    dasheyyh_xy = feature_matching(yulingkongque_pic)
    mousedianji.mouse_click(dasheyyh_xy[0], dasheyyh_xy[1], 0)

# 选择挑战图标
def tiaozhan():
    yuhuntiaozhan_xy = feature_matching(yulingtiaozhan_pic)
    mousedianji.mouse_click(yuhuntiaozhan_xy[0], yuhuntiaozhan_xy[1], 0)


def yuhun(t):
    yuhun_tubiao()
    yuhun_dashe_tubiao()
    t=int(t)

    while t>0:
        tiaozhan()
        s = 10
        j =0
        #s= checking(opencvjietu.jieshu(),yuhun_jieshu_pic_s)
        while s >= 5:
            i = 10
            jieshu = opencvjietu.jieshu()
            jieshu = opencv_compare.PIL_opencv(jieshu)  # 截取图片
            s = similarity.classify_aHash(yuling_jieshu_pic_s, jieshu)
            #print(s)
            defeated = opencvjietu.defeated()
            defeated = opencv_compare.PIL_opencv(defeated)
            i = similarity.classify_aHash(img_defeated, defeated)
            #print('i=',i)
            if i< 10:
                tiaozhan()
                j = j+1#统计失败次数
                t = t+1
                print('这是第',j,'次失败！')
                break

            #设置一个队列，把s存入队列中当队列中的数值都一样时证明停留在了同一画面
            time.sleep(2)
        if s<5:
            a = feature_matching(yuling_jieshu_pic)
            mousedianji.mouse_click(a[0], a[1], 0)
        t=t-1
        time.sleep(random.randint(0, 3))
        print('阴阳师大人，小助手已经帮您刷了',1000-t,'次暗孔雀御灵了！总共失败',j,'次，继续加油哦！')
        #刷100，200，350，500，800次时停下来半个小时
        while t==800 or t==500 or t==300 or t==200 or t==100 :
            time.sleep(1800)




yuhun(1000)