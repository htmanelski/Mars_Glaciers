"""
Created on Thu Oct 29 16:29:06 2020

@author: henrymanelski
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importing the csv
gla = pd.read_csv (r'glaciers.csv')




# visualiazation df  
vis_gla=gla 

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

# lets plot some cool stuff: starting with area vs elevation
plt.scatter(x=gla['buffer_mea:double'], y=gla['glf_area_s:double'],alpha=0.6,color='Blue', s=2)
plt.title("Area vs Elevation of Glaciers on Mars")
plt.xlabel('Elevation (m)')
plt.ylabel('Area (km^2)')
plt.savefig('area_vs_elevation_glaciers.jpeg')  
plt.show()

# lets split things into north and south cause why not 
north = pd.DataFrame()
south = pd.DataFrame()
for x in gla.index:
    north = gla.loc[gla['latitude'] > 0]
    south = gla.loc[gla['latitude'] < 0]
    
# area vs elevation in the north
plt.scatter(x=north['buffer_mea:double'], y=north['glf_area_s:double'],alpha=0.6,color='Blue', s=2)
plt.title("Area vs Elevation of Glaciers on Mars in Northern Latitudes")
plt.xlabel('Elevation (m)')
plt.ylabel('Area (km^2)')
plt.savefig('northern_glaciers.jpeg')  
plt.show()

# area vs elevation in the south
plt.scatter(x=south['buffer_mea:double'], y=south['glf_area_s:double'],alpha=0.6,color='Blue', s=2)
plt.title("Area vs Elevation of Glaciers on Mars in Southern Latitudes")
plt.xlabel('Elevation (m)')
plt.ylabel('Area (km^2)')
plt.savefig('southern_glaciers.jpeg')  
plt.show()

# now lets just create a csv summarizing the results
south.describe().to_csv('southern_glacier_summary.csv', index = False)
north.describe().to_csv('northern_glacier_summary.csv', index = False)


 
# we are going to seperate small medium and large glaciers. Boundaries 
# are arbitrary. 
small=pd.DataFrame()
medium=pd.DataFrame()
large=pd.DataFrame()

# now we need to scale things. we need to turn a lat/long into a pixel
# dimension so we need some math
for x in gla.index:
    '''
    # scaling function (based on pixel dimension of the background image)
    new_Long = (gla.loc[x,'longitude'])*(1024/360)
    new_Long = new_Long + 515
    if (new_Long>1024):
        new_Long=new_Long-1024
    new_Lat = -((gla.loc[x,'latitude']-90)/90)*250.5 
    '''
    
    # scaling function (based on pixel dimension of the background image)
    new_Long = (gla.loc[x,'longitude'])*(2312/360)
    new_Long = new_Long + 1157
    if (new_Long>2312):
        new_Long=new_Long-2312
    new_Lat = -((gla.loc[x,'latitude']-90)/90)*578.5 
    
    
    
    interm = pd.DataFrame({'longitude': [new_Long], 'latitude':[new_Lat]})
    
    # seperating the glaciers by size
    if (-9000<gla.loc[x,'buffer_mea:double']<8000):
        if (0<gla.loc[x,'glf_area_s:double']<10):
            combine=[small,interm]
            small=pd.concat(combine)
        if (10<gla.loc[x,'glf_area_s:double']<50):
            combine=[medium,interm]
            medium=pd.concat(combine)
        if (50<gla.loc[x,'glf_area_s:double']<200):
            combine=[large,interm]
            large=pd.concat(combine)
            
# printing them out by size 
plt.scatter(x=small['longitude'], y=small['latitude'],alpha=0.6,color='Blue', s=2, label="0-10 $km^2$ ")
plt.scatter(x=medium['longitude'], y=medium['latitude'],alpha=0.6,color='Green', s=2, label="10-50 $km^2$ ")
plt.scatter(x=large['longitude'], y=large['latitude'],alpha=0.6,color='Red', s=2, label="50-200 $km^2$ ")
plt.legend(loc='best',fancybox=True, framealpha=1, shadow=True, borderpad=1, bbox_to_anchor=(1.05, 1), markerscale=5, title="Area")

# formatting all nice and creating the jpeg 
plt.tight_layout()
plt.axis('off')
plt.title('Mid-Latitude \n Glaciers on Mars',fontsize=25, weight=700,family='Arial Narrow')
im = plt.imread("map2.png")
implot = plt.imshow(im)
plt.savefig('glacier_map.jpeg', dpi=500)  
plt.show()

# heat map time
x=vis_gla['longitude']
y=vis_gla['latitude']
heatmap, xedges, yedges = np.histogram2d(x, y, bins=(128,62))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.clf()
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.savefig('heatmap_glaciers.jpeg')
plt.show()