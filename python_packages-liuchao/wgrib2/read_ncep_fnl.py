#!/usr/bin/env python3
# -*- coding utf-8 -*-
#===author：liuchao
import os
import numpy as np
import pandas as pd
os.chdir('C:\Python37\wgrib2')
filepath = 'C:\Python37\wgrib2'
gribfilename='fnl_201912080000.grib2'
outfilename='data.csv'

#os.system(os.path.abspath('.')+'\wgrib\wgrib.exe '+gribfilename+' -d 1 -text -nh -o '+outfilename)
os.system(r"wgrib2 "+gribfilename+"  -match ':UGRD:950 mb'  -csv "+outfilename)  #此处需要修改变量
#os.system(r"wgrib2 fnl_201912080000.grib2 -v")
#========================定义函数==============
def read_fnl(filepath,outfilename,lat_1 = 30.0,lat_2 = 50.0,lon_1 = 105,lon_2 = 125):
    data = pd.read_csv(r'{0}\{1}'.format(filepath,outfilename), header=None) #header不带文件头

    #读取再分析数据处理
    lon = data[4]  #读取第四列赋给经度
    lon = np.array(lon)
    lon = np.array(lon.astype(int)).reshape((181, 360))   #astype指定类型，并形成一个二维数组
    lon_index = np.where((lon[0, :] >= lon_1) & (lon[0, :] <= lon_2))[0]  #取第0行所有满足要求的列

    lat = data[5]
    lat = np.array(lat.astype(int)).reshape((181, 360))
    lat_index = np.where((lat[:, 0] >= lat_1) & (lat[:, 0] <= lat_2))[0]  #生成的turple给0

    u = np.array(data[6]).reshape((181, 360))
    u = u[lat_index, :][:,lon_index]

    Lon = lon[lat_index, :][:,lon_index]
    Lat = lat[lat_index ,:][:,lon_index]
    return Lon,Lat,u

#=================调用函数================	
lon,lat,var = read_fnl(filepath,outfilename,lat_1 = 10.0,lat_2 = 50.0,lon_1 = 70,lon_2 = 125)
