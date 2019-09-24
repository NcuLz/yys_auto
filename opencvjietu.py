#程序实现使用PIL屏幕进行截图
from  PIL import ImageGrab
import win32gui
import win32api
from ctypes import *
from ctypes.wintypes import *



def Resolving_power():
    return win32api.GetSystemMetrics(0),win32api.GetSystemMetrics(1)
print(Resolving_power())

def get_windows_info():#获取阴阳师窗口信息
    wdname = u'阴阳师-网易游戏'
    handle = win32gui.FindWindow(0, wdname)#获取窗口句柄
    if handle ==0:
        print('阴阳师客户端没有打开！！！')
        return None
    else:

        print(win32gui.GetWindowRect(handle))#
        print(win32gui.GetClientRect(handle))
        return win32gui.GetWindowRect(handle),win32gui.GetClientRect(handle)

        #get_window_info()函数返回 自带方法获取的窗口截图的大小会带上windows的毛边效果不是真正的窗口大小
        #https://blog.csdn.net/muslim377287976/article/details/90730214
        # 阴阳师窗口信息(x1, y1, x2, y2)，(x1, y1)是窗口左上角的坐标，(x1, y1)

#截图功能函数,传参x,y是要截取图片的左上角和右下角在屏幕中的坐标位置
def jietu(xtop,ytop,xbottom,ybottom):
    img = ImageGrab.grab((xtop,ytop,xbottom,ybottom))
    return img

#获取截图的相对坐标
def get_posx(x, window_size):#返回x相对坐标
    return (window_size[2] - window_size[0])* x /859
def get_posy(y, window_size):
    return (window_size[3] - window_size[1])* y / 514

#返回整个屏幕的截图
def yys_client():

    topx = window_size[0]
    topy = window_size[1]
    bottomx = window_size[2]
    bottomy = window_size[3]
    image = jietu(topx, topy, bottomx, bottomy)
    return image

#返回图标截图并保存
def tubiao_jietu():
    #御灵图标在图中的相对位置
    topx = window_size[0]
    topy = window_size[1]
    #御灵图标的相对位置
    img_yuling = ImageGrab.grab((topx + get_posx(247, window_size), topy + get_posy(435, window_size),
                           topx + get_posx(320, window_size), topy + get_posy(485, window_size)))
    #img_yuling.show()
    #img_yuling.save('pic/yuling.png')
    #print("调用测试")

    #结界突破图标截图 下面是相对位置
    img_jiejie = ImageGrab.grab((topx + get_posx(180, window_size), topy + get_posy(435, window_size), topx + get_posx(246, window_size),topy + get_posy(485, window_size)))
    #img_jiejie.show()
    #img_jiejie.save('pic/jiejietupo.png')

    #御魂图标截图，下面是相对位置
    img_yuhun = ImageGrab.grab((topx + get_posx(111, window_size), topy + get_posy(435, window_size), topx + get_posx(173, window_size),topy + get_posy(485, window_size)))
    #img_yuhun.show()
    #img_yuhun.save('pic/yuhun.png')


    #觉醒图标，下面是结界突破的图标位置
    img_juexing = ImageGrab.grab((topx + get_posx(35, window_size), topy + get_posy(435, window_size), topx + get_posx(105, window_size),topy + get_posy(485, window_size)))
    #img_juexing.show()
    #img_juexing.save('pic/juexing.png')
    #探索

    #御魂八歧大蛇选择图标
    img_yuhun_dashe = ImageGrab.grab((topx + get_posx(150, window_size), topy + get_posy(150, window_size),
                                  topx + get_posx(400, window_size), topy + get_posy(400, window_size)))
    # img_yuhun_dashe.show()
    # img_yuhun_dashe.save('pic/yuhundashe.png')

    #御魂业原火选择图标
    img_yuhun_yyh = ImageGrab.grab((topx + get_posx(500, window_size), topy + get_posy(150, window_size),
                                  topx + get_posx(750, window_size), topy + get_posy(380, window_size)))
    # img_yuhun_yyh.show()
    # img_yuhun_yyh.save('pic/yuhunyyh.png')

    #御魂选择开始
    img_yuhun_tiaozhan = ImageGrab.grab((topx + get_posx(600, window_size), topy + get_posy(340, window_size),
                                  topx + get_posx(680, window_size), topy + get_posy(380, window_size)))
    #  img_yuhun_tiaozhan.show()
    # img_yuhun_tiaozhan.save('pic/yuhuntiaozhan.png')

    #结束时截图
    # img_yuhun_tiaozhan = ImageGrab.grab((topx + get_posx(380, window_size), topy + get_posy(350, window_size),
    #                                      topx + get_posx(480, window_size), topy + get_posy(450, window_size)))
    # img_yuhun_tiaozhan.show()
    #img_yuhun_tiaozhan.save('pic/jieshu.png')

def jieshu():
    topx = window_size[0]
    topy = window_size[1]
    img_yuhun_jieshu = ImageGrab.grab((topx + get_posx(380, window_size), topy + get_posy(350, window_size),
                                         topx + get_posx(480, window_size), topy + get_posy(450, window_size)))
    #img_yuhun_jieshu.show()
    # img_yuhun_tiaozhan.save('pic/jieshu.png')
    return img_yuhun_jieshu
def jiacheng():
    topx = window_size[0]
    topy = window_size[1]
    #加成图标
    img_jiacheng = ImageGrab.grab((topx + get_posx(282, window_size), topy + get_posy(40, window_size),
                                   topx + get_posx(315, window_size), topy + get_posy(75, window_size)))
    # img_jiacheng.show()
    # img_jiacheng.save('pic/jiacheng.png')


    #御魂加成
    img_yuhun_jiacheng = ImageGrab.grab((topx + get_posx(250, window_size), topy + get_posy(155, window_size),
                                         topx + get_posx(320, window_size), topy + get_posy(195, window_size)))
    img_yuhun_jiacheng.show()
    img_yuhun_jiacheng.save('pic/yuhunjiacheng.png')
    #觉醒加成
    # img_juexing_jiacheng = ImageGrab.grab((topx + get_posx(250, window_size), topy + get_posy(110, window_size),
    #                                      topx + get_posx(290, window_size), topy + get_posy(150, window_size)))
    # img_juexing_jiacheng.show()
    # img_juexing_jiacheng.save('pic/juexingjiacheng.png')

    return img_jiacheng
def yuling():
    topx = window_size[0]
    topy = window_size[1]
    #黑豹
    img_yuling_heibao = ImageGrab.grab((topx + get_posx(450, window_size), topy + get_posy(150, window_size),
                                         topx + get_posx(600, window_size), topy + get_posy(450, window_size)))
    # img_yuling_heibao.show()
    # img_yuling_heibao.save('pic/yuling_heibao.png')
    #孔雀
    img_yuling_kongque = ImageGrab.grab((topx + get_posx(600, window_size), topy + get_posy(150, window_size),
                                         topx + get_posx(750, window_size), topy + get_posy(450, window_size)))
    # img_yuling_kongque.show()
    # img_yuling_kongque.save('pic/yuling_kongque.png')

#战斗失败截图
def defeated():
    topx = window_size[0]
    topy = window_size[1]
    #战斗失败
    defeated = ImageGrab.grab((topx + get_posx(200, window_size), topy + get_posy(320, window_size),
                                         topx + get_posx(650, window_size), topy + get_posy(420, window_size)))

    # defeated.show()
    # defeated.save('pic/defeated.png')
    return defeated

window_size, client_size = get_windows_info()
print(window_size)
#yys_client().show()
# yys_client().save('pic/yuhunshibai.png')
tubiao_jietu()
#jieshu()
#jiacheng()
#yuling()
# defeated()