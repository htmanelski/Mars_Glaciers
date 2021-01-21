#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:21:28 2021

@author: henrymanelski
"""
from math import cos, asin, sqrt, pi
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms

# importing the csv
gla = pd.read_csv (r'glaciers.csv')

# deleting columns I don't care about 
del gla['Feature:string']
del gla['GLF#:integer']
del gla['parent_ima:string']
del gla['glf_head_e:double']
del gla['glf_head_l:double']
del gla['glf_termin:double']
del gla['midchannel:double']
del gla['midchannel2:double']
del gla['midchannel1:double']
del gla['midchannel3:double']
del gla['center_e_l:double']
del gla['center_lat:double']
del gla['glf_length:double']
del gla['glf_width_:double']
del gla['glf_orient:double']
del gla['buffer_min:double']
del gla['buffer_max:double']
del gla['buffer_std:double']
del gla['elongation:double']
del gla['Fill Color:color']
del gla['glf_termin1:double']

# lat long values 
input_lat=input("Enter a latitude (decimal): ")
input_long=input("Enter a longitude (decimal, 0-360 E): ")
input_lat=float(input_lat)
input_long=float(input_long)

# distance function
def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 6779 * asin(sqrt(a)) 

distances = []

i = 0 
while (i < len(gla.index)):
    
    distances.append(distance(input_lat,input_long,gla.loc[i,'latitude'],gla.loc[i,'longitude']))
    i=i+1
    
distances = np.array(distances)

# find the "k" nearest glaciers
k = 10

# finding the smallest distances
smallest_dist=[]
smallest_dist = distances[smallest_dist[:k]]

# getting the indices of the smallest distances
ind_s_dist = np.argpartition(distances,k)[:k]

# creating a new array of the smallest lon
result_lon =[]
i=0
while (i<k):
    result_lon.append(gla.loc[ind_s_dist[i],'longitude'])
    i=i+1
    
# creating a new array of the smallest lat
result_lat =[]
i=0
while (i<k):
    result_lat.append(gla.loc[ind_s_dist[i],'latitude'])
    i=i+1
    
# now we have to scale to put it on the background image
scaled_lon = []
scaled_lat = []
i=0
while (i<k):
    
    # scaling function (based on pixel dimension of the background image)
    new_Long = (result_lon[i])*(2312/360)
    new_Long = new_Long + 1157
    if (new_Long>2312):
        new_Long=new_Long-2312
    new_Lat = -((result_lat[i]-90)/90)*578.5 
    
    scaled_lon.append(new_Long)
    scaled_lat.append(new_Lat)
    
    i=i+1

# now we have to scale the input longitude and latitude. I hate my life. 
scaled_input_long = (input_long)*(2312/360)+ 1157
if (scaled_input_long>2312):
    scaled_input_long = scaled_input_long-2312
scaled_input_lat = -((input_lat-90)/90)*578.5 
    
# finding cool area statistics
area = []

i=0
while (i<k):
    area.append(gla.loc[ind_s_dist[i],'glf_area_s:double'])
    i=i+1
    
area=np.array(area)

avg_area = str(int(np.average(area)))
sum_area = str(int(np.sum(area)))

the_closest = distances[np.argpartition(distances,1)[:1]]

smallest_distances = distances[np.argpartition(distances,k)[:k]]

# we are going to want to print maybe the n smallest distances
n=3

# indicies of the smallest ones
ind_smallest =  np.argpartition(distances,n)[:n]

# creating a new array of the smallest n lon
smallest_n_lon =[]
i=0
while (i<n):
    smallest_n_lon.append(gla.loc[ind_smallest[i],'longitude'])
    i=i+1
    
# creating a new array of the smallest n lat
smallest_n_lat =[]
i=0
while (i<n):
    smallest_n_lat.append(gla.loc[ind_smallest[i],'latitude'])
    i=i+1


deg = u'\xb0'

# huge line we will want to print
line = "\nThe average distance to the nearest \n"+str(k)+"  glaciers is " + str(int(np.average(smallest_distances))) +  " kilometers. " + "\nThe total area of these glaciers is \n" + sum_area + " km^2. The average area is " + avg_area + "km^2. " + "\n\nThe closest glacier is "+ str(int(the_closest[0])) + " km away. "

line3 = ""
i = 0 
while (i<n):
    line3 = line3 + "\n(" + str(smallest_n_lat[i]) + str(deg) + ", " + str(smallest_n_lon[i]) + str(deg) +  "E)"
    i=i+1
    
line2 = "\n\nThe nearest " + str(n) + " glaciers are at: " + str(line3)



# plotting stuff
plt.scatter(scaled_lon, scaled_lat,alpha=0.6,color='Red', s=10,label="Nearest glaciers")
plt.scatter(scaled_input_long,scaled_input_lat,alpha=0.6, color='Yellow', s=10, label="Chosen location")

plt.tight_layout()
im = plt.imread("map2.png")
implot = plt.imshow(im)
plt.axis('off')
plt.legend(loc='center right',fancybox=True, framealpha=1, shadow=True, borderpad=1, bbox_to_anchor=(1.39, 0.50), markerscale=3)

plt.title('Closest '+ str(k) + ' glaciers to (' +str(input_lat) + '$^\degree$, ' + str(input_long) +'$^\degree$ E)',fontsize=25, weight=700,family='Arial Narrow')
plt.savefig('nearest_glaciers.jpeg', dpi=500, bbox_inches='tight') 
#plt.text(2450,250,line, horizontalalignment='left')
plt.show()

# print statements
print(line)
print(line2)

# spaceX landing site example: 39.083 , 189.793
# bradbury landing: -4.5895 , 137.4417
