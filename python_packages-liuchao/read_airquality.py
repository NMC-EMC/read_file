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

#==================(3)读空气质量站点数据========================================
file_path = 'X:\AQI\\2020'
filename = '2020031123.000'

#==================定义函数部分=============
def air_quality_sk(file_path,filename):
    with open(r'{0}\{1}'.format(file_path,filename), 'r', encoding='gbk') as f:  # 读取文件
        info = f.readlines()[1:]  # 跳过前1行
        sta, lon, lat, aqi = [], [], [], []
        for i in info:
            line = i.strip().split()
            sta.append(int(line[0]))
            lon.append(float(line[1]))
            lat.append(float(line[2]))
            aqi.append(float(line[3]))
    sta = np.array(sta).reshape((-1, 1))
    lon = np.array(lon).reshape((-1, 1))
    lat = np.array(lat).reshape((-1, 1))
    aqi = np.array(aqi).reshape((-1, 1,))
    return  sta,lon, lat, aqi

#=================调用函数================
station, Lon, Lat, AQI = air_quality_sk(file_path,filename)