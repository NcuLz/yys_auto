#鼠标事件，用于鼠标的操作，切记要获得管理员权限才能进行鼠标操作 如单击，滑动等，
#在pycharm IDE编译器中只需要将pychram以管理员身份启动即可，这样里面的程序就会获得管理员权限了。
#author：lz

import win32api
import win32con
import time
import random
import opencvjietu
#鼠标事件
def mouse_click(x, y, t):#点击鼠标并移动
    #获取客户端当前的左上角的坐标
    x0,y0 = opencvjietu.window_size[0], opencvjietu.window_size[1]
    #相对位置
    # x = int(opencvjietu.get_posx(x, opencvjietu.window_size))
    # y = int(opencvjietu.get_posy(y, opencvjietu.window_size))
    #实际位置
    x = x0+x
    y = y0+y
    #在实际位置上加上随机晃动
    x = x + random.randint(-10,10)
    y = y + random.randint(-5,5)
    print("鼠标点的位置",x, y)
    #鼠标随机移动
    random_point = ((x+random.randint(-200, 300)), (y+random.randint(-200, 300)))
    win32api.SetCursorPos(random_point)

    win32api.SetCursorPos((x,y))#鼠标定位到（x，y）
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)#鼠标事件，左键单击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    random_point = ((x + random.randint(-200, 300)), (y + random.randint(-200, 300)))
    win32api.SetCursorPos(random_point)
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    if t == 0:#控制点击频率
        time.sleep(random.random()*2+1)
    else:
        time.sleep(t)
#move_click(30,30,0)
#mouse_click(147,474, 0)
