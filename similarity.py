import cv2
import numpy as np
from matplotlib import pyplot as plt


# 最简单的以灰度直方图作为相似比较的实现
def classify_gray_hist(image1,image2,size = (256,256)):
 # 先计算直方图
 # 几个参数必须用方括号括起来
 # 这里直接用灰度图计算直方图，所以是使用第一个通道，
 # 也可以进行通道分离后，得到多个通道的直方图
 # bins 取为16
 image1 = cv2.resize(image1,size)
 image2 = cv2.resize(image2,size)
 hist1 = cv2.calcHist([image1],[0],None,[256],[0.0,255.0])
 hist2 = cv2.calcHist([image2],[0],None,[256],[0.0,255.0])
 # 可以比较下直方图
 plt.plot(range(256),hist1,'r')
 plt.plot(range(256),hist2,'b')
 plt.show()
 # 计算直方图的重合度
 degree = 0
 for i in range(len(hist1)):
  if hist1[i] != hist2[i]:
   degree = degree + (1 - abs(hist1[i]-hist2[i])/max(hist1[i],hist2[i]))
  else:
   degree = degree + 1
 degree = degree/len(hist1)
 return degree

# 平均哈希算法计算
def classify_aHash(image1,image2):
 image1 = cv2.resize(image1,(8,8))
 image2 = cv2.resize(image2,(8,8))
 gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
 gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
 hash1 = getHash(gray1)
 hash2 = getHash(gray2)
 return Hamming_distance(hash1,hash2)

# 输入灰度图，返回hash
def getHash(image):
 avreage = np.mean(image)
 hash = []
 for i in range(image.shape[0]):
  for j in range(image.shape[1]):
   if image[i,j] > avreage:
    hash.append(1)
   else:
    hash.append(0)
 return hash
# 计算汉明距离
def Hamming_distance(hash1,hash2):
 num = 0
 for index in range(len(hash1)):
  if hash1[index] != hash2[index]:
   num += 1
 return num
#jiejie = cv2.imread('pic/juexing.png')
# cv2.imshow('img2',jiejie)
# cv2.waitKey()
#yuhun = cv2.imread('pic/juexing.png')
#print(classify_gray_hist(jiejie, yuhun))
#print(classify_aHash(jiejie, yuhun))