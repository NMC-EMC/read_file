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

file_path = 'X:\data-cdrom\\2020\surface\\visib'
filename = '20031119.000'

#==================定义函数部分=============
def sim_sk(file_path,filename):
    with open(r'{0}\{1}'.format(file_path,filename), 'r', encoding='gbk') as f:  # 读取文件
        info = f.readlines()[3:]  # 跳过前3行
        sta, lon, lat, vis = [], [], [], []
        for i in info:
            line = i.strip().split()
            sta.append(int(line[0]))
            lon.append(float(line[1]))
            lat.append(float(line[2]))
            vis.append(float(line[4]))
    sta = np.array(sta).reshape((-1, 1))
    lon = np.array(lon).reshape((-1, 1))
    lat = np.array(lat).reshape((-1, 1))
    vis = np.array(vis).reshape((-1, 1,))
    return  sta,lon, lat, vis

#=================调用函数================
station, Lon, Lat, Vis_obs = sim_sk(file_path,filename)