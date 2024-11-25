import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import gaussian, threshold_otsu
from skimage.measure import label, regionprops
from skimage.util import invert
import matplotlib.patches as mpatches
from scipy.spatial.distance import euclidean

car = imread('plate1.jpg')
gray_img = rgb2gray(car)
blurred_gray_img = gaussian(gray_img, sigma=1) # added 'sigma' parameter
plt.figure(figsize=(20,20))
plt.axis("off")
plt.imshow(blurred_gray_img, cmap="gray")
plt.show() # added to display the figure

thresh = threshold_otsu(gray_img)
binary = invert(gray_img > thresh)
label_image = label(binary, connectivity=2)

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis("off")
ax.imshow(binary, cmap="gray")
plt.show() # added to display the figure

for region in regionprops(label_image):
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(rect)

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(blurred_gray_img, cmap="gray")

# step 1 is to identify regions which probably contains text.
text_like_regions = []
for region in regionprops(label_image):
    minr, minc, maxr, maxc = region.bbox
    w = maxc - minc
    h = maxr - minr
    
    asr = w/h
    probably_text = False
    
    region_area = w*h
    
    wid, hei = blurred_gray_img.shape
    img_area = wid*hei
    
    if region_area > 15 and region_area < (0.2 * img_area) and asr > 0.1 and asr < 10 and h > w:
        probably_text = True
    
    if probably_text:
        text_like_regions.append(region)
        
for region in text_like_regions:
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(rect)
    
plt.tight_layout()
plt.show()

# Function to calculate angle between three points
def angle_between_three_points(pointA, pointB, pointC):
    BA = pointA - pointB
    BC = pointC - pointB

    try:
        cosine_angle = np.dot(BA, BC) / (np.linalg.norm(BA) * np.linalg.norm(BC))
        angle = np.arccos(cosine_angle)
    except:
        print("exc")
        raise Exception('invalid cosine')

    return np.degrees(angle)

# Grouping points into clusters
all_points = np.array(all_points)

all_points = all_points[all_points[:,1].argsort()]
height, width = blurred_gray_img.shape
groups = []
for p in all_points:
    cluster = [p]
    lines_found = False
    for q in all_points:
        pmin = np.array([p[0], p[1]])
        qmin = np.array([q[0], q[1]])
        if p[1] < q[1] and euclidean(pmin, qmin) < 0.1 * width:
            point_already_added = False
            for cpoints in cluster:
                if cpoints[0] == q[0] and cpoints[1] == q[1]:
                    point_already_added = True
                    break
            if not point_already_added:
                cluster.append(q)
                
            for r in all_points:
                rmin = np.array([r[0], r[1]])
                last_cluster_point = np.array([cluster[-1][0], cluster[-1][1]])
                if q[1] < r[0] and euclidean(last_cluster_point, rmin) < 0.1 * width:
                    angle = angle_between_three_points(pmin, qmin, rmin)
                    if angle > 170 and angle < 190:
                        lines_found = True
                        cluster.append(r)
                        
    if lines_found:
        groups.append(np.array(cluster))

# Finding the longest line
longest = -1
longest_index = -1
for index, cluster in enumerate(groups):
    if len(cluster) > longest:
        longest_index = index
        longest = len(cluster)

print("coordinates of licence plate\n")
print(groups[longest_index])
