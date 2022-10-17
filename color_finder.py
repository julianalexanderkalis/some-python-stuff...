#import for finding the dominant colors
import matplotlib
import PIL
import scipy
import matplotlib.pyplot as plt
from matplotlib import image as img

#read the image source
image = img.imread('Path/to/image')

#define, how many colors to look at
number_of_colors = 8

#image.shape
#plt.imshow(image);
 
r = []
g = []
b = []

#append each pixelvalues to the respective RGB list
for line in image:
    
    for pixel in line:
        
        temp_r, temp_g, temp_b = pixel
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

#some importing
from mpl_toolkits.mplot3d import Axes3D

#unnecessary stuff

#-----------------------------------------------------------------------------------------------
#fig = plt.figure()
#ax = Axes3D(fig)
#ax.scatter(r, g, b)
#plt.show()
#-----------------------------------------------------------------------------------------------


#creating dataframe
import pandas as pd
df = pd.DataFrame({'red': r, 'blue': b, 'green': g})

from scipy.cluster.vq import whiten

df['scaled_red'] = whiten(df['red'])
df['scaled_blue'] = whiten(df['blue'])
df['scaled_green'] = whiten(df['green'])

df.sample(n=10)

#performing cluster analysis
from scipy.cluster.vq import kmeans

cluster_centers, distortion = kmeans(df[['scaled_red', 'scaled_green', 'scaled_blue']], number_of_colors)


colors = []
r_std, g_std, b_std = df[['red', 'green', 'blue']].std()

for cluster_center in cluster_centers:
    
    scaled_r, scaled_g, scaled_b = cluster_center
    colors.append((scaled_r * r_std / 255, 
                  scaled_g * g_std / 255, 
                  scaled_b * b_std / 255))
    
plt.imshow([colors])

#plot the colors, not necessary
plt.show() 

#information about computing time:

#------------------------------------------------------------------------------------------
#11 sec für 5 cluster
#13 sec für 10 cluster
#26 sec für 20 cluster

#without plotting the scatterplot: 25% percent faster!!!
#------------------------------------------------------------------------------------------

#create a list with the color values ranging from 0 to 255
relevant_colors = []
temp_value = 0

for item in colors:
    
    temp_list = []
    
    for value in item:
        
        temp_list.append(value * 255)
    relevant_colors.append(temp_list)
    
    temp_list = []
    
#print(relevant_colors)