#!/usr/bin/env python3
# -*- coding utf-8 -*-
#===author：liuchao
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate
import  datetime
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl

#=====================(1)读plot站点文件========================
file_path = 'Z:\data\surface\plot_hc'
filename = '20031219.000'

#===========定义函数部分====================
def plot_hc(file_path,filename):
    with open(r'{0}\{1}'.format(file_path,filename), 'r', encoding='gbk') as f:
        sta, lon, lat, temp = [], [], [], []
        for i in f:  # 此方法用于通过缩进的方式把数据提取出来
            line = i.strip().split()
            if len(line) > 5:   #这里是大于5个空格
                sta.append(int(line[0]))    # 提取站点号
                lon.append(float(line[1]))  # 提取经度
                lat.append(float(line[2]))  # 提取纬度
                temp.append(float(line[16])) # 这里要提取温度变量
        sta = np.array(sta).reshape((-1,1))
        lon = np.array(lon).reshape((-1,1))
        lat = np.array(lat).reshape((-1,1))
        temp = np.array(temp).reshape((-1,1,))

    return  sta,lon, lat, temp

#=================调用函数================
station, Lon, Lat, var = plot_hc(file_path,filename)
