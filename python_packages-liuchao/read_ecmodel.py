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

#======================(4)读取EC格点数据=========================================
file_path = 'Z:\data\\newecmwf_grib\\rh\\2'
filename = '20030208.000'
def ecmodel(file_path, filename, lon_min = 60.0, lon_max = 150.0, lat_min = -10.0, lat_max = 60.0, grid_interval = 0.25, lon_1 = 60.0,lon_2 = 120.0,lat_1 = 10.0,lat_2 = 50):
    """
    :param grid_data: 格点场数据
    :param lon_min: 起始经度
    :param lon_max: 终止经度
    :param lat_min: 起始纬度
    :param lat_max: 终止纬度
    :param grid_interval: 经度间隔
    :param lon_1: 用户起始经度
    :param lon_2: 用户终止经度
    :param lat_1: 用户起始纬度
    :param lat_2: 用户终止纬度
    """
    ec_data = []
    with open(r'{0}\{1}'.format(file_path,filename), 'r', encoding='gbk') as f:
         str_data = f.readlines()[2:]
         kk = []
         for idx, i in enumerate(str_data, 1):
             dt = [float(k) for k in i.strip().split()]
             if len(dt) != 1:
                 kk.extend(dt)
             else:
                 kk.extend(dt)
                 ec_data.extend(kk)
                 kk.clear()
    ec_data = np.array(ec_data).reshape((281, 361))  #提取EC模式数据
    lat_range = np.arange(lat_min, lat_max + grid_interval, grid_interval)[::-1]
    lon_range = np.arange(lon_min, lon_max + grid_interval, grid_interval)
    lon_grid, lat_grid = np.meshgrid(lon_range, lat_range)
    lat_index = np.where((lat_grid[:, 0] >= lat_1) & (lat_grid[:, 0] <= lat_2))[0]  # 生成的turple给0
    lon_index = np.where((lon_grid[0, :] >= lon_1) & (lon_grid[0, :] <= lon_2))[0]  # 取第0行所有满足要求的列
    Lon = lon_grid[lat_index, :][:, lon_index]
    Lat = lat_grid[lat_index, :][:, lon_index]
    ec_data = ec_data[lat_index, :][:, lon_index]
    return Lon, Lat,ec_data

#只要修改模式经纬度和网格间隔以及想要提取的数据范围即可
lon,lat,data = ecmodel(file_path,filename,lon_min = 60.0, lon_max = 150.0, lat_min = -10.0, lat_max = 60.0, grid_interval = 0.25,lon_1 = 60.0,lon_2 = 90.0,lat_1 = 30.0,lat_2 = 50)
